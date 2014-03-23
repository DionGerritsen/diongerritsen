from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hallo Alicia!'

@app.route('/test/')
def hello_test():
    return 'Dit is een test'

if __name__ == '__main__':
    app.run()