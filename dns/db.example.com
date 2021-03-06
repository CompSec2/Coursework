$TTL 3H
@   IN SOA  @ example.com. (
                0   ; serial
                3H  ; refresh
                1H  ; retry
                1W  ; expire
                3H )    ; minimum
@            IN   NS     example.com.
@            IN   A      192.0.2.1
@            IN   A      192.0.2.9
@            IN   AAAA   2a00:1450:4010:c0b::8a
@            IN   MX     10 example.com.
@            IN   MX     20 example.com.
ww1          IN   CNAME  example.com.
ww2          IN   CNAME  example.com.
ww3          IN   CNAME  example.com.
ww4          IN   CNAME  example.com.
ww5          IN   CNAME  example.com.
ww6          IN   CNAME  example.com.
mail         IN   CNAME  example.com.
gopher       IN   CNAME  example.com.
example.com. IN   TXT    "v=spf1 ip4:203.0.113.42 include:_spf.google.com ~all"
$INCLUDE Kexample.com.+007+19562.key
$INCLUDE Kexample.com.+007+33843.key
