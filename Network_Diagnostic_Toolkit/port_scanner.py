import socket

def scan_ports(host):
    for port in range(20, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
