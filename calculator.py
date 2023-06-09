from flask import Flask, render_template, request
from calculator import Calculator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    result = None
    if operation == 'add':
        result = Calculator.add(num1, num2)
    elif operation == 'subtract':
        result = Calculator.subtract(num1, num2)
    elif operation == 'multiply':
        result = Calculator.multiply(num1, num2)
    elif operation == 'divide':
        result = Calculator.divide(num1, num2)
    elif operation == 'power':
        result = Calculator.power(num1, num2)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
