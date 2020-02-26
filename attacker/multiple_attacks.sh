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
container=0

handler() {
    for PID in "${processes[@]}"
        do
            echo "stopping process ${PID}"
            kill ${PID}
            while kill -0 ${PID} 2> /dev/null
                do
                    wait ${PID}
                done;
        done;
    docker-compose down
    exit
}

trap handler SIGINT;

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