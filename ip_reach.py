import sys
import subprocess
import platform


# Checking IP reachability
def ip_reach(ip_list):
    for ip in ip_list:
        # Check to see which OS is the system running, depending on that we use necessary ping flags
        ping_flag = '-c'  # for Linux / MacOS / Unix
        if platform.system() == 'Windows':
            ping_flag = '-n'  # for Windows

        # Spawn a new child process using the 'subprocess' module
        # NOTE: Rather than passing a string to subprocess, our function passes a list of strings. The ping program
        # gets each argument separately (even if the argument has a space in it), so the shell does not process other
        # commands that are provided by the user after the ping command terminates. You do not have to explicitly set
        # shell=False - it is the default.
        ping_reply = subprocess.run(['ping', ip, ping_flag, '2'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                    universal_newlines=True)  # Never use 'shell=True' as it allows shell injection
        # the last parameter 'universal_newlines' returns the output in str format that way we don't need to use str()

        # Check if the ping is successful and that the script does not return true even if the IP is unreachable
        # NOTE: we use 'subprocess.PIPE' to capture the output so that we can use it in the below conditional expression
        if ping_reply.returncode == 0 and ('unreachable' not in ping_reply.stdout):  # returncode (also known as Exit
            # Status)
            print(f"\n* {ip} is reachable\n")
            continue
        else:
            print(f"\n* {ip} not reachable :( Check connectivity and try again.")
            sys.exit()
