from scapy.sendrecv import sniff


def handler(packet):
    print(len(packet))
    print([0])


sniff(filter="udp port 53", prn=handler)
