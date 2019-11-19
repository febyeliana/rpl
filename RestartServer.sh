#!/usr/bin/bash
exec sudo su <<EOF
systemctl restart pbmps-api-server
systemctl restart nginx
EOF
