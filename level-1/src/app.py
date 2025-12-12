from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from models import db, User, init_db
from auth import generate_token, require_auth, require_admin, get_current_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
init_db(app)


@app.route('/')
def index():
    """Home page - redirect to dashboard if authenticated, otherwise to login."""
    username = get_current_user()
    if username:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration page."""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        # Validation
        if not username or not email or not password:
            flash('All fields are required.', 'error')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return render_template('register.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters long.', 'error')
            return render_template('register.html')
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'error')
            return render_template('register.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'error')
            return render_template('register.html')
        
        # Create new user
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login page."""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        if not username or not password:
            flash('Username and password are required.', 'error')
            return render_template('login.html')
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            flash('Invalid username or password.', 'error')
            return render_template('login.html')
        
        # Generate authentication token
        token = generate_token(username)
        
        # Create response and set cookie
        response = make_response(redirect(url_for('dashboard')))
        response.set_cookie('auth_token', token, httponly=True, max_age=3600*24)
        
        flash(f'Welcome back, {username}!', 'success')
        return response
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    """Logout user by clearing authentication cookie."""
    response = make_response(redirect(url_for('login')))
    response.set_cookie('auth_token', '', expires=0)
    flash('You have been logged out successfully.', 'info')
    return response


@app.route('/dashboard')
@require_auth
def dashboard():
    """User dashboard - requires authentication."""
    username = get_current_user()
    user = User.query.filter_by(username=username).first()
    return render_template('dashboard.html', user=user)


@app.route('/admin')
@require_admin
def admin():
    """Admin panel - requires admin privileges."""
    users = User.query.all()
    return render_template('admin.html', users=users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
