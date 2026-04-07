from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/weather/<latitude>/<longitude>')
def get_weather(latitude, longitude):
    response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation_sum')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)