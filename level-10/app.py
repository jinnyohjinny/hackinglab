import os
from flask import Flask, render_template, jsonify, request
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.config['ENV'] = 'production'
app.config['DEBUG'] = False

def auth_middleware(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_token = request.cookies.get('auth_token')
        if not auth_token:
            request.is_authenticated = False
        else:
            request.is_authenticated = True
        return f(*args, **kwargs)
    return decorated_function

@app.errorhandler(404)
def not_found(e):
    return jsonify(error="Resource not found"), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify(error="Internal server error"), 500

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(error="Internal server error"), 500

@app.route('/')
def home():
    return render_template('index.html', message="Welcome to URL Path Analyzer")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'version': '2.1.4',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/analytics')
def analytics():
    return jsonify({
        'total_paths_analyzed': 48392,
        'security_score': 94.7,
        'threats_blocked': 1247,
        'uptime_days': 127,
        'last_scan': datetime.now().isoformat()
    })

@app.route('/api/scan', methods=['POST'])
def scan_path():
    data = request.get_json()
    path = data.get('path', '')
    
    analysis = {
        'path': path,
        'length': len(path),
        'safe_characters': all(c.isalnum() or c in '-_/' for c in path),
        'encoded_properly': '%' not in path or all(path[i+1:i+3].isalnum() for i, c in enumerate(path) if c == '%' and i+2 < len(path)),
        'risk_score': min(100, len(path) * 2 + path.count('%') * 5),
        'timestamp': datetime.now().isoformat()
    }
    
    return jsonify(analysis)

@app.route('/<path:user_input>')
@auth_middleware
def greeting(user_input):
    try:
        message = eval('"Hello ' + user_input + '!"')
        return render_template('index.html', message=message)
    except Exception as e:
        return jsonify(error="Internal server error"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
