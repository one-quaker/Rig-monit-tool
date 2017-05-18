import urllib.request
import json
import re
import sys
from pprint import pprint
import argparse


parser = argparse.ArgumentParser(description='Rig monitoring')

parser.add_argument('-s', '--server-list', type=str, nargs='+', required=True, help='For example: -s SERVER_IP_OR_NAME:PORT 192.168.0.10:3333 rig01.local:3334 rig01.myname.com:3333')
parser.add_argument('-t', '--target-hashrate', type=int, nargs='+', help='For example: -t 170 42 86')
parser.add_argument('-m', '--minimal', action='store_true', default=False, help='Minimal output')
parser.add_argument('-D', '--debug', action='store_true', default=False, help='Debug mode')

args = parser.parse_args()

if args.debug:
    print(args.server_list)

res = []


for i in args.server_list:
    host, port = i.split(':')

    with urllib.request.urlopen('http://{}:{}'.format(host, port)) as f:
        data = f.read()

        regex = b"\{\"result\"\:\s(?P<data>\[.*\])\}"
        matches = re.finditer(regex, data, re.MULTILINE)

        for matchNum, match in enumerate(matches):
            val = match.group(matchNum).decode('utf-8')
            res.append(json.loads(val).get('result'))


s = 'Pool: {pool}\nWork time: {uptime_human:.2f} hours\nCoin: {coin}\nTotal hashrate: {hash_total} Mh/s\nServer speed: {share_per_min:.2f} (shares in 1 minute)\nGood shares: {good_share}\nBad shares: {bad_share}\nMiner version: {ver}\n{gpu_stat}\n{hash_total_alarm}'
if args.minimal:
    s = 'Pool: {pool}\nWork time: {uptime_human:.2f} hours\nTotal hashrate: {hash_total} Mh/s\nServer speed: {share_per_min:.2f} (shares in 1 minute)\nBad shares: {bad_share}\n{hash_total_alarm}'

s += 40 * '=' + '\n'


for rid, i in enumerate(res):
    uptime = int(i[1])
    hashrate_total = float(i[2].split(';')[0]) / 1000
    good_count = int(i[2].split(';')[1])

    d = dict(
        pool=i[-2],
        coin=i[0].split()[-1],
        ver=i[0].split()[0],
        uptime=uptime,
        uptime_human=float(i[1]) / 60,
        hash_total_alarm='',
        hash_total=hashrate_total,
        good_share=good_count,
        bad_share=int(i[2].split(';')[2]),
        share_per_min=good_count / uptime,
        gpu=dict(),
    )

    if hashrate_total < args.target_hashrate[rid]:
        d['hash_total_alarm'] = '[ALARM] Current hashrate is {} and less than {} !!!!!!!!!\n'.format(hashrate_total, args.target_hashrate[rid])


    gpu_key = 'gpu{:02d}'
    for idx, v in enumerate(i[3].split(';')):
        d['gpu'][gpu_key.format(idx)] = dict(hashrate=v, hashrate_human=round(float(v) / 1000, 2))


    gpu_temp = []
    gpu_fan = []
    for idx, v in enumerate(i[6].split(';')):
        if ((idx + 1) % 2) == 0:
            gpu_fan.append(v)
        else:
            gpu_temp.append(v)

    for idx, v in enumerate(zip(gpu_temp, gpu_fan)):
        d['gpu'][gpu_key.format(idx)]['temp'] = v[0]
        d['gpu'][gpu_key.format(idx)]['fan'] = v[1]


    gpu_stat = []
    for k, v in d.get('gpu').items():
        gpu_stat.append('{}: {hashrate_human} Mh/s, {temp}C, {fan}%'.format(k.replace('gpu', 'GPU_'), **v))
    d['gpu_stat'] = '\n'.join(sorted(gpu_stat))

    if args.debug:
        print(i)
        pprint(d)

    print(s.format(**d))
