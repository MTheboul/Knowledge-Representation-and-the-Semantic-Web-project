from SparQL import*
from Wikidata import*
from PredefinedQuestions import*
import json

def getActorInformation(actor):
    movies = getMoviesByActor(actor)
    
    rolesInMovie = []
    for movie in movies:
        value = []
        if("(" in movie):
            tmp = movie.split("(")
            tmp = tmp[0].strip()
            value = getRoleofActor(tmp, actor)
        else:
            value = getRoleofActor(movie, actor)
        if(len(value) > 0):
            rolesInMovie.append(value)
    
    information = {'Movie':rolesInMovie, 'Information':getActorDetailedInformation(actor)}
    return information
    
def getMovieInformation(movie ="Interstellar"): #TO DO
    Actor_role = getActorsAndRole(movie)
    print()
    
def createQuizActor(actor):
    data = getActorInformation(actor)
    quiz = createActorQuiz(data)
    
    return quiz

def createQuizMovie(movie):
    data = getMovieInformation(movie)
    quiz = createActorQuiz(data)

createQuizActor("Brad Pitt")