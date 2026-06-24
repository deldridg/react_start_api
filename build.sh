#!/usr/bin/env bash
set -e

# Install Python dependencies
pip install -r requirements.txt

# Build React - assumes react_start is a sibling directory to react_start_api
cd ../react_start
npm install
npm run build

# Copy React build into Django
cp -r build ../react_start_api/react_build

# Back to Django
cd ../react_start_api
python manage.py collectstatic --noinput
python manage.py migrate