#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

# 1- update and install nginx if not exist
sudo su
apt - get update
apt - get - y install nginx

# 2- make this dir note that: -p :if the parent dir not exist make it also
mkdir - p / data / web_static / releases / test/
mkdir - p / data / web_static / shared/

# 3- write this html un the file
echo '< html >
<head >
< / head >
<body >
Holberton School
< / body >
< / html >' > / data / web_static / releases / test / index.html


# Create a symbolic link /data/web_static/current linked to the...
# .../data/web_static/releases/test/ folder. If the symbolic link already...
# ...exists, it should be deleted and recreated every time the script is ran.
ln - sf / data / web_static / releases / test / /data / web_static / current


# Give ownership of the /data/ folder to the ubuntu user AND group (you can
# assume this user and group exist). This should be recursive; everything
# inside should be created/owned by this user/group.
chown - hR ubuntu: ubuntu / data/

# to add /bbnb_static to the configrationfile of nginx (make sure to check
# the file by yourself )
sed - i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' / etc / nginx / sites - available / default

sudo service nginx restart
