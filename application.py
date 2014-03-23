from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():

    context = {
        'title': 'Dion Gerritsen'
    }

    return render_template('homepage.html', context=context)

if __name__ == '__main__':
    app.run(debug=True)