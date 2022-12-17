from KnowledgeGraphs import SparQL, Wikidata, GoogleKnowledgeGraph
from PredefinedQuestions import*

#Collects information from diffrent datasources about a specific Actor
def getActorInformation(actor):
    #dbpedia get movies the actor have starred in
    movies = SparQL.getMoviesByActor(actor)

    rolesInMovie = []
    #If the actor has done more than 15 movies we need to do mutiple queries
    if(len(movies) < 15):
        #wikidata get role of the actor
        rolesInMovie = Wikidata.getRoleOfActor(movies, actor)
    else:
        while(len(movies)>0):
            tmpList = movies[0:15]
            movies = movies[15:len(movies)-1]
            roles = Wikidata.getRoleOfActor(tmpList, actor)
            for role in roles:
                rolesInMovie.append(role)

    return {'Movie':rolesInMovie, 'Information':Wikidata.getActorDetailedInformation(actor)}

#Collects information from diffrent datasources about a specific Movie
def getMovieInformation(movie):
    #dbpedia
    movieInfo = list(SparQL.getMovieWithInfo(movie))

    # Gets all actors and roles avalible for the movie
    movieActorAndRole = Wikidata.getActorsAndRoles(movie)
    tmpRolActor = []
    # Only include leads
    for i, actor in enumerate(movieInfo[2]):
        for roleAndActor in movieActorAndRole:
            if(actor in roleAndActor):
                tmpRolActor.append(roleAndActor)
                break
    
    movieInfo[2] = tmpRolActor

    #wikidata get movie genres and realise year
    genre = Wikidata.getMovieGenre(movie)
    year = Wikidata.getMovieReleaseYear(movie) 

    return {'Title':movie, 'Director':movieInfo[1], 'ActorAndRole':movieInfo[2], 'Genre':genre, 'General Info':year} #add more to general info?


#Move to API server thingy ma thing
def createQuizActor(actor):
    liklySearchTerm = GoogleKnowledgeGraph.getMostLiklySearchTerm(actor, 'Person')
    data = getActorInformation(liklySearchTerm)
    quiz = generateActorQuiz(data)
    
    return quiz
    

#Move to API server thingy ma thing
def createQuizMovie(movie):
    liklySearchTerm = GoogleKnowledgeGraph.getMostLiklySearchTerm(movie, 'Movie')
    
    data = getMovieInformation(liklySearchTerm)
    quiz = generateMovieQuiz(data)

    return quiz