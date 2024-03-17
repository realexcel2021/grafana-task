FROM php:7.4-apache

WORKDIR /app

COPY . /app/

RUN sed -i 's/index.html/index.php/g' /etc/httpd/conf/httpd.conf

RUN sudo sed -i 's/<db endpoint>/localhost/g' /var/www/html/index.php

EXPOSE 80

CMD ["apache2-foreground"]
