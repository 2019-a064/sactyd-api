from flask import Flask
from flask_restful import Resource, Api
from Clases.inicio import HelloWorld

app = Flask(__name__)
api = Api(app)

#Recurso agregado a API-REST
api.add_resource(HelloWorld, '/')


if __name__ =='__main__':
    app.run(debug=True)
