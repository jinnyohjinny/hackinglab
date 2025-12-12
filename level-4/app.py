from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', '')
    greeting = ''
    
    if name:
        # Generate personalized greeting
        try:
            greeting = eval(f"f'Hello, {name}!!!'")
        except Exception as e:
            greeting = "Error generating greeting"
    
    return render_template('index.html', greeting=greeting, name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
