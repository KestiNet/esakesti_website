from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/professional_timeline')
def professional_timeline():
    return render_template('professional_timeline.html')

@app.route('/contact_me')
def contact_me():
    return render_template('contact_me.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

if __name__ == "__main__":
    app.run(debug=True)
