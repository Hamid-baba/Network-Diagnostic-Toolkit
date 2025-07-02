from ping_test import ping
from port_scanner import scan_ports

def main():
    print("1. Ping Test")
    print("2. Port Scan")
    choice = input("Select tool: ")
    if choice == "1":
        ping("8.8.8.8")
    elif choice == "2":
        scan_ports("localhost")

if __name__ == "__main__":
    main()
