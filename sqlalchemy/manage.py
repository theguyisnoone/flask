from flask_script import Manager,Server
from main import app,db,User#

manager=Manager(app)

manager.add_command("server",Server())

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User)#



if __name__ =="__main__":
    manager.run()







#official
# from flask import Flask
# from flask_script import Manager
# from flask_script import Command
# app = Flask(__name__)
# manager = Manager(app)
# class Hello(Command):
#     def run(self):
#         print('hello world')
#
# manager.add_command('hello', Hello())
# if __name__ == "__main__":
#     manager.run()
