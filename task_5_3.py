
access_template = [
"switchport mode access", 
"switchport access vlan {}",
"switchport nonegotiate", 
"spanning-tree portfast",
"spanning-tree bpduguard enable"
]
trunk_template = [
"switchport trunk encapsulation dot1q", "switchport mode trunk",
"switchport trunk allowed vlan {}"
]

print ("Enter the interface mode: ")
mode = input()

print("Enter the interface type and number: ")
interface = input() 

if (mode == "access"): 
    print("Enter VLAN number: ")
else: 
    print("Enter the allowed VLANs")

vlan = input()

print ("-"*15)

if (mode == "access"): 
    print ("interface {}".format(interface))
    print ("\n".join(access_template).format(vlan))
elif (mode =="trunk"): 
    print ("interface {}".format(interface))
    print ("\n".join(trunk_template).format(vlan))

