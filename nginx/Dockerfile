FROM nginx:latest

# Copy your nginx.conf file from the nginx directory to the correct location
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

# Copy your frontend files to the Nginx default directory
COPY frontend /usr/share/nginx/html

