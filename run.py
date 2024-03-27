from __init__ import init_app
from database.db import db


app = init_app()



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
