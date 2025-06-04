# Basic template for what I need
from flask import Flask


app = Flask(__name__)

@app.route('')
def create(): 
    return 'Created!'



if __name__ == '__main__':
    app.run(debug=True)