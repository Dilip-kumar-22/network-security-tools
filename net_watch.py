import socket
import threading
from queue import Queue
from datetime import datetime
from colorama import Fore, Style, init

# Initialize Colorama for cool terminal colors
init(autoreset=True)

# --- CONFIGURATION ---
TARGET = "127.0.0.1" # Default to localhost for safety. Change to scan other IPs.
START_PORT = 1
END_PORT = 1024 # Standard system ports
THREADS = 100 # Speed of the scan

# Thread-safe queue
q = Queue()
open_ports = []

def port_scan(port):
    """
    Tries to connect to a port. If successful, grabs the banner.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) # 1 second timeout
        result = s.connect_ex((TARGET, port))
        
        if result == 0:
            # Port is Open! Try to grab banner
            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = "Unknown Service"
            
            with print_lock:
                print(f"{Fore.GREEN}[+] Port {port} is OPEN: {Style.BRIGHT}{banner}")
            open_ports.append(port)
        s.close()
    except:
        pass

def threader():
    """
    Worker thread that pulls ports from the queue.
    """
    while True:
        worker = q.get()
        port_scan(worker)
        q.task_done()

print_lock = threading.Lock()

def main():
    global TARGET
    print(f"{Fore.CYAN}--- NET-WATCH: TACTICAL PORT SCANNER ---")
    user_target = input(f"Enter Target IP (Default {TARGET}): ")
    
    if user_target:
        TARGET = user_target
    
    # Resolve domain to IP if needed
    try:
        target_ip = socket.gethostbyname(TARGET)
    except socket.gaierror:
        print(f"{Fore.RED}[!] Hostname could not be resolved.")
        return

    print(f"{Fore.YELLOW}[*] Scanning Target: {target_ip}")
    print(f"{Fore.YELLOW}[*] Scanning Ports: {START_PORT} - {END_PORT}")
    print(f"{Fore.YELLOW}[*] Threads: {THREADS}")
    print("-" * 50)
    
    start_time = datetime.now()

    # Spawn Threads
    for _ in range(THREADS):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    # Fill Queue
    for worker in range(START_PORT, END_PORT + 1):
        q.put(worker)

    # Wait for completion
    q.join()

    duration = datetime.now() - start_time
    print("-" * 50)
    print(f"{Fore.CYAN}[*] Scan Completed in: {duration}")
    print(f"{Fore.GREEN}[*] Open Ports Found: {open_ports}")

if __name__ == "__main__":
    main()
