# Use a base image suitable for your web application (e.g., Python)
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the necessary files to the container
COPY web_app.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create the 'templates' directory and copy individual files
COPY templates /app/templates

# Expose the port on which the web application is running
EXPOSE 80

# Command to run the web application
CMD ["python", "web_app.py"]
