from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'secretkey'
@app.route('/')
def addone():
    if 'counter' not in session:
        session['counter']= 1
    else:
        session['counter'] += 1
    return render_template('show.html')
# adding this method
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/two')
def addtwo():
    if 'counter' in session:
        session['counter'] += 2
    return render_template('show.html')

if __name__=="__main__":
    app.run(debug=True)