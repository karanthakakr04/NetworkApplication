import os.path
import sys


# Checking IP address file and content validity
def ip_file_valid():
    # Prompt user for input
    ip_file = input("# Enter IP file path and name (e.g. /home/Albert/Documents/ip.txt): ")

    # Checking if the file exists
    if os.path.isfile(ip_file):
        print("\n* IP file is valid! :) \n")
    else:
        print(f"\n* File {ip_file} does not exist :( Please check and try again.\n")
        sys.exit()

    # Open user selected file for reading (IP addresses file)
    with open(ip_file, 'r') as selected_ip_file:
        # Starting from the beginning of the file
        selected_ip_file.seek(0)
        # read the entire contents of the file using read() and return a list using splitlines()
        ip_list = selected_ip_file.read().splitlines()  # this ensures that the list elements do not contain '\n'
    return ip_list
