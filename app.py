from flask import Flask, render_template
import os

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

@app.route('/gonogo')
def gonogo():
    return render_template('gonogo.html')

@app.errorhandler(403)
def forbidden_error(error):
  app.logger.error('403 error occurred: %s', error)
  return "403 Forbidden", 403


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))  # Use PORT environment variable or default to 8080
    app.run(debug=True,host='0.0.0.0', port=5000)
