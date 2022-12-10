
from datetime import datetime
def createActorQuiz(data):
    questionAnswer = []
    movieBaseQuestions = [
        "QNUM: Who did ACTOR play in MOVIE. ANUM: ROLEOFCHAR"
    ]
    personalBaseQuestions = [
        "QNUM: Where was ACTOR born? ANUM: PLACEOFBIRTH",
        "QNUM: When was ACTOR born? ANUM: YEAROFBIRTH",
        "QNUM: How many children does ACTOR have? ANUM: NUMOFCHILDREN"
    ]
    movies = data['Movie']
    information = data['Information']
    i = 1
    for movieQues in movieBaseQuestions:
        for movInfo in movies:
            movie = movieQues
            movie = movie.replace("NUM", str(i), 2)
            movie = movie.replace("MOVIE", movInfo[0][0])
            movie = movie.replace("ROLEOFCHAR", movInfo[0][1])
            movie = movie.replace("ACTOR", movInfo[0][2])
            questionAnswer.append(movie)
            i += 1

    for personal in personalBaseQuestions:
        personal = personal.replace("NUM", str(i), 2)
        personal = personal.replace("ACTOR", movInfo[0][2])
        personal = personal.replace("NUMOFCHILDREN", information[0][0])
        personal = personal.replace("YEAROFBIRTH", information[0][1].split("T")[0])
        personal = personal.replace("PLACEOFBIRTH", information[0][2])
        questionAnswer.append(personal)
        i += 1

    return questionAnswer
        