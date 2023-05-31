#!/Users/monassar/opt/anaconda3/bin/python

from sys import argv 

print ("What is the vlan you would like?")

vlan_nb = int ( input() ) 

print (vlan_nb)
print (type(vlan_nb))

access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

# {} is placeholder for a variable/value
# \n is newline 

# print('\n'.join(access_template).format(5))

# ipynb is stored in JSON formt 
# py is stored in TXT format 