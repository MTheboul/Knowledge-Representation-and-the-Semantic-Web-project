import json

#Structrued like this to easy add/remove questions if new infor added (hopefully)
def generateActorQuiz(data):
    questionAnswer = {}
    movieBaseQuestions = [
        ["Question: In MOVIE who did ACTOR play?", "Answer: ROLEOFCHAR"]
    ]
    personalBaseQuestions = [
        ["Question: Where was ACTOR born?", "Answer: PLACEOFBIRTH"],
        ["Question: When was ACTOR born?", "Answer: YEAROFBIRTH"],
        ["Question: How many children does ACTOR have?", "Answer: NUMOFCHILDREN"]
    ]
    movies = data['Movie']
    information = data['Information']
    if(len(information) < 3): # most of the time number of childern missing
        information[0].insert(0, '0') # add that they have no childeren to start of list
    i = 1
    for movieQues in movieBaseQuestions:
        for movInfo in movies:
            question = movieQues[0]
            question = question.replace("MOVIE", movInfo[0])
            question = question.replace("ACTOR", movInfo[2])
            answer = movieQues[1].replace("ROLEOFCHAR", movInfo[1])
            
            questionAnswer["Q" + str(i)] = [question, answer]
            i += 1

    # Some inconsistencies can appear if Two or more actors have the exact same name and are both working as actors
    # Not fixed
    for personal in personalBaseQuestions:
        question = personal[0].replace("ACTOR", movInfo[2])
        answer = personal[1]
        answer = answer.replace("NUMOFCHILDREN", information[0][0])
        answer = answer.replace("YEAROFBIRTH", information[0][1].split("T")[0])
        answer = answer.replace("PLACEOFBIRTH", information[0][2])

        questionAnswer["Q" + str(i)] = [question, answer]
        i += 1

    return json.dumps(questionAnswer,indent=2)

#Structrued like this to easy add/remove questions if new infor added
def generateMovieQuiz(data):
    questionAnswer = {}
    actorBaseQuestions = [
        ["Question: Who did ACTOR play in MOVIE?", "Answer: ROLEOFCHAR"],
        ["Question: Who played ROLEOFCHAR play in MOVIE?", "Answer: ACTOR"]
    ]
    directorBaseQuestions = [
         ["Question: Who directed MOVIE?", "Answer: DIRECTOR"]
    ]
    genreBaseQuestions = [
        ["Question: What Genre is MOVIE?", "Answer: GENRE"]
    ]
    generalMovieBaseQuestions = [
        ["Question: When was MOVIE released?", "Answer: RELEASEYEAR"],
    ]
    title = data['Title']
    directors = data['Director']
    actorRoles = data['ActorAndRole']
    genres = data['Genre']
    generalInfo = data['General Info'] #only year right now

    i = 1
    for actorQue in actorBaseQuestions:
        for actorRoleFacit in actorRoles:
            question = actorQue[0]
            question = question.replace("ROLEOFCHAR", actorRoleFacit[0])
            question = question.replace("ACTOR", actorRoleFacit[1])
            question = question.replace("MOVIE", title)
            
            answer = actorQue[1]
            answer = answer.replace("ROLEOFCHAR", actorRoleFacit[0])
            answer = answer.replace("ACTOR", actorRoleFacit[1])

            questionAnswer["Q" + str(i)] = [question, answer]
            i += 1

    for direcQue in directorBaseQuestions:
        for director in directors:
            question = direcQue[0]
            question = question.replace("MOVIE", title)

            answer = direcQue[1]
            answer = answer.replace("DIRECTOR", director)
            questionAnswer["Q" + str(i)] = [question, answer]
            i += 1
    
    for genreQue in genreBaseQuestions:
        for genre in genres:
            question = genreQue[0]
            question = question.replace("MOVIE", title)

            answer = genreQue[1]
            answer = answer.replace("GENRE", genre)

            questionAnswer["Q" + str(i)] = [question, answer]
            i += 1

    for generalQue in generalMovieBaseQuestions:
        for general in generalInfo:
            question = generalQue[0]
            question = question.replace("MOVIE", title)

            answer = generalQue[1]
            answer =  answer.replace("RELEASEYEAR", general.split("T")[0])

            questionAnswer["Q" + str(i)] = [question, answer]
            i += 1
    
    return json.dumps(questionAnswer,indent=2)