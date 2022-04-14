import sys, os

sys.path.insert(0, os.path.dirname(__file__))
venvpath = '/home/j70thk7opfq0/virtualenv/flask-tut/3.7/lib/python3.7/site-packages'
sys.path.insert(0, venvpath)

from flaskr_factory_app import app as application