#!/usr/bin/env bash
#installs nginx if not exists
#host webstatic

#sudo apt-get -y update

if ! command nginx -v  &> /dev/null;  then
	sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/releases/test/

sudo echo "<h1>  Nginx is Active </h1>" > /data/web_static/releases/test/index.html

sudo chown -R ubuntu:ubuntu /data

#create a symlink current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#configure nginx to serve at /data/web_static/current

sudo sed -i '/default_server;/!b;n;a\\n\   location /hbnb_static {\n\talias /data/web_static/current;\n}' /etc/nginx/sites-available/default

#Restart nginx 
sudo nginx -s reload
