from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask Application deployed using Jenkins!"

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "message": "Application is running successfully"
    })


@app.route("/about")
def about():
    return jsonify({
        "application": "Flask Jenkins Pipeline Demo",
        "technology": [
            "Python",
            "Flask",
            "Jenkins",
            "CI/CD"
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
