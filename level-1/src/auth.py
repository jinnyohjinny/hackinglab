import base64
from functools import wraps
from flask import request, redirect, url_for, flash


def generate_token(username):
    """
    Generate authentication token for user.
    
    Args:
        username: The username to generate token for
        
    Returns:
        Authentication token string
    """
    token = base64.b64encode(username.encode()).decode()
    return token


def verify_token(token):
    """
    Verify and decode authentication token.
    
    Args:
        token: The authentication token to verify
        
    Returns:
        Username if valid, None otherwise
    """
    try:
        username = base64.b64decode(token.encode()).decode()
        return username
    except Exception:
        return None


def require_auth(f):
    """
    Decorator to require authentication for routes.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('auth_token')
        if not token:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        
        username = verify_token(token)
        if not username:
            flash('Invalid session. Please log in again.', 'error')
            return redirect(url_for('login'))
        
        return f(*args, **kwargs)
    return decorated_function


def require_admin(f):
    """
    Decorator to require admin privileges for routes.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('auth_token')
        if not token:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        
        username = verify_token(token)
        if not username:
            flash('Invalid session. Please log in again.', 'error')
            return redirect(url_for('login'))
        
        if username != 'admin':
            flash('Access denied. Admin privileges required.', 'error')
            return redirect(url_for('dashboard'))
        
        return f(*args, **kwargs)
    return decorated_function


def get_current_user():
    """
    Get the currently authenticated user from the request.
    
    Returns:
        Username if authenticated, None otherwise
    """
    token = request.cookies.get('auth_token')
    if not token:
        return None
    return verify_token(token)
