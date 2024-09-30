from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime, timedelta

app = Flask(__name__)

work_time = 41.5
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday"]

def calc_GoHomeTime(friday_start, remaining_hours):
  go_home_time = friday_start + timedelta(hours=remaining_hours)
  return go_home_time

def convert_decimal_hours_to_time(value):
  total_minutes = value * 60
  hours = total_minutes // 60
  minutes = total_minutes % 60
  return int(hours), int(minutes)

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

@app.route('/gonogo', methods=['GET', 'POST'])
def gonogo():
  if request.method == 'POST':
      times = [float(request.form.get(day, 0)) for day in weekdays]
      friday_start_time = request.form.get('friday_start', '')

      try:
          friday_start_datetime = datetime.strptime(friday_start_time, "%H:%M")
      except ValueError:
          return jsonify({"error": "Please enter a valid time in HH:MM format for Friday start time."})

      sum_of_entries = sum(times)
      message = ""
      for day, time in zip(weekdays, times):
          converted_time = convert_decimal_hours_to_time(time)
          message += f"{day}: {converted_time[0]:02d}:{converted_time[1]:02d}\n"

      message += f"Friday start time: {friday_start_time}\n"
      
      remaining_hours = work_time - sum_of_entries
      go_home_time = calc_GoHomeTime(friday_start_datetime, remaining_hours)
      go_home_time_converted = go_home_time.strftime("%H:%M")
      message += f"GoHome: {go_home_time_converted}\n"

      return jsonify({"message": message})

  return render_template('gonogo.html', weekdays=weekdays)

@app.errorhandler(403)
def forbidden_error(error):
    app.logger.error('403 error occurred: %s', error)
    return "403 Forbidden", 403

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 8080))  # Use PORT environment variable or default to 8080
  app.run(debug=True,host='0.0.0.0', port=5000)

# Modified files during execution:
# app.py