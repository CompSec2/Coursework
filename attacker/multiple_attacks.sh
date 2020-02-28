#!/usr/bin/env bash
#docker-compose up --scale attacker=5; # argument
#
#for each attacker give a dns ip
# docker exec -ti coursework_attacker sh -c "python attack.py 4 8"

argv="$@"
ips=${argv:2}

processes=()
attack() {
    docker exec -t coursework_attacker_${1} sh -c "python attack.py ${2} ${3}"
}

attackers=$((${#} - 1))
docker-compose up -d --scale attacker=${attackers};

handler() {
    container=0
    for PID in "${processes[@]}"
        do
            container=$(( $container + 1 ))
            echo
            echo "stopping attack script inside container"
            docker exec -t coursework_attacker_${container} sh -c "ps | grep python | head -n 1| tr -s ' '|cut -d' ' -f2| xargs kill -s SIGINT"
            while kill -0 ${!} 2> /dev/null
                do
                    wait ${!}
                done;
        done;
    docker-compose down
    exit 1
}

trap handler SIGINT;

container=0
for i in ${ips}
do
    container=$(( $container + 1 ))
    echo "starting attack on coursework_attacker_${container}"
    attack ${container} ${1} ${i} &
    processes+=("${!}")
done;


while true
do
    sleep 1
done;