from flask import Flask, request, render_template, url_for, session, redirect
import logging 
app = Flask(__name__)

logging.basicConfig(filename='demo.log', level=logging.DEBUG)

@app.route('/loggedIn')
def hello():
    app.logger.info('Processing default request')        
    return 'I hope nothing bad happens to me!'

@app.route('/', methods=['GET','POST'])
def loginVictim():
    varError = ''
    if request.method == 'POST':
        if request.form['password'] == 'toor' and request.form['username'] == 'root':
            app.logger.info('Processing default request')
            return redirect(url_for('hello')) 
        varError = 'The credentials are wrong! Try again.' 
    app.logger.info('Processing default request')        
    return render_template('loginForm.html',  error = varError)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
