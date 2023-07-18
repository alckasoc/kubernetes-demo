import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def write_to_database():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("/data/time.txt", "a") as f:
        f.write(current_time + "\n")
    return "Current time written to the database."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
