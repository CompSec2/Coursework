from scapy.layers.dns import DNS
from scapy.layers.inet import IP
from scapy.sendrecv import sniff


def handler(packet):
    print("length:", len(packet))
    print("source:", packet[IP].src)
    print("destination:", packet[IP].dst)
    print("packet:")
    packet[DNS].show()


sniff(filter="udp port 53", prn=handler)
