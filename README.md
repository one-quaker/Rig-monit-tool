Rig monitoring tool
===================

CLI interface for claymore's dual miner 9.x
Tested on claymore 9.3

Usage instructions
==================
Linux users:
* just run `python3 monit_cli.py --help` to see options

Mac users:
* install [brew](https://brew.sh/)
* install python `brew install python3`
* run `python3 monit_cli.py --help`

Windows users:
* download and install latest stable version of [python 3](https://www.python.org/downloads/windows/)
* press Win+R, type `cmd`, press ENTER key
* run `python3 C:\PATH_TO_REPO_FOLDER\monit_cli.py --help`

Example (full report):
======================

`python3 monit_cli.py -s 192.168.1.30:3333 192.168.1.31:3333 rig01.myname.local:3333 -t 21 58 150`

```
#output

Pool: musicoin.miningclub.info:8558
Work time: 5.03 hours
Coin: ETH
Total hashrate: 21.116 Mh/s
Server speed: 0.62 (shares in 1 minute)
Good shares: 188
Bad shares: 0
Miner version: 9.3
GPU_00: 21.12 Mh/s, 63C, 36%
========================================

Pool: eth-eu1.nanopool.org:9999
Work time: 5.03 hours
Coin: ETH
Total hashrate: 58.272 Mh/s
Server speed: 0.90 (shares in 1 minute)
Good shares: 273
Bad shares: 0
Miner version: 9.3
GPU_00: 29.13 Mh/s, 58C, 52%
GPU_01: 29.14 Mh/s, 56C, 52%
========================================

Pool: eth-eu1.nanopool.org:9999
Work time: 4.28 hours
Coin: ETH
Total hashrate: 144.951 Mh/s
Server speed: 2.13 (shares in 1 minute)
Good shares: 548
Bad shares: 0
Miner version: 9.3
GPU_00: 29.82 Mh/s, 51C, 54%
GPU_01: 25.38 Mh/s, 58C, 54%
GPU_02: 30.68 Mh/s, 61C, 66%
GPU_03: 29.53 Mh/s, 63C, 66%
GPU_04: 29.55 Mh/s, 59C, 54%
[ALARM] Current hashrate is 144.951 and less than 150 !!!!!!!!!
========================================
```

Example (minimal report):
=========================

`python3 monit_cli.py -s 192.168.1.30:3333 192.168.1.31:3333 rig01.myname.local:3333 -t 21 60 150 -m`

```
#output

Pool: musicoin.miningclub.info:8558
Work time: 5.08 hours
Total hashrate: 21.1 Mh/s
Server speed: 0.62 (shares in 1 minute)
Bad shares: 0
========================================

Pool: eth-eu1.nanopool.org:9999
Work time: 5.08 hours
Total hashrate: 58.274 Mh/s
Server speed: 0.91 (shares in 1 minute)
Bad shares: 0
[ALARM] Current hashrate is 58.274 and less than 60 !!!!!!!!!
========================================

Pool: eth-eu1.nanopool.org:9999
Work time: 4.33 hours
Total hashrate: 144.953 Mh/s
Server speed: 2.13 (shares in 1 minute)
Bad shares: 0
[ALARM] Current hashrate is 144.953 and less than 150 !!!!!!!!!
========================================
```

If this code helps you, please support me
=========================================

* BTC `1PMKwrtsWfxrj1Z3kcF9oh7r4UsqRF2Ucx`
* ETH `0x9acca04d389f7858fd821e5430e6bdd3a9511d5e`
* ZEC `t1PdiwD6AHpBGkFHNAxeBxxPCv58j8FTy6o`
