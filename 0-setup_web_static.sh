#!/usr/bin/env bash
#installs nginx if not exists
#host webstatic


if ! command nginx -v  &> /dev/null;  then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi
#setup init files
echo 'Holberton School' > /var/www/html/index.html
echo "Ceci n'est pas une page" > /var/www/html/404.html

#sed -i '/server_name _/a location /redirect_me { rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlw\u4? permanent; }' /etc/nginx/sites-available/default
#sed -i '/server_name _/a error_page 404 /404.html; location = /404.html {root /var/www/error/; internal; }' /etc/nginx/sites-available/default

sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/nginx.conf


#sets up deployment for webstatic
sudo mkdir -p /data/web_static/releases/test/

sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo chown -R ubuntu:ubuntu /data/

#create a symlink current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#configure nginx to serve at /data/web_static/current

sudo sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}" /etc/nginx/sites-available/default

#Restart nginx 
sudo nginx -s reload
