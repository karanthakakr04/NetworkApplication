import sys
import os.path
import time
import re
import paramiko
from datetime import datetime

# Checking username/password file
# Prompt user for input - USERNAME/PASSWORD file
user_credentials = input("# Enter login credentials file path and name (e.g. /home/Albert/Documents/login_cred.txt): ")

# Checking if the file exists
if os.path.isfile(user_credentials):
    print("\n* Username/Password file is valid! :) \n")
else:
    print(f"\n* File {user_credentials} does not exist :( Please check and try again.\n")
    sys.exit()

# Checking commands file
# Prompt user for input - COMMANDS FILE
cmd_file = input("# Enter commands file path and name (e.g. /home/Albert/Documents/command.txt): ")

# Checking if the file exists
if os.path.isfile(cmd_file):
    print("\n* Commands file is valid! :) \n")
else:
    print(f"\n* File {cmd_file} does not exist :( Please check and try again.\n")
    sys.exit()


# Open SSHv2 connection to the device
def ssh_connection(ip):
    # Creating SSH connection
    try:
        with open(user_credentials, 'r', encoding='utf-8') as selected_user_file:
            # Starting from the beginning of the file
            selected_user_file.seek(0)

            # use pattern matching to extract username and password
            result = re.match(r'(\w+),(\w+)', selected_user_file.readlines()[0].rstrip("\n"))
            if not result:
                print(f"File {user_credentials} doesn't contain a valid username/password.")
                sys.exit()
            # Grouping constructs break up a regex in Python into subexpressions or groups. This serves two purposes:
            # Grouping -- A group represents a single syntactic entity. Additional metacharacters apply to the entire
            # group as a unit.
            # Capturing -- Some grouping constructs also capture the portion of the search string that matches the
            # subexpression in the group. You can retrieve captured matches later through several different mechanisms.
            username = result.group(1)
            password = result.group(2)

        # Open SSH connection to Arista switches
        session = paramiko.SSHClient()

        # For testing purposes, this allows auto-accepting unknown host keys.
        # Do not use in production! The default would be RejectPolicy
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the device using the username and password
        session.connect(ip, username=username, password=password)

        # Start an interactive shell session on the router
        connection = session.invoke_shell()

        # Setting terminal length for entire output - disable pagination
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        # Entering global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        with open(cmd_file, 'r', encoding='utf-8') as selected_cmd_file:
            # Starting from the beginning of the file
            selected_cmd_file.seek(0)

            # Writing each line in the file to the device
            # Read and send the entire file line by line
            for command in selected_cmd_file:  # This approach is more Pythonic and can be quicker and more memory
                # efficient. Therefore, it is suggested you use this instead
                connection.send(command + '\n')  # We need this extra newline character for the commands to run
                time.sleep(2)

        # Checking command output for IOS syntax errors
        router_output = connection.recv(65535)

        # Checking command output for IOS syntax errors
        # NOTE: The 'b' represents an instance of the bytes type, because the network device does not return plain text
        # (type string) when querying it via SSH.
        if re.search(b"% Invalid input", router_output):
            print(f'* There was at least one IOS syntax error on the device {ip} :(\n')
        else:
            print(f'DONE for the device {ip}. Data sent to file at {datetime.now()}\n')  # use the datetime module to
            # print the current date and time

        # Part 1:
        # Test for reading command output
        # Note: Output from the router is a byte-like object which is why we use str conversion.
        # print(str(router_output) + '\n')

        # Part 2:
        # Searching for the CPU utilization value within the output of "show processes top once"
        # NOTE: In python 3, the default encoding is "utf-8", so you can directly use:
        cpu_usage = re.search(r'%Cpu\(s\):(\s)+(.+?)(\s)*us,', router_output.decode())  # decoding the bytes
        # object to produce a string (encoded to the popular 'UTF-8' format) and running a search on it

        # Extracting the second group which matches the actual value of the cpu utilization
        cpu_utilization = cpu_usage.group(2)

        # Opening the CPU utilization text file and appending the results
        with open(r'/home/karan/PycharmProjects/NetworkApp/cpu.txt', 'a', encoding='utf-8') as cpu_stats:
            cpu_stats.write(cpu_utilization + '\n')

        # Closing the ssh connection
        session.close()

    except paramiko.AuthenticationException:
        print("* Invalid username or password :( \n* Please check the username/password file or the device "
              "configuration.")
        print("* Closing program... Bye!")
