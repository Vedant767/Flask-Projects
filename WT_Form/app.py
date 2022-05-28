from flask import Flask, render_template, request
from forms import StudentForm

app = Flask(__name__)
app.secret_key = "form_csrf_token_security_key"

@app.route('/form', methods = ['POST', 'GET'])
def FormView():
    form = StudentForm()
 
    if request.method =='POST':
        form = StudentForm()
        if form.validate_on_submit() == True:
            return "Process Successful"
        return render_template('form.html', form = form)
     
    return render_template('form.html', form = form)

app.run(host='localhost', port=5000)