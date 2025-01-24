from flask import Flask
from flask_migrate import Migrate
from server.models import db



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

# Ensure models are imported after db.init_app to avoid circular imports
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'

if __name__ == "__main__":
    app.run(debug=True)