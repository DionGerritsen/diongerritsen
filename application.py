import re
from flask import Flask, render_template, request, redirect
app = Flask(__name__)



@app.route('/')
def homepage():
    
    route = request.url_root

    if not "1347" in route:
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