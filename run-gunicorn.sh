#!/usr/bin/bash
cd /home/ec2-user/rpl/back/pbmps-api
/home/ec2-user/rpl/back/pbmps-api/bin/gunicorn --workers 3 --bind 0.0.0.0:4000 -m 007 wsgi:app
