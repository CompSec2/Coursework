# Coursework

## Running
With docker installed:
```bash
docker-compose up --build
```

With the containers running, to run a command inside the attacker container:
```bash
docker exec coursework_attacker $command
```

To run an interactive shell:
```bash 
docker exec -it coursework_attacker /bin/sh
```

Then to run the attack script from inside the attacker just run:
```bash
python attack.py
```

To see Flask app: navigate to http://localhost:5000

To see DNS admin panel: navigate to https://localhost:10000/ and log in with `root`/`highentropy`

## TODO:
- [x] create basic Flask app
- [x] create attacker dockerfile
- [ ] figure out how to spoof IP and start attack
- [ ] make sure DNS configuration is OK, and allows for attack
- [ ] create attack script
- [ ] run Flask with WSGI to mimic a production like environment
- [ ] add Wireshark container which dumps traces onto volume connected to the host OS
- [ ] put all this in a VM