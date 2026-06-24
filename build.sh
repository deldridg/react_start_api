#!/usr/bin/env bash
set -e

pip install -r requirements.txt

git clone https://github.com/deldridg/react_start.git /tmp/react_start
cd /tmp/react_start
npm install
npm run build

# Copy entire React build into Django
cp -r dist/ $OLDPWD/react_build

cd $OLDPWD
python manage.py collectstatic --noinput
python manage.py migrate