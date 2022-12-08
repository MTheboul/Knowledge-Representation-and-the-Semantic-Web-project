from SPARQLWrapper import SPARQLWrapper, JSON

#Extract the name of the resource from DBPedia
def extractStringData(resources):
    values = []
    for resource in resources:
        name = str(resource).replace("http://dbpedia.org/resource/", "")
        name = name.replace("_", " ")
        values.append(name)

    return values

#Return bindings from response of sparql query
def convertJson(result):
    body = result.popitem() 

    information = body[1]
    bindings = information.get('bindings')

    return bindings

#Fetch the movie resource and the leading actors from DBPedia with movieTitle as input
def getMovieWithInfo(movieTitle):
    sparqlMovieInput = SPARQLWrapper("http://dbpedia.org/sparql")
    sparqlMovieInput.setReturnFormat(JSON)

    queryString = "SELECT ?movie ?stars ?director {?movie rdf:type dbo:Film ; dbo:starring ?stars ; dbo:director ?director ; dbp:name ?title FILTER(?title = " + '"' + movieTitle + '"' + "@en)}"
    sparqlMovieInput.setQuery(queryString)
    response = sparqlMovieInput.queryAndConvert()

    bindings = convertJson(response)
    movieResult = [bindings[0]['movie']['value']]
    directorResult = [bindings[0]['director']['value']]

    leadActors = []
    for actor in bindings:
        leadActors.append(actor['stars']['value'])

    movieResult = extractStringData(movieResult)
    directorResult = extractStringData(directorResult)
    leadActors = extractStringData(leadActors)

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

    movies = extractStringData(movies)
    return movies


movieWithActors = getMovieWithInfo("Interstellar")
print(movieWithActors)
moviesFromActor = getMoviesByActor("Anne Hathaway")
print(moviesFromActor)