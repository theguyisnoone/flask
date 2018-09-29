from flask  import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object(DevConfig)
db=SQLAlchemy(app)

@app.route('/')
# def home():
#     return '<h1>Hello world!</h1>'

class User(db.Model):
    __tablename__='user_table'
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(255))
    password=db.Column(db.String(255))

    def __init__(self,username):
        self.username=username

    def __repr__(self):
        return "<user '{}'>".format(self.username)


if __name__ =="__main__":
    app.run()