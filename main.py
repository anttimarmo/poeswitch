# Create new admin user in controller, no special permissions needed
# Define variables and controller address

username = ''
password = ''
hostname = ''

MacToLookFor = [
    'c6:a1:8e:54:56:82',  # Phone 1
    'd6:4f:f8:3d:0a:bf']  # Phone 2

SwPorts = [
    {'sw_mac': '74:ac:b9:41:45:0a', 'port_idx': 5}
]

from pyunifi.controller import Controller

Poe = ''
c = Controller(hostname, username, password, ssl_verify=False)

for client in c.get_clients():
    if client['mac'] in MacToLookFor:
        print('Found %s in list of clients, setting Poe = Off' % (client['mac'], ))
        Poe = 'Off'

if Poe == 'Off':
    for sw in SwPorts:
        print('Setting port %s off on switch %s' % (sw['port_idx'], sw['sw_mac']))
        c.switch_port_power_off(sw['sw_mac'], sw['port_idx'])
else:
    for sw in SwPorts:
        print('Setting port %s on on switch %s' % (sw['port_idx'], sw['sw_mac']))
        c.switch_port_power_on(sw['sw_mac'], sw['port_idx'])
