network_services = [
"192.168.1.1", 20, "SSH"
"192.168.1.1", 80, "HTTP"
"192.168.1.1", 50, "HTTPS"
]
 
for ip, port, portocol in network_services:
 print(f"Protocal {protocol} at {ip}:{port}")
