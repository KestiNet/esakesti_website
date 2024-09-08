from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # This will look for 'index.html' in the 'templates' folder

@app.route('/professional_timeline')
def professional_timeline():
    return render_template('professional_timeline.html')  # This will look for 'professional_timeline.html' in the 'templates' folder

@app.route('/contact_me')
def contact_me():
    return render_template('contact_me.html')

if __name__ == "__main__":
    app.run(debug=True)