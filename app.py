from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# Load expenses from file
def load_expenses():
    try:
        with open('expenses.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        category = request.form['category']
        expenses = load_expenses()
        expenses.append({'description': description, 'amount': amount, 'category': category})
        save_expenses(expenses)
        return redirect(url_for('view_expenses'))
    return render_template('add_expenses.html')

@app.route('/view')
def view_expenses():
    expenses = load_expenses()
    total_expenses = sum(expense['amount'] for expense in expenses)
    return render_template('view_expenses.html', expenses=expenses, total_expenses=total_expenses)

if __name__ == '__main__':
    app.run(debug=True)
