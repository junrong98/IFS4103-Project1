from flask import Flask, request, jsonify, render_template, Response
from urllib.parse import urlparse
import subprocess
import socket
import time

app = Flask(__name__)

# Define the IP to blacklist
blacklisted_ip = '172.18.0.2'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_result')
def get_result():
    # Get the URL from the 'url' query parameter
    url = request.args.get('url')

    if not url:
        return jsonify({'error': 'URL parameter is missing'}), 400
    
    # Prepend 'http://' if no scheme is provided
    if not urlparse(url).scheme:
        url = 'http://' + url
        
    # Extract the IP address from the URL
    parsed_url = urlparse(url)
    
    if parsed_url.hostname is None:
        return f'Error occurred: Invalid URL', 500
    
    ip_address = socket.gethostbyname(parsed_url.hostname)
    
    # Blacklist filter
    if ip_address in [blacklisted_ip]:
        return jsonify({'error': 'Access to this IP address is not allowed'}), 403

    try:
        time.sleep(5)
        
        # Build the curl command
        curl_command = ['curl', '-s', url]

        # Execute the curl command
        result = subprocess.run(curl_command, capture_output=True, text=True)

        # Set Content-Type to text/plain
        headers = {'Content-Type': 'text/plain'}

        # Directly return the result.stdout without processing
        return Response(result.stdout, headers=headers)
    except Exception as e:
        # Handle any exceptions that might occur during the process
        return f'Error occurred: {str(e)}', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
