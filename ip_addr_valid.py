import sys
import ipaddress


# Checking IP address validity
def ip_addr_valid(ip_list):

    for ip in ip_list:
        try:
            ipa = ipaddress.ip_address(ip)  # return a <class 'ipaddress.IPv4Address'> object
        except ValueError as e:  # A ValueError is raised if address does not represent a valid IPv4 or IPv6 address.
            print(e)
        else:
            if ipa.is_multicast:  # IP addresses belonging to class D are multicast addresses.
                print(f"\n* There was an multicast IP address in the file: {ip}")
                sys.exit()
            elif ipa.is_loopback:  # The IP address range 127.0.0.0 – 127.255.255.255 is reserved for loopback.
                print(f"\n* There was an loopback IP address in the file: {ip}")
                sys.exit()
            elif ipa.is_reserved:  # IP addresses belonging to class E are reserved for experimental and research
                # purposes.
                print(f"\n* There was an reserved IP address in the file: {ip}")
                sys.exit()
            elif ipa.is_link_local:  # The IP address range 169.254.0.0 - 169.254.255.255 is reserved for link-local.
                print(f"\n* There was an link-local IP address in the file: {ip}")
                sys.exit()
            else:
                continue
