#!/bin/bash

# Install required packages
sudo apt update
sudo apt install -y nginx

# Configure Nginx
sudo tee /etc/nginx/sites-available/portfolio << EOF
server {
    listen 80;
    server_name iamsagarsharma.com www.iamsagarsharma.com;
    root /var/www/portfolio;
    index index.html;

    location / {
        try_files \$uri \$uri/ =404;
    }
}
EOF

# Create symbolic link
sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default

# Create directory for the website
sudo mkdir -p /var/www/portfolio

# Copy website files
sudo cp -r index.html blog.html styles.css /var/www/portfolio/

# Set proper permissions
sudo chown -R www-data:www-data /var/www/portfolio
sudo chmod -R 755 /var/www/portfolio

# Test Nginx configuration
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx
