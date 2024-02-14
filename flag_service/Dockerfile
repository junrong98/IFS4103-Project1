# Use a base image suitable for your flag service (e.g., Python)
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the necessary files to the container
COPY flag_service.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the flag service is running
EXPOSE 5000

# Command to run the flag service
CMD ["python", "flag_service.py"]