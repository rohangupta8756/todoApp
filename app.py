from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock data - replace with database in real application
tasks = [
    {'id': 1, 'title': 'Learn Flask', 'done': False},
    {'id': 2, 'title': 'Build a To-Do App', 'done': False}
]
next_task_id = 3

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global next_task_id
    title = request.form['title']
    new_task = {'id': next_task_id, 'title': title, 'done': False}
    tasks.append(new_task)
    next_task_id += 1
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>')
def update_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = not task['done']
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
