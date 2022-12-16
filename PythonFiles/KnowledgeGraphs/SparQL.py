from SPARQLWrapper import SPARQLWrapper, JSON


#Fetch the movie resource and the leading actors from DBPedia with movieTitle as input
def getMovieWithInfo(movieTitle):
    sparqlMovieInput = SPARQLWrapper("http://dbpedia.org/sparql")
    sparqlMovieInput.setReturnFormat(JSON)

    queryString = "SELECT ?movie ?stars ?director {?movie rdf:type dbo:Film ; dbo:starring ?stars ; dbo:director ?director ; dbp:name ?title FILTER(?title = " + '"' + movieTitle + '"' + "@en)}"
    sparqlMovieInput.setQuery(queryString)
    response = sparqlMovieInput.queryAndConvert()

    bindings = convertJson(response)
    movieResult = bindings[0]['movie']['value']
    directorResult = bindings[0]['director']['value']

    leadActors = []
    for actor in bindings:
        leadActors.append(actor['stars']['value'])

    movieResult = extractStringDataDBpedia(movieResult)
    directorResult = extractStringDataDBpedia(directorResult)
    leadActors = extractStringDataDBpedia(leadActors)

    movieWithActors = (movieResult, directorResult, leadActors)
    return movieWithActors

#Fetch movies that a certain actor has had a starring role in
def getMoviesByActor(actorName):
    sparqlMoviesByActorInput = SPARQLWrapper("http://dbpedia.org/sparql")
    sparqlMoviesByActorInput.setReturnFormat(JSON)

    queryString = "SELECT ?movies {?movies rdf:type dbo:Film ; dbp:starring ?star FILTER(?star = " + '"' + actorName + '"' + "@en)}"
    sparqlMoviesByActorInput.setQuery(queryString)
    response = sparqlMoviesByActorInput.queryAndConvert()

    bindings = convertJson(response)
    movies = []
    for movie in bindings:
        movies.append(movie['movies']['value'])

    movies = extractStringDataDBpedia(movies)
    return movies


#movieWithActors = getMovieWithInfo("Interstellar")
#print(movieWithActors)
#moviesFromActor = getMoviesByActor("Anne Hathaway")
#print(moviesFromActor)
def extractStringDataDBpedia(resources):
    values = []

    if type(resources) != list:
        resources = [resources]

    for resource in resources:
        name = str(resource).replace("http://dbpedia.org/resource/", "")
        name = name.replace("_", " ")
        values.append(name)

    return values

def convertJson(result):
    body = result.popitem() 

    information = body[1]
    bindings = information.get('bindings')

    return bindings