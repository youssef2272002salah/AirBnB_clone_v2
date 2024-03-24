#!/usr/bin/python3
'''display “C ” followed by the value of the text
variable (replace underscore _ symbols with a space )'''

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def hello_world():
    """ Returns some text. """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns some text. """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Returns some text. """
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is_cool"):
    """ Returns some text. """
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def python_number(n):
    """ Returns some text. """
    n = str(n)
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def python_number_template(n):
    """ Returns some text. """
    n = str(n)
    message = f'Number: {n}'
    return render_template('5-number.html', message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
