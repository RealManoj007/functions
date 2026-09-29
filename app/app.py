from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """GET endpoint for root path"""
    app.logger.info("Homepage endpoint invoked");
    return jsonify({
        'message': 'Welcome to the Cloud with varjosh',
        'platform':"Github Actions",
        'status': 'success'
    }), 200

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    app.logger.info("Health check endpoint invoked");
    return jsonify({
        'status': 'healthy',
        'message': 'API is running'
    }), 200

if __name__ == '__main__':
    app.logger.info("Starting Flask application");
    app.run(
      host="0.0.0.0",
      port=int(os.getenv("PORT",5000))
    )
