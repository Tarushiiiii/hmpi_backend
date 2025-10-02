from flask import Flask, request, jsonify
from flask_cors import CORS
from model.calc_hmpi import calculate_hmpi
import os

app = Flask(__name__)
CORS(app)   # allow requests from React

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        hmpi_value = calculate_hmpi(data)
        return jsonify({"hmpi_value": hmpi_value})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
