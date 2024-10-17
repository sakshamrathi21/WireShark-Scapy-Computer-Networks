# CS378-2024 Lab 6: Wireshark & Scapy

## Overview

This repository contains solutions for **Lab 6** of the **CS378-2024** course. In this lab, we explore network traffic analysis and manipulation using **Wireshark**, a packet analyzer, and **Scapy**, a Python-based packet manipulation tool. The lab consists of five parts that involve investigating traffic captures, understanding basic authentication, decrypting TLS traffic, capturing our own network traffic, and using Scapy for crafting custom packets.

## Contents

The repository is structured as follows:

- `report.pdf`: Detailed answers to the questions asked in various parts of the lab.
- `my_http_capture.pcap`: Packet capture of HTTP traffic from Part 4.
- `my_udp_capture.pcap`: Packet capture of UDP traffic from Part 4.
- `scapy_icmp.py`: Python script using Scapy to send an ICMP Echo Request and capture the Echo Reply.
- `scapy_dns_ns.py`: Python script using Scapy to send a DNS query with a non-standard DNS record type.
- `scapy_ip_spoof.py`: Python script using Scapy to send a TCP SYN packet with a spoofed source IP.

## Lab Breakdown

### Part 1: Investigating HTTP Traffic with Wireshark
We used Wireshark to open a `.pcap` file and analyze HTTP packets. Key findings include:

- **HTTP versions** of the client and server.
- **IP addresses** of the client and server.
- **Status code** returned by the server and metadata about the retrieved HTML file.

### Part 2: Basic Authentication over HTTP
Analyzed HTTP Basic Authentication using Wireshark:

- **Status codes** and reasons for initial request failures.
- The success of subsequent requests due to the inclusion of an **Authorization** header.
- **Username** and **password** extracted from packet captures.

### Part 3: Analyzing and Decrypting TLS Traffic
Used Wireshark and a pre-master key to decrypt TLS traffic:

- Common **cipher suite** used.
- **Protocol** of communication.
- **Master key** for the session.

### Part 4: Capturing Your Own Traffic
Captured network traffic on the loopback interface using Wireshark and my own HTTP and UDP traffic:

- **HTTP traffic** capture shows the last modification time of a webpage.
- **UDP traffic** capture shows data sent using custom socket programs.

### Part 5: Packet Manipulation with Scapy
Used Scapy to craft and send various network packets:

1. **ICMP Echo Request**: Sent a ping and captured the Echo Reply.
   - Script: `scapy_icmp.py`
2. **DNS Query**: Sent a DNS query with a non-standard record type.
   - Script: `scapy_dns_ns.py`
3. **TCP SYN with Spoofed IP**: Sent a TCP SYN packet with a spoofed source IP.
   - Script: `scapy_ip_spoof.py`

Each task was verified by capturing the generated packets in Wireshark.

