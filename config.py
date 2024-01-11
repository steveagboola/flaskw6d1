import os

#Get the path to the base directory/folder
basedir = os.path.abspath(os.path.dirname(__file__))
# "C:\\Users\\bstan\\Documents\\codingtemple-kekambas-137\\week6\\flask_api"

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')