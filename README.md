# <p align="center">Review Bot Api<p>
  
<p align="center"><img src="https://github.com/Mps24-7uk/review_api/blob/master/Images/sentiment-analysis.jpg" width="400" height="250"></p>


## Introducton

ML Based Review Api designed to handle reviews given by User(customers) and Predict whether the Review is positive or negative

In addition to the pure API implementation from Scratch, a number of high-level classes to make the development of API easy and straightforward.

## Dependencies [Required Modules](https://github.com/Mps24-7uk/review_api/blob/master/requirements.txt)

1. nltk
2. regex
3. scipy
4. numpy
5. pandas
6. sklearn
7. Flask
8. Flask-RESTful
9. FLask-SQLALchemy
10. uwsgi
11. psycopg


# Methodology/Principal

 It consists of two important steps : Creating and Production

<p align="center"><img src="https://image.slidesharecdn.com/machinelearninginproduction-150928004829-lva1-app6891/95/machine-learning-in-production-12-638.jpg?cb=1443401438" width="500" height="300"></p>


### 1. Creation

Train the Model Using Historical Dataset and test Accuracy the Model 

[How to train and test the Model](https://github.com/Mps24-7uk/Restaurant_Reviews/blob/master/README.md)

### 2. Production

#### Serialization & Deserialization
  In the context of data storage, 
  serialization is the process of translating data structures or object state into a format that can be stored.
  
  This is done to reduce the size and complexity of dataset and which reduces the time of re-execution.
  
#### Creating an API using Flask

There are three important parts in constructing our wrapper function, Apicall():

* Getting the request data enter by user (for which predictions are to be made)
* Loading our pickled estimator
* jsonify our predictions and send the response back 

  
 # Deployment 

### [Heroku Cloud Station](https://www.heroku.com/platform)

Heroku is a cloud platform based on a managed container system, with integrated data services and a powerful ecosystem, for    deploying and running modern apps.

Deployment Involves following process:

* Create Application
* Provid GitHub Connection
* Select Python as Build Packages
* Heruko Postreg:: DataBase
* Deploy Application



