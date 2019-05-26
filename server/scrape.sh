#!/usr/bin/env bash

cd /home/dwang/teenhacksli-2019/server
python3 /home/dwang/teenhacksli-2019/server/app.py
mkdir -p articles
rsync -a articles /var/www/html
rsync index.html /var/www/html
rsync weather.html /var/www/html
rsync news.html /var/www/html
rsync firstaid.html /var/www/html

