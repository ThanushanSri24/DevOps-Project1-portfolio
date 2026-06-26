#Import Flask class from flask library
from flask import Flask, render_template
#craete the object of Flask class
app = Flask(__name__)
#home route callback function
@app.route("/")
#the function that will be executed when the home route is accessed
def home():
    return render_template("index.html")
#debug = true allows the application to automatically reload when code changes are detected and provides detailed error messages in the browser. This is useful during development but should be turned off in production for security reasons.
if __name__ == "__main__":
    app.run(debug=True)