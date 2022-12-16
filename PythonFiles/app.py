from flask import Flask, request
from MovieActorInformation import createQuizActor, createQuizMovie
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/createQuizActor', methods=['GET'])
def QuizActor():
    return createQuizActor(request.args.get("name"))


@app.route('/createQuizMovie', methods=['GET'])
def QuizMovie():
    return createQuizMovie(request.args.get("name"))
