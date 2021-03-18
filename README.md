# network-application

The goal of this project is to automate physical and virtual device configuration within a network. Although, some network admins still manage configuration manually which can be mentally and physically draning, it might often lead to errors in configuration files, losing track of changes and can be time-consuming. With a configuration automation tool, like this one, repetitive tasks can be executed with minimal manual intervention.  

# Recommended Environment / Setup

  > 3 Arista virtual switches

You will need to create an account (https://eos.arista.com/user-manager/?action=login) with Arista. Once you have an account and log in, go to the bottom of the page and click "Software Downloads" under the Support heading. Scroll down and expand vEOS-lab -> 4.20. Click on vEOS-lab-4.20.15M.vmdk to download. You will also need to expand vEOS-lab -> aboot and click on Aboot-veos-8.0.0.iso to download.

  > Virtual Box - Version 6.1.18 (a newer release should work fine)

Download here: https://www.virtualbox.org/wiki/Downloads. You will need to setup the vmdk and iso files. There is some configuration involved to be able to network with your host PC.

  > Python 3.6+ 
    
Download here: https://www.python.org/downloads/. Make sure to download the latest stable version for better support.

# Part 1 - Switch Configuration via Secure Shell (SSH)

The objective of this part is to automate commands on one or more switches using Python.

There are 3 files that can be used for configuration - username(s)/password(s), commands, and Internet Protocol (IP) addresses. The program will first check that the files are valid and that the IP addresses can be reached via ping. If the checks pass, then the program will run the commands below on all 3 Arista switches (must be running in Virtual Box). The ouput from the switches will need to be cleaned up for better readability, this is an arbitrary example to show the functionality.

![1](https://user-images.githubusercontent.com/17943347/111696468-b99c2280-880a-11eb-8cab-758f85e0a4b4.png)

If the checks pass, then the program will run the commands below on all 3 Arista switches (must be running in Virtual Box). The ouput from the switches will need to be cleaned up for better readability, this is an arbitrary example to show the functionality.

![cmd](https://user-images.githubusercontent.com/17943347/111696541-d0db1000-880a-11eb-857a-29a01875d3ac.png)

![2](https://user-images.githubusercontent.com/17943347/111696579-da647800-880a-11eb-84b7-d35560add4ff.png)

We can pass more commands to the arista switches to further explore the functionality.

![cmd_2](https://user-images.githubusercontent.com/17943347/111696902-3f1fd280-880b-11eb-8141-d58c689dc1b2.png)

![NetworkApp_Fourth_Run](https://user-images.githubusercontent.com/17943347/111697028-65de0900-880b-11eb-8660-545e3a3ddb1e.png)

# Part 2 - Extracting Network Parameter & Building Graph

The objective of this part is to extract the CPU utilization value from the switch and build a graph using python's matplotlib library.

Unlike the commands in part 1, we pass only one command to the arista switch inorder to get the CPU utilization value. Note that the program is going to verify all three files (usr.txt, cmd.txt, and ip.txt) even for this part of the project. 

![cmd_3](https://user-images.githubusercontent.com/17943347/111697346-d2f19e80-880b-11eb-8480-0c7d4b1f65bf.png)

The program will query the switch once every 10 seconds and extract the CPU parameter. 

![cpu](https://user-images.githubusercontent.com/17943347/111697688-41cef780-880c-11eb-8934-d64834e28d55.png)

![github_output](https://user-images.githubusercontent.com/17943347/111697512-0af8e180-880c-11eb-9b1c-988efe865404.png)

After saving the utilization values in a dedicated text file, in this case cpu.txt, we will use it to build a live graph that keeps updating as new entries are added.

![Arista_1_(2)](https://user-images.githubusercontent.com/17943347/111697892-89558380-880c-11eb-8d7e-d8c24b55778a.png)
