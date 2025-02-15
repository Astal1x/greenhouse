from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)
soiltext = ['Enough', 'Not enough, needs water!']
lighttext = ['Enough', 'Not enough, needs to turning on lights!']
@app.route("/")
def index():
    return render_template("index.html")  # Load on HTML

@app.route("/data")
def get_data():
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 60), 2)
    soil = random.choice(soiltext)
    light = random.choice(lighttext)
    return jsonify({"temperature": temperature, "humidity": humidity, 'soil': soil, "light": light})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
