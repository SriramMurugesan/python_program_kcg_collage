from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
tasks = []
task_id = 0

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/addtask', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        global task_id
        task_id += 1
        task = request.form.get('task')
        if task:
            tasks.append({'id': task_id, 'task': task})
    return redirect(url_for('index'))

@app.route('/deletetask/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))



# # @app.route('/login')
# # def login():
# #     return 'Login Page'
# @app.route('/register', methods=['GET','POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         return f"Username: {username}, Password: {password}"
#     return """
#     <form action = '/register' method = 'post'>
#     <label for = 'username'>Username</label>
#     <input type = 'text' name = 'username'>
#     <label for = 'password'>Password</label>
#     <input type = 'password' name = 'password'>
#     <input type = 'submit' value = 'Register'>
#     </form>
#     """


if __name__ == '__main__':
    app.run(debug=True)