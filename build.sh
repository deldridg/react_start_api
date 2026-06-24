#!/usr/bin/env bash
set -e

# Install Python deps
pip install -r requirements.txt

# Clone React repo and build it
git clone https://github.com/deldridg/react_start.git /tmp/react_start
cd /tmp/react_start
npm install
npm run build

# Copy React build into Django
cp -r dist/ $OLDPWD/react_build

# Back to Django
cd $OLDPWD
python manage.py collectstatic --noinput
python manage.py migrate