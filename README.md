# phukienanphu2023

## chuẩn bị

```
sudo apt update && sudo apt upgrade -y
sudo apt install python3.10-venv -y
sudo apt install nginx -y
```

## cài đặt db
```
sudo apt install mariadb-server -y

sudo mariadb
CREATE USER 'sieunhan'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'sieunhan'@'%' WITH GRANT OPTION;

CREATE DATABASE ongnuoc;
exit;
```

## clone project và bật venv
quen
```
sudo apt install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
sudo apt install libmysqlclient-dev
sudo apt install python3-dev libmysqlclient-dev gcc
sudo apt install pkg-config

pip3 install mysqlclient
pip3 install -r requirements.txt
pip3 install python-environ
```
if open-cv
```
pip3 install opencv-python-headless 

```

## cài đặt gunicorn bên trong project
```
pip install gunicorn
gunicorn --bind 0.0.0.0:8000 app.wsgi:application
```


## cấu hình nginx
```
cd /etc/nginx/sites-available/
sudo touch project
sudo vim project
```

```
server {
    listen 80;
    server_name my_domain;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /var/www/static/;
        autoindex on;
    }
}
```


```
sudo ln -s /etc/nginx/sites-available/project /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```


## di chuyển đến project và chạy thử
```
cd /project
gunicorn --bind 0.0.0.0:8000 app.wsgi:application --workers 4
```
kiểm tra địa chỉ ip

## cấu hình supervisor
cài đặt vào tạo một tệp cho dự án
```
sudo apt install supervisor
sudo touch /etc/supervisor/conf.d/project.conf
sudo vim /etc/supervisor/conf.d/project.conf
```

nội dung tệp
```
[program:project]
directory=/home/ubuntu/project
command=/home/ubuntu/project/env3/bin/gunicorn --bind 0.0.0.0:8000 app.wsgi:application --workers 4
user=ubuntu
autostart=true
autorestart=true
redirect_stderr=true
```

khởi động lại
```
sudo supervisorctl reread
sudo supervisorctl update
```

```
sudo systemctl restart supervisor
sudo supervisorctl status project
```

## collectsatic
```
python manage.py collectstatic
sudo cp -r /home/ubuntu/project/staticfiles /var/www/static
```

## cú pháp backup
```
scp -i keyname.pem ubuntu@ec2_ip:path/to/file.sql ./bk
```
