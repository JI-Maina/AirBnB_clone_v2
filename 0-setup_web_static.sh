#!/usr/bin/env bash
# sets the web servers for the deployment of web_static app

# install Nginx
sudo apt update -y
sudo apt install nginx -y
sudo ufw allow 'Nginx HTTP'

# create folders
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "Airbnb Clone v2" > /data/web_static/releases/test/index.html

# Delete and create symbolik link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of /data/ to ubuntu and group
sudo chown -R ubuntu:ubuntu /data/

printf %s "server {
	location /hbnb_static {
		alias /data/web_static/current/;
		index index.html index.htm;
	}
}" > /etc/nginx/sites-available/default

sudo service nginx restart
