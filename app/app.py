from flask import Flask
import math

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome To My World</h1>'

@app.route('/is_prime/<int:x>')
def is_prime(x):
    if x < 2:
        return False
    return str(all(x % i for i in range(2, int(math.sqrt(x)) + 1)))

if __name__=="__main__":
    app.run()