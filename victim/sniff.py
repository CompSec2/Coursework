from scapy.layers.dns import DNS
from scapy.layers.inet import IP
from scapy.sendrecv import sniff


def handler(packet):
    print("length:", len(packet))
    print("source:", packet[IP].src)
    print("destination:", packet[IP].dst)


sniff(filter="dst host 172.16.238.10 and src host 172.16.238.8 and udp ", prn=handler)
