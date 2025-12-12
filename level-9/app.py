import os
from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)
app.config['ENV'] = 'production'
app.config['DEBUG'] = False

@app.errorhandler(404)
def not_found(e):
    return jsonify(error="Resource not found"), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify(error="Internal server error"), 500

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(error="An error occurred"), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parse/<path:user_input>')
def parse_url(user_input):
    try:
        result = eval('"' + user_input + '"')
        return jsonify(result=result, status="success")
    except Exception as e:
        return jsonify(error="Invalid input format", status="error"), 400

@app.route('/api/validate', methods=['POST'])
def validate_url():
    data = request.get_json()
    url = data.get('url', '')
    
    checks = {
        'length': len(url) < 2048,
        'protocol': url.startswith('http://') or url.startswith('https://'),
        'special_chars': not any(c in url for c in ['<', '>', '{', '}']),
        'encoding': all(ord(c) < 128 for c in url)
    }
    
    return jsonify({
        'url': url,
        'checks': checks,
        'safe': all(checks.values()),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/logs')
def get_logs():
    fake_logs = [
        {'timestamp': '2025-12-12 10:45:23', 'level': 'INFO', 'message': 'URL validation completed'},
        {'timestamp': '2025-12-12 10:44:15', 'level': 'INFO', 'message': 'Path sanitization successful'},
        {'timestamp': '2025-12-12 10:43:02', 'level': 'WARN', 'message': 'Suspicious pattern detected'},
        {'timestamp': '2025-12-12 10:42:18', 'level': 'INFO', 'message': 'Security check passed'},
        {'timestamp': '2025-12-12 10:41:55', 'level': 'INFO', 'message': 'Request processed successfully'}
    ]
    return jsonify(logs=fake_logs)

@app.route('/api/stats')
def get_stats():
    return jsonify({
        'total_requests': 15847,
        'blocked_requests': 342,
        'success_rate': 97.8,
        'uptime': '45 days',
        'last_update': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
