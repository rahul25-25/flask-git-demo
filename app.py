from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Rahul"

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)
