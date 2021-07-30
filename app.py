from flask import Flask, render_template

# Configure application
app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    greeting = 'Welcome to My Data Science Portfolio Website'

    return render_template('/index.html',
                            greeting=greeting)

@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():

    greeting = 'Welcome to My Data Science Portfolio'

    return render_template('/portfolio.html',
                            greeting=greeting)

@app.route('/blog', methods=['POST', 'GET'])
def blog():

    greeting = 'Welcome to My Data Science Blog'

    return render_template('/blog.html',
                            greeting=greeting)

@app.route('/timeline', methods=['POST', 'GET'])
def timeline():

    greeting = 'Welcome to My Data Science Blog'

    return render_template('/timeline.html',
                            greeting=greeting)