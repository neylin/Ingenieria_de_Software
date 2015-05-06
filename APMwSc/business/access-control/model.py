'''
Created on May 5, 2015

@author: neylin
'''

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
