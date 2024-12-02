from scapy.all import *

def send_spoofed_syn(target_ip, spoofed_ip, target_port):
    ip_layer = IP(src=spoofed_ip, dst=target_ip)
    tcp_layer = TCP(dport=target_port, flags="S")
    packet = ip_layer/tcp_layer
    send(packet)
    print(f"Sent spoofed TCP SYN packet from {spoofed_ip} to {target_ip}:{target_port}")

if __name__ == "__main__":
    target_ip_addr = input("Enter the target IP address: ") # requesting for target IP from the user
    spoofed_ip = input("Enter the spoofed source IP address: ") # requesting for spoofed IP from the user
    target_port = int(input("Enter the target port (e.g., 80 for HTTP): ")) # requesting for target port from the user
    
    send_spoofed_syn(target_ip_addr, spoofed_ip, target_port)
