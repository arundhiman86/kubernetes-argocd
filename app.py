from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from the web-app!"})

@app.route("/api/goodbye")
def goodbye():
    return jsonify({"message": "Goodbye!"})

@app.route("/healthcheck")
def healthcheck():
    return jsonify({"message": "App is running!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

