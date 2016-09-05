from flask import Flask
from flask import render_template
from flask import request
import duvet

app = Flask(__name__)
app.debug = True
d = None


@app.route("/", methods=['GET'])
def landing():
    return render_template('landing.html')


@app.route("/search", methods=['GET'])
def search():
    global d

    if request.args.get('min_seeders'):
        min_seeders = int(request.args.get('min_seeders'))
    else:
        min_seeders = None

    if request.args.get('search'):

        d = duvet.Duvet()
        d.search(request.args.get('search'), season=request.args.get('season'),
                 episode=request.args.get('episode'), min_seeders=min_seeders, wait_and_return_results=False)

    return "1"


@app.route("/results", methods=['GET'])
def results():
    global d
    if d:
        torrents = d.torrents
        finished = d.finished
    else:
        torrents = []
        finished = False

    return render_template('results.html', torrents=torrents, finished=finished)


if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run()
