### Bot gaianet
### Syarat
* install npm python dan pm2
### Install
```
git clone https://github.com/Dwentzart/boted.git bot
```
```
cd bot
```
### Runing random.py
```
python3 random.py
```
### Beri akses
```
chmod +x run.sh
```
### Happy
```
for i in {1..50}; do pm2 start run.sh --name "gaia-chat-$i" --interpreter bash; done
```
### Log
* log
```
pm2 logs
```
* hapus
```
pm2 delete all
```
