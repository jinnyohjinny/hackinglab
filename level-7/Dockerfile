FROM php:7.0-fpm-alpine

RUN apk add --no-cache nginx

COPY src/ /var/www/html/
COPY nginx.conf /etc/nginx/nginx.conf

RUN chown -R nginx:nginx /var/www/html && \
    chmod -R 755 /var/www/html

RUN mkdir -p /run/nginx && \
    chown -R nginx:nginx /run/nginx

EXPOSE 80

CMD php-fpm -D && nginx -g 'daemon off;'
