from flask import Flask, request
import requests

app = Flask(__name__)

# Define the endpoints and hook URLs in an array
endpoints = [
    {"name": "nightwatch-brocure", "url": "https://nightwatch.app.n8n.cloud/webhook/c8d3c9b4-d3be-47b8-ba71-c86e652a1ff5", "method": "POST"},
    {"name": "endpoint2", "url": "https://hook2.com", "method": "GET"},
    {"name": "endpoint3", "url": "https://hook3.com", "method": "POST"},
]

# Define the route to handle incoming requests
@app.route('/', methods=['POST', 'GET'])
def forward_request():
    # Check if the request matches one of the defined endpoints
    for endpoint in endpoints:
        if request.path == f'/{endpoint["name"]}' and request.method == endpoint["method"]:
            # Forward the request to the designated hook URL
            res = requests.request(endpoint["method"], endpoint["url"], data=request.data, headers=request.headers)
            return res.content, res.status_code
    
    # If the request doesn't match any of the defined endpoints, return a 404 error
    return 'Endpoint not found', 404

if __name__ == '__main__':
    app.run(debug=True)
