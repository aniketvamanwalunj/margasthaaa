from flask import Flask, render_template

app = Flask(__name__)

# Route for home page
@app.route("/")
def home():
    return render_template("margasthaaa.html")   # make sure your HTML file is named index.html

if __name__ == "__main__":
    app.run(debug=True)
