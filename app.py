import os
from flask import Flask
from flask_restful import Api
 
from resources.item import Item,Match_Input_Output,ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='jose'
api=Api(app)



api.add_resource(Item,'/item')
api.add_resource(Match_Input_Output,'/Match')
api.add_resource(ItemList,'/items/<string:token>')

if __name__ == "__main__":
	from db import db
	db.init_app(app)
	app.run(port=5000, debug=True)