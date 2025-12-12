from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf.csrf import CSRFProtect
import redis
import os
import logging
from utils.waf import SecurityFilter
from utils.security import apply_security_headers, require_auth
from utils.mock_data import get_dashboard_stats, get_chart_data, get_recent_scans

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'cloudcode-analyzer-secret-key-2024')
app.config['SESSION_TYPE'] = 'redis'

csrf = CSRFProtect(app)

redis_client = redis.Redis(
    host=os.environ.get('REDIS_HOST', 'redis'),
    port=6379,
    decode_responses=True
)

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri=f"redis://{os.environ.get('REDIS_HOST', 'redis')}:6379"
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.after_request
def after_request(response):
    return apply_security_headers(response)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'demo' and password == 'demo123':
            session['logged_in'] = True
            session['username'] = username
            logger.info(f"User {username} logged in successfully")
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    username = session.get('username')
    session.clear()
    logger.info(f"User {username} logged out")
    return redirect(url_for('login'))

@app.route('/dashboard')
@require_auth
def dashboard():
    stats = get_dashboard_stats()
    chart_data = get_chart_data()
    recent_scans = get_recent_scans()
    
    return render_template('dashboard.html', 
                         stats=stats, 
                         chart_data=chart_data,
                         recent_scans=recent_scans,
                         username=session.get('username'))

@app.route('/analyzer')
@require_auth
def analyzer():
    return render_template('analyzer.html', username=session.get('username'))

@app.route('/documentation')
@require_auth
def documentation():
    return render_template('documentation.html', username=session.get('username'))

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/api/analyze-python', methods=['POST'])
@limiter.limit("10 per minute")
@csrf.exempt
def analyze_python():
    """
    Advanced Python code pattern analyzer.
    Uses static analysis techniques to identify potential security issues.
    """
    try:
        data = request.get_json()
        code_snippet = data.get('code_snippet', '')
        
        is_valid, error_msg, decoded_code = SecurityFilter.validate_input(code_snippet)
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        try:
            result = str(eval(decoded_code))
            sanitized_result = SecurityFilter.sanitize_output(result)
            
            return jsonify({
                "status": "success",
                "result": f"Analysis complete: {sanitized_result}",
                "patterns_detected": ["standard_python_syntax"],
                "risk_level": "low"
            })
        except Exception as e:
            return jsonify({
                "status": "error",
                "error": "Analysis failed - unable to parse code structure"
            }), 400
            
    except Exception as e:
        return jsonify({"error": "Invalid request format"}), 400

@app.route('/health')
def health():
    """Health check endpoint"""
    try:
        redis_client.ping()
        return jsonify({"status": "healthy", "redis": "connected"}), 200
    except:
        return jsonify({"status": "unhealthy", "redis": "disconnected"}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
