from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory database (replace this with a real database in a production environment)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    due_date = request.form.get('due_date')

    if task_text and due_date:
        task = {'text': task_text, 'due_date': due_date}
        tasks.append(task)

    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
