from scapy.all import *
import datetime


# Function to process captured packets
def packet_callback(packet):
    # Get the timestamp of the packet
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Print packet summary with timestamp
    print(f"\n[{timestamp}] Packet Captured")

    # Check if it's an IP packet
    if IP in packet:
        ip_src = packet[IP].src  # Source IP
        ip_dst = packet[IP].dst  # Destination IP
        protocol = packet[IP].proto  # Protocol

        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {protocol}")

        # Check for TCP/UDP payload
        if TCP in packet:
            print("Protocol: TCP")
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")
            print(f"TCP Payload: {packet[TCP].payload}")
        elif UDP in packet:
            print("Protocol: UDP")
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")
            print(f"UDP Payload: {packet[UDP].payload}")
        else:
            print("Other Protocol")
    else:
        print("Non-IP Packet")


# Function to start sniffing packets
def start_sniffing(interface):
    print(f"[*] Starting packet sniffing on {interface}...")
    # Sniff packets and call packet_callback for each packet
    sniff(iface=interface, prn=packet_callback, store=0)


# Main program
if _name_ == "_main_":
    # Define the network interface (e.g., eth0, wlan0, etc.)
    interface = input("Enter the network interface to sniff on (e.g., eth0, wlan0): ")
    start_sniffing(interface)
