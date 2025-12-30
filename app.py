from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("margasthaaa.html")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",   # allow access from local Wi-Fi devices
        port=5000,        # you can change to 8000, 8080, etc.
        debug=True
    )
