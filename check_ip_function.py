import ipaddress
def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as err:
        return False

ip1 = '10.1.1.1'
ip2 = '10.1.1' # not valid ip 

if __name__ == "__main__": # does not run if you import the module
    print('Checking IP...')
    print(ip1, check_ip(ip1))
    print(ip2, check_ip(ip2))