from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import braintree

import app_config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://udacitystudios@localhost:5432/todoapp'
db = SQLAlchemy(app)

# Model
class Todo(db.Model):
  __tablename__ = 'todos'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)

  def __repr__(self):
    return f'<Todo {self.id} {self.description}>'

db.create_all()

# Paypal
gateway = braintree.BraintreeGateway(access_token=use_your_access_token)

stripe_keys = {
  'secret_key': os.environ['STRIPE_SECRET_KEY'],
  'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

@app.route("/client_token", methods=["GET"])
def client_token():
  return client_token = gateway.client_token.generate()

@app.route('/')
def index():
    return render_template('index.html', data=[{
            'description': 'Todo 1'
          }, {
            'description': 'Todo 2'
          }, {
            'description': 'Todo 3'
          }])


if __name__ == '__main__':
    app.run()
