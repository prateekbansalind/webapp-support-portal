# Use the official Nginx image as a base
FROM nginx:alpine

# Set the working directory
WORKDIR /app

# Install Python, pip, and other dependencies
RUN apk add --no-cache python3 py3-pip && pip3 install --upgrade pip

# Copy the Flask application
COPY . /app

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Remove the default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy the Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/

# Expose port 80 for Nginx
EXPOSE 81

# Start Gunicorn and Nginx
CMD ["sh", "-c", "gunicorn app:app -b 127.0.0.1:8000 & exec nginx -g 'daemon off;'"]
