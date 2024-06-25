import nmap

# Create an Nmap scanner object
scanner = nmap.PortScanner()

# Perform a scan with additional arguments
scanner.scan('127.0.0.1', arguments='-sV')

# Print scan results
for host in scanner.all_hosts():
    print('Host:', host)
    print('State:', scanner[host].state())
    for proto in scanner[host].all_protocols():
        print('Protocol:', proto)
        ports = scanner[host][proto].keys()
        for port in ports:
            print('Port:', port, 'State:', scanner[host][proto][port]['state'])
            print('Service:', scanner[host][proto][port]['name'])
            print('Version:', scanner[host][proto][port]['version'])
