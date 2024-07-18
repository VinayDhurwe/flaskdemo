from flask import Flask, render_template,request,flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/palindrome', methods=['GET', 'POST'])
def palindrome():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        if text.strip():  # Check if the input text is not empty after stripping whitespace
            if is_palindrome(text):
                result = f'"{text}" is a palindrome!'
            else:
                result = f'"{text}" is not a palindrome.'
        else:
            result = 'Please enter a valid text.'
    return render_template('palindrome.html', result=result)


@app.route('/fibonacci', methods =['GET','POST'])
def fibonacci():
    result = None
    if request.method == 'POST':
        try:
            n = int(request.form['number'])
            result = fib(n)
        except ValueError:
            flash('Please enter a valid integer', 'danger' )
    return render_template('fibonacci.html', result=result)

@app.route('/reverse', methods = ['GET','POST'])
def reverse():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        result = text[::-1]
    return render_template('reverse.html', result=result)


def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
    return a

def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 