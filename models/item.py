import scipy
import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle

from db import db

class ItemModel(db.Model):
	
	__tablename__='items'
	id=db.Column(db.Integer,primary_key=True)	
	token=db.Column(db.String(500))
	input=db.Column(db.String(500))
	output=db.Column(db.String(100))
	
	def __init__(self,token,input=None,output=None):
		self.token=token
		self.input=input
		self.output=output
		
	def json(self):
		return {'token':self.token,'input':self.input,'output':self.output}
		
	 
	@classmethod
	def find_by_name(cls,token):
		return cls.query.filter_by(token=token).first() 
		
	def save_to_db(self):
		db.session.add(self)
		db.session.commit() 


	@classmethod
	def predict_result(cls,input):
		dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

		

		Add=pd.DataFrame({'Review':[input],'Liked':[1]})

		fin=pd.concat([dataset,Add],ignore_index=True)

		corpus = []
		for i in range(0,len(fin) ):
			review = re.sub('[^a-zA-Z]', ' ', fin['Review'][i])
			review = review.lower()
			review = review.split()
			ps = PorterStemmer()
			review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
			review = ' '.join(review)
			corpus.append(review)
		
		
		
		from sklearn.feature_extraction.text import CountVectorizer

		cv = CountVectorizer(max_features = 1700)
		X = cv.fit_transform(corpus).toarray()
		y = fin.iloc[:-1,0].values



		from sklearn.naive_bayes import GaussianNB
		classifier = GaussianNB()
		classifier.fit(X[:-1], y)



		with open('Model','rb') as f1:
			classifierview = pickle.load(f1)
			
			
		return str(classifierview.predict(X)[-1])
			
