from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key= 'your_secret_key'
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'target' not in session:
        session['target'] = random.randint(1, 100)

    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess < session['target']:
            message = 'Think higher!'
        elif guess > session['target']:
            message = 'Think lower!'
        else:
            message = 'Congratulations! You guessed it!'
            session.pop('target')
        return render_template('index.html', message=message)
    
    return render_template('index.html', message=None)

@app.route('/reset', methods=['GET'])
def reset():
    session.pop('target', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)