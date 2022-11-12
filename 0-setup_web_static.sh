#!/usr/bin/env bash
# Set up web servers for depoyment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
echo "Hello World" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s -f "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
