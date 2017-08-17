from flask import Flask, request, render_template, redirect
from check import validate, error_dct
import os

app = Flask('__name__')
app.config['DEBUG'] = True

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify_pass = request.form['verify_pass']
        email = request.form['email']
        preserve_email = email
        preserve_username = username

        form = validate(username, password, verify_pass, email)
        return eval(form)
    else:
        return render_template('sign_up_form.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    verify_pass = request.form['verify_pass']
    email = request.form['email']

    form = validate(username, password, verify_pass, email)
    if form == None:
        return render_template('/welcome.html', username=username)
    else:
        return redirect('/', code = 307)
            
app.run()