$TTL 3H
@   IN SOA  @ hostmaster.example.com. (
                0   ; serial
                3H  ; refresh
                1H  ; retry
                1W  ; expire
                3H )    ; minimum
@            IN   NS     ns1.example.com.
@            IN   NS     ns2.example.com.
@            IN   A      192.0.2.10
@            IN   MX     10 host2.example.com.
@            IN   MX     20 host3.example.com.
ns1          IN   A      192.0.2.1
ns2          IN   A      192.0.2.2
host1        IN   A      192.0.2.10
host2        IN   A      192.0.2.11
host3        IN   A      192.0.2.12
www          IN   CNAME  example.com.
mail         IN   CNAME  host2.example.com.
gopher       IN   CNAME  host3.example.com.
example.com. IN   TXT    "v=spf1 ip4:203.0.113.42 include:_spf.google.com ~all"
