from flaskblog import create_app
from flaskblog import db
app = create_app()
with app.app_context():
    db.create_all()
    print("Database created successfully!")
if __name__ == '__main__':
    app.run(debug=True)
