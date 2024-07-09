import socket
from datetime import datetime

# Define the target
target = input("Enter the host to be scanned: ")
# Convert hostname to IPv4
target_ip = socket.gethostbyname(target)

# Print a nice banner
print("-" * 60)
print("Scanning Target: " + target_ip)
print("Scanning started at: " + str(datetime.now()))
print("-" * 60)

try:
    # Will scan ports between 1 and 1024
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # Returns an error indicator
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port}: Open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program !!!!")
    exit()
except socket.gaierror:
    print("\nHostname Could Not Be Resolved !!!!")
    exit()
except socket.error:
    print("\nServer not responding !!!!")
    exit()

print("Scanning completed at: " + str(datetime.now()))
