import scapy.all as scapy
import time

print("[arp-capture] Starting arp-capture tool... please wait")
time.sleep(3)
ip_range_request = input("[address] arp-request(default: 192.168.0.1/24): ")
print("[+] [request] Sending arp-request to capture the response data")
time.sleep(2)
arp_response = scapy.arping(ip_range_request)
print("\n[+] [finished] Arp-capture finished you can close this program")
while True:
	time.sleep(9)
