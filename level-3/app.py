from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkeythatnoonecanquess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/admin')
@login_required
def admin():
    if not current_user.admin:
        flash('Access denied: Admin privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    return render_template('admin.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        # VULNERABILITY: Mass Assignment
        # Directly assigning form data to User model attributes without filtering
        # The 'admin' field can be set to True if included in the form data
        
        user_data = request.form.to_dict()
        
        # We handle password separately to hash it, but other fields are auto-assigned
        password = user_data.pop('password', None)
        
        if not user_data.get('username') or not password:
            flash('Username and password are required', 'danger')
            return redirect(url_for('register'))
            
        if User.query.filter_by(username=user_data.get('username')).first():
             flash('Username already exists', 'danger')
             return redirect(url_for('register'))

        new_user = User()
        new_user.set_password(password)
        
        # Vulnerable loop: blindly setting attributes
        for key, value in user_data.items():
            if hasattr(new_user, key):
                # Simple type conversion for boolean logic which might be passed as strings
                if key == 'admin':
                    if str(value).lower() in ['true', '1', 'yes', 'on']:
                        setattr(new_user, key, True)
                    else:
                        setattr(new_user, key, False)
                else:
                    setattr(new_user, key, value)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
            
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
