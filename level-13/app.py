from flask import Flask, request, render_template, jsonify
import os
import time
from collections import defaultdict
from datetime import datetime, timedelta

app = Flask(__name__)

rate_limit_store = defaultdict(list)
RATE_LIMIT = 10
RATE_WINDOW = 60

def check_rate_limit(ip):
    now = time.time()
    rate_limit_store[ip] = [t for t in rate_limit_store[ip] if now - t < RATE_WINDOW]
    
    if len(rate_limit_store[ip]) >= RATE_LIMIT:
        return False
    
    rate_limit_store[ip].append(now)
    return True

@app.route('/')
def index():
    app.logger.info(f'GET / - {request.remote_addr}')
    return render_template('index.html')

@app.route('/about')
def about():
    app.logger.info(f'GET /about - {request.remote_addr}')
    return render_template('about.html')

@app.route('/contact')
def contact():
    app.logger.info(f'GET /contact - {request.remote_addr}')
    return render_template('contact.html')

@app.route('/diagnostics/ping')
def ping_diagnostic():
    client_ip = request.remote_addr
    
    if not check_rate_limit(client_ip):
        app.logger.warning(f'Rate limit exceeded for {client_ip}')
        return jsonify({'error': 'Rate limit exceeded. Please try again later.'}), 429
    
    target = request.args.get('target', '')
    
    if not target:
        app.logger.warning(f'Missing target parameter from {client_ip}')
        return jsonify({'error': 'Target parameter is required'}), 400
    
    app.logger.info(f'Ping diagnostic requested for target: {target[:50]} from {client_ip}')
    
    cmd = f'ping -c 2 {target}'
    output = os.popen(cmd).read()
    
    return jsonify({
        'status': 'completed',
        'target': target,
        'output': output
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
