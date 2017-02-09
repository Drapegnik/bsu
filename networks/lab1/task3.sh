#!/usr/bin/env bash
echo '## 3. `ping`'
bash ping.sh 10.150.1.5
bash ping.sh 10.150.1.1
bash ping.sh 10.0.0.20
bash ping.sh 10.150.6.29
bash ping.sh 10.150.3.30
bash ping.sh ya.ru
bash ping.sh yandex.ru
bash ping.sh tut.by
bash ping.sh onliner.by '-c 19 -s 1000'
bash ping.sh localhost