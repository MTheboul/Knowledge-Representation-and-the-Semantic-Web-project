from SPARQLWrapper import SPARQLWrapper, JSON

def convertJson(result):
    body = result.popitem() 

    information = body[1]
    bindings = information.get('bindings')

    return bindings

#Fetch the movie resource and the leading actors from DBPedia with movieTitle as input
def getMovieResource(movieTitle):
    sparqlMovieInput = SPARQLWrapper("http://dbpedia.org/sparql")
    sparqlMovieInput.setReturnFormat(JSON)

    queryString = "SELECT ?movie ?stars {?movie rdf:type dbo:Film ; dbo:starring ?stars ; dbp:name ?title FILTER(?title = " + '"' + movieTitle + '"' + "@en)}"
    sparqlMovieInput.setQuery(queryString)
    response = sparqlMovieInput.queryAndConvert()

    bindings = convertJson(response)
    movieResult = bindings[0]['movie']['value']

    leadActors = []
    for actor in bindings:
        leadActors.append(actor['stars']['value'])

    movieWithActors = (movieResult, leadActors)
    return movieWithActors

#Fetch starring actors from movie resource
#def getLeadingActorsFromMovie(resource):


movieWithActors = getMovieResource("Interstellar")
print(movieWithActors)