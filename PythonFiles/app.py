from flask import Flask, request, jsonify
from MovieActorInformation import createQuizActor, createQuizMovie
app = Flask(__name__)


@app.route('/createQuizActor', methods=['GET'])
def search():
    return createQuizActor(request.args.get("name"))
