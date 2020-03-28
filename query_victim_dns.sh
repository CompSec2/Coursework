#!/bin/bash
docker exec -t coursework_victim_web  /bin/bash -c "time nslookup example.com 172.16.238.101"
