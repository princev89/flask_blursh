from flask import Flask, jsonify, request 
import blurhash
import requests

app = Flask(__name__) 

@app.route('/', methods=['POST']) 
def home(): 
    if request.method == 'POST':
        url = request.json.get('url')  # Assuming the JSON payload contains the 'url' key
        
        if url:
            img_resp = requests.get(url, stream=True)
            if img_resp.status_code == 200:
                hash = blurhash.encode(img_resp.raw, x_components=4, y_components=3)
                
            else:
                return jsonify({'error': 'Failed to fetch image from the provided URL'}), 400
        else:
            return jsonify({'error': 'No URL provided in the request payload'}), 400
        
        return jsonify({'data': hash})

# driver function 



