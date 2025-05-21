from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Halo Dunia, Ini DevOps Pertamaku!"

if __name__ == '__main__':
    app.run()
