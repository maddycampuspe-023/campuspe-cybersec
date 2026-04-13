import socket
import time

def scan_port(ip,port):
    sock  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((ip, port))
    sock.close()

    return result == 0

if __name__ == "__main__":
    print("network scanner ")
    
    target= input("enter target ip :")
    ports_input = input("enter ports (comma seperated):")
    ports = [int(p.strip()) for p in ports_input.split(",")]

    start_time = time.time()

    with open("scan_results.txt","w") as file : 
        file.write(f"scan results for { target }\n")
        
        for port in ports:
            status = "OPEN" if scan_port(target, port) else "CLOSED"
            print(f"port {port}:{status}")
            file.write(f"Port{port}:{status}\n")

    end_time = time.time()

    print("scan completed.")
    print(f"Time taken : {end_time - start_time:.2f} seconds")            