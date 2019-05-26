#!/usr/bin/env bash

python3 /home/dwang/teenhacksli-2019/server/app.py
rsync -a articles/ /var/www/html/articles/
rsync index.html /var/www/html
