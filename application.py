from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/')
def homepage():

    if request.url_root != 'http://127.0.0.1:5000/':
        template = 'homepage.html'
        context = {
            'title': 'Dion Gerritsen'
        }
    else:
        template = 'dashboard.html'
        context = {
            'title': '1347 VP'
        }

    return render_template(template, context=context)

if __name__ == '__main__':
    app.run(debug=False)