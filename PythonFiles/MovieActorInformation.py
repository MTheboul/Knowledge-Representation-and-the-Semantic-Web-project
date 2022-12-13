from SparQL import*
from Wikidata import*
from PredefinedQuestions import*

#Collects information from diffrent datasources about a specific Actor
def getActorInformation(actor):
    #dbpedia get movies the actor have starred in
    movies = getMoviesByActor(actor)
    
    rolesInMovie = []
    for movie in movies:
        value = []
        if("(" in movie):
            tmp = movie.split("(")
            tmp = tmp[0].strip()
            #wikidata get role of the actor
            value = getRoleOfActor(tmp, actor)
        else:
            value = getRoleOfActor(movie, actor)
        if(len(value) > 0):
            rolesInMovie.append(value)
    #get personal information about actor and combine all info
    return {'Movie':rolesInMovie, 'Information':getActorDetailedInformation(actor)}

#Collects information from diffrent datasources about a specific Movie
def getMovieInformation(movie):
    #dbpedia
    movieInfo = list(getMovieWithInfo(movie))
    i = 0
    for actor in movieInfo[2]:
        #wikidata get role of the actor
        movieActorAndRole = getRoleOfActor(movie, actor)
        actorAndRole = movieActorAndRole.pop() #Remove outer list
        actorAndRole.remove(movie) #Remove title
        movieInfo[2][i] = actorAndRole #add to movieinfo
        i += 1
    #wikidata get movie genres and realise year
    genre = getMovieGenre(movie)
    year = getMovieReleaseYear(movie) 

    return {'Title':movie, 'Director':movieInfo[1], 'ActorAndRole':movieInfo[2], 'Genre':genre, 'General Info':year} #add more to general info?


#Move to API server thingy ma thing
def createQuizActor(actor):
    data = getActorInformation(actor)
    quiz = createActorQuiz(data)
    
    return quiz

#Move to API server thingy ma thing
def createQuizMovie(movie):
    data = getMovieInformation(movie)
    quiz = createMovieQuiz(data)

    return quiz

createQuizActor("Anne Hathaway")