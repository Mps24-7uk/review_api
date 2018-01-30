
from flask_restful import Resource,reqparse
from models.item import ItemModel


class Item(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('token',type=str,required=True,help="this cant bee empty")
	

	
	def post(self):
		
		data=Item.parser.parse_args()
		item=ItemModel(data['token'])
		
		if ItemModel.find_by_name(data['token']):
			return {'message':"An item with name '{}' already exist".format(data['token'])},400 # bad request
		

		try:
			item.save_to_db()
		except:
			return {"message":"An error occur inserting the item"},500 # internal server errror
		
		return item.json(),201  # Create

	
		


		 
class Match_Input_Output(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('token',type=str,required=True,help="cant bee empty")
	parser.add_argument('input',type=str,required=True,help="this cant be empty")
	
	def post(self):
		data=Match_Input_Output.parser.parse_args()
		item= ItemModel.find_by_name(data['token'])
		
		if item :
			item.input=data['input']
			
		try:
			item.output=ItemModel.predict_result(data['input'])
			item.save_to_db()
		except:
			item.output="None"
			item.save_to_db()
			return {"message":"Model is not trained on this value"},500 # internal server errror
			
		return item.json(),201  # Create
					
	
	
class ItemList(Resource):	
	
	def get(self,token):
		item=ItemModel.find_by_name(token)
		if item:
			return item.json()
		return {'message':'Item not found'},404  #NULL