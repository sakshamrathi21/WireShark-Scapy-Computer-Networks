from scapy.all import *

def send_dns_any_query(dns_server, domain):
    dns_query = IP(dst=dns_server)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=domain, qtype=255)) # qtype=255 for ANY query
    response = sr1(dns_query, timeout=2) # Send the DNS query and wait for a response

    if response:
        print(f"Received DNS response from {dns_server}:")
        print(response.summary())
        response.show()
    else:
        print(f"No response received from {dns_server}.")

if __name__ == "__main__":
    dns_server = input("Enter the DNS server IP address (e.g., 8.8.8.8): ") # Requesting for the DNS server IP from the user
    domain = input("Enter the domain name to query (e.g., example.com): ") # Requesting for the domain name from the user
    
    send_dns_any_query(dns_server, domain)  # Send the DNS query to the specified DNS server and domain name
