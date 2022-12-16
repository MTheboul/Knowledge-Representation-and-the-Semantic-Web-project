from KnowledgeGraphs import SparQL, Wikidata
from PredefinedQuestions import*

#Collects information from diffrent datasources about a specific Actor
def getActorInformation(actor):
    #dbpedia get movies the actor have starred in
    movies = SparQL.getMoviesByActor(actor)
    
    rolesInMovie = []
    for movie in movies:
        value = []
        if("(" in movie):
            tmp = movie.split("(")
            tmp = tmp[0].strip()
            #wikidata get role of the actor
            value = Wikidata.getRoleOfActor(tmp, actor)
        else:
            value = Wikidata.getRoleOfActor(movie, actor)
        if(len(value) > 0):
            rolesInMovie.append(value)
    #get personal information about actor and combine all info
    return {'Movie':rolesInMovie, 'Information':Wikidata.getActorDetailedInformation(actor)}

#Collects information from diffrent datasources about a specific Movie
def getMovieInformation(movie):
    #dbpedia
    movieInfo = list(SparQL.getMovieWithInfo(movie))
    i = 0
    for actor in movieInfo[2]:
        # error handlning
        if("(" in actor):
            tmp = actor.split("(")
            tmp = tmp[0].strip()
            #wikidata get role of the actor
            movieActorAndRole = Wikidata.getRoleOfActor(movie, tmp)
        else:
            movieActorAndRole = Wikidata.getRoleOfActor(movie, actor)

        #no role or actor result
        if(movieActorAndRole == []):
            movieInfo[2].remove(actor)
            continue
        actorAndRole = movieActorAndRole.pop() #Remove outer list
        actorAndRole.remove(movie) #Remove title
        movieInfo[2][i] = actorAndRole #add to movieinfo
        i += 1
    #wikidata get movie genres and realise year
    genre = Wikidata.getMovieGenre(movie)
    year = Wikidata.getMovieReleaseYear(movie) 

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