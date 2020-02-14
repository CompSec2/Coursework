from flask import render_template, Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'I hope nothing bad happens to me'

@app.rout('/login', methods=['GET','POST'])
def loginVictim():
    varError = '' 
    if request.method == 'POST':
        if request.form['password'] == 'toor' and request.form['username'] == 'toor':
             return redirect(url_for('hello'))
        else: 
            varError = 'The credentials are wrong! Try again.'
    return render.template('templates/login.html', error = varError)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
