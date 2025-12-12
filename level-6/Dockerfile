FROM alpine:3.8

# Install build dependencies and nginx
RUN apk add --no-cache \
    nginx \
    php5 \
    php5-fpm \
    php5-json \
    php5-openssl \
    php5-ctype

# Create necessary directories
RUN mkdir -p /var/www/html /run/nginx /var/log/php5

# Copy application files
COPY src/ /var/www/html/

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Configure PHP-FPM
RUN sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php5/php.ini && \
    sed -i 's/display_errors = Off/display_errors = Off/g' /etc/php5/php.ini

# Set proper permissions
RUN chown -R nginx:nginx /var/www/html && \
    chmod -R 755 /var/www/html

# Expose port 80
EXPOSE 80

# Start both PHP-FPM and Nginx
CMD php-fpm5 && nginx -g 'daemon off;'
