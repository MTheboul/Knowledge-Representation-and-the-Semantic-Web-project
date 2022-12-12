from datetime import datetime
import json
     
def createActorQuiz(data):
    questionAnswer = {}
    movieBaseQuestions = [
        ["Question: Who did ACTOR play in MOVIE.", "Answer: ROLEOFCHAR"]
    ]
    personalBaseQuestions = [
        ["Question: Where was ACTOR born?", "Answer: PLACEOFBIRTH"],
        ["Question: When was ACTOR born?", "Answer: YEAROFBIRTH"],
        ["Question: How many children does ACTOR have?", "Answer: NUMOFCHILDREN"]
    ]
    movies = data['Movie']
    information = data['Information']
    i = 1
    for movieQues in movieBaseQuestions:
        for movInfo in movies:
            question = movieQues[0]
            question = question.replace("MOVIE", movInfo[0][0])
            question = question.replace("ACTOR", movInfo[0][2])
            answer = movieQues[1].replace("ROLEOFCHAR", movInfo[0][1])
            
            questionAnswer["Q" + str(i)] = [question, answer]
            i += 1

    for personal in personalBaseQuestions:
        question = personal[0].replace("ACTOR", movInfo[0][2])
        answer = personal[1]
        answer = answer.replace("NUMOFCHILDREN", information[0][0])
        answer = answer.replace("YEAROFBIRTH", information[0][1].split("T")[0])
        answer = answer.replace("PLACEOFBIRTH", information[0][2])

        questionAnswer["Q" + str(i)] = [question, answer]
        i += 1
    js = json.dumps(questionAnswer,indent=2)
    return js
        