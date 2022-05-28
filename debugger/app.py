from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcd'

app.debug = True
toolbar = DebugToolbarExtension(app)

@app.route('/form')
def form():
    return render_template('form.html')
 
app.run(host='localhost', port=5000)