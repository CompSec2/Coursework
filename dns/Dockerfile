FROM sameersbn/bind:9.11.3-20190706

# authoritative DNS config based off https://devops.ionos.com/tutorials/configure-authoritative-name-server-using-bind-on-ubuntu/
ADD named.conf.options /etc/bind/
ADD named.conf.local /etc/bind/
ADD db.example.com /etc/bind/
