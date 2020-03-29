FROM sameersbn/bind:9.11.3-20190706

RUN apt-get update && apt-get upgrade -y

ADD gen-signed.sh /etc/bind/

# authoritative DNS config based off https://devops.ionos.com/tutorials/configure-authoritative-name-server-using-bind-on-ubuntu/
ADD named.conf.options /etc/bind/
ADD named.conf.local /etc/bind/
ADD db.example.com.simple /etc/bind/
# signed DNS config based off https://www.digitalocean.com/community/tutorials/how-to-setup-dnssec-on-an-authoritative-bind-dns-server--2
ADD db.example.com /etc/bind/
ADD db.example.com.signed /etc/bind/
ADD Kexample.com* /etc/bind/
