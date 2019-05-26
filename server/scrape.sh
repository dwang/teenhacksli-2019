#!/usr/bin/env bash

cd /home/dwang/teenhacksli-2019/server
python3 /home/dwang/teenhacksli-2019/server/app.py
rsync -a /home/dwang/teenhacksli-2019/server/articles /var/www/html
rsync /home/dwang/teenhacksli-2019/server/index.html /var/www/html
rsync /home/dwang/teenhacksli-2019/server/weather.html /var/www/html
rsync /home/dwang/teenhacksli-2019/server/news.html /var/www/html
rsync /home/dwang/teenhacksli-2019/server/firstaid.html /var/www/html

