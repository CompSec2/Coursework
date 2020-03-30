#!/bin/bash
docker exec -t coursework_victim_web  /bin/bash -c "tail /var/www/victim.com/logs/access.log"
