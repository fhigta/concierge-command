from flask import Flask, send_file, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def dashboard():
    return send_file('dashboard.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
