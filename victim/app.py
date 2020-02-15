from flask import request, render_template, url_for, Flask, redirect
app = Flask(__name__)

@app.route('/')
def hello():
    return 'I hope nothing bad happens to me'

@app.route('/login', methods=['GET','POST'])
def loginVictim():
    varError = '' 
    if request.method == 'POST':
        if request.form['password'] == 'toor' and request.form['username'] == 'toor':
       #      return redirect(url_for('hello'))
        else: 
            varError = 'The credentials are wrong! Try again.'
    return render_template('loginForm.html', error = varError)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
