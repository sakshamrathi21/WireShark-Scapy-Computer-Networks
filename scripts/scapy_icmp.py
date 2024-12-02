from scapy.all import *

def send_icmp_request(target_ip, message):
    icmp_request = IP(dst=target_ip)/ICMP()/message # Create an ICMP packet with the specified message
    response = sr1(icmp_request, timeout=2) # Send the ICMP packet and wait for a response

    if response:
        print(f"Received ICMP Echo Reply from {target_ip}:")
        print(response.summary())
    else:
        print(f"No response received from {target_ip}.")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ") # Requesting for the target IP from the user
    message = input("Enter a custom message to include in the ICMP packet: ") # Requesting for a custom message from the user
    send_icmp_request(target_ip, message) # Send the ICMP packet to the specified target IP with the custom message
