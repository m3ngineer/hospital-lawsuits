import sys

from flask import Flask, jsonify, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# import braintree

import app_config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mattheweng@localhost:5432/health_econ'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
# Model
class Todo(db.Model):
  __tablename__ = 'todos'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)
  completed = db.Column(db.Boolean, nullable=False)
  def __repr__(self):
    return f'<Todo {self.id} {self.description}>'

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.order_by('id').all())

@app.route('/todos/create', methods=['POST'])
def create_todo():

  error = False
  body = {}
  try:
      description = request.get_json()['description']
      todo = Todo(description=description, completed=False)
      db.session.add(todo)
      db.session.commit()
      body['description']  = todo.description
      body['completed'] = todo.completed
  except:
      db.session.rollback()
      error=True
      print(sys.exc_info())
  finally:
      db.session.close()
  if error:
      abort(400)
  else:
      return jsonify(body)

@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def update_todo(todo_id):

    try:
        completed_state = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed_state
        db.session.commit()
    except:
        db.session.rollback()
        abort(400)
    finally:
        db.session.close()

    return redirect(url_for('index'))

@app.route('/todos/<todo_id>/delete', methods=['DELETE'])
def delete_todo(todo_id):

    try:
        # completed_state = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
    except:
        db.session.rollback()
        abort(400)
    finally:
        db.session.close()

    return jsonify({ 'success': True })

if __name__ == '__main__':
    app.run(debug=True)
