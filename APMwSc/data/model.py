'''
Created on May 1, 2015

@author: Neylin Belisario
         Oriana Graterol
'''

from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy


manager = Manager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db) 
manager.add_command('db',MigrateCommand)

def create_app(config_name):
    app = Flask(__name__)
    #app.config.from.object(config[config_name])
    config[config_name].init_app(app)
    
    db.init_app(app)
    
    
    

