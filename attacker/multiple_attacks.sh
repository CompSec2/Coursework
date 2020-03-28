#!/usr/bin/env bash

argv="$@"
ips=${argv:6}

processes=()
attack() {
    docker exec -t coursework_attacker_${1} sh -c "python attack.py ${2} ${3} ${4}"
}

attackers=$((${#} - 2))
docker-compose up -d --scale attacker=${attackers};

handler() {
    container=0
    for PID in "${processes[@]}"
        do
            container=$(( $container + 1 ))
            echo
            echo "stopping attack script inside container"
            docker exec -t coursework_attacker_${container} bash -c "ps -a| grep python | head -n 1| tr -s ' '|cut -d' ' -f2| xargs kill -s 2"
        done;
    exit 1
}

trap handler SIGINT;

echo "starting attack against coursework_victim_${1}"

container=0
for i in ${ips}
do
    container=$(( $container + 1 ))
    echo "starting attack from coursework_attacker_${container}"
    attack ${container} ${1} ${2} ${i} &
    processes+=("${!}")
done;


while true
do
    sleep 1
done;
