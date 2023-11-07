from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.dotabase"
app.config["SQLALCHEMY_TRACT_MODIFICATIONS"] = False

#To solve runtime error of working outside application context
app.app_context().push()

#To initialise the database
db = SQLAlchemy(app)

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100))
  complete = db.Column(db.Boolean)

@app.route("/")
def index():
  #To display on the page, query the database
  todo_list = Todo.query.all()
  return render_template("base.html", todo_list=todo_list)

#this enable adding ToDos
@app.route("/add", methods = ["POST"])
def add():
  title = request.form.get("title")
  new_todo = Todo(title=title, complete = False)
  db.session.add(new_todo)
  db.session.commit()
  return redirect(url_for("index"))

#creating function for update
@app.route("/update/<int:todo_id>")
def update(todo_id):
  todo = Todo.query.filter_by(id=todo_id).first()
  todo.complete = not todo.complete
  db.session.commit()
  return redirect(url_for("index"))

#creating function for delete
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
  todo = Todo.query.filter_by(id=todo_id).first()
  db.session.delete(todo)
  db.session.commit()
  return redirect(url_for("index")) 

if __name__ == "__main__":
  #To create the database
  db.create_all()
  app.run(debug=True)