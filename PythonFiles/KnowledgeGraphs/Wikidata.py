from SPARQLWrapper import SPARQLWrapper, JSON
import time

#Get all actors and their role name from a movie.
def getActorsAndRoles(movie):
  sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
  sparql.setReturnFormat(JSON)
  queryString = """SELECT ?nameOfRole ?name WHERE {
    ?movie rdfs:label '"""+ movie +"""'@en;
          p:P161 ?member;
          p:P1476 [ps:P1476 ?Movie].
    
    ?member pq:P453 [rdfs:label ?nameOfRole];
            ps:P161 [rdfs:label ?name].

    filter(lang(?name)="en")
    filter(lang(?nameOfRole)="en")
  }limit 200"""

  sparql.setQuery(queryString)
  result = sparql.queryAndConvert()
  roles = convertJson(result)

  return extractStringWikidata(roles)

#get movie realese year from wikidata (only get the first relese date).
def getMovieReleaseYear(movie):
  sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
  sparql.setReturnFormat(JSON)
  queryString = """
    select ?date where{
    ?movie rdfs:label '""" + movie + """'@en;
           p:P31 [ps:P31 wd:Q11424];
           p:P577 [ps:P577 ?date].
      }limit 1
      """
  sparql.setQuery(queryString)
  result = sparql.queryAndConvert()
  year = convertJson(result)
  return extractStringWikidata(year)

#Get Genre/-s of movie
def getMovieGenre(movie):
  sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
  sparql.setReturnFormat(JSON)
  queryString = """SELECT ?genre WHERE {
    ?movie rdfs:label '""" + movie + """'@en;
           p:P31 [ps:P31 wd:Q11424];
           p:P136 [ps:P136 [rdfs:label ?genre]].
      filter (lang(?genre) = 'en')
  }"""
  sparql.setQuery(queryString)
  result = sparql.queryAndConvert()
  genre = convertJson(result)
  return extractStringWikidata(genre)

#Filter an specific actor from a movie.
def getRoleOfActor(movie, actor):
  sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
  sparql.setReturnFormat(JSON)
  lenght = len(movie) #there is an upperlimit on the number of chars in the query around 15 of the unions are possible with almost any name
  queryString = """SELECT ?Movie ?nameOfRole ?name WHERE { { """
  if (len(movie) > 1): # One actor from multiple movies
    for i in range(lenght):
      movie[i] = movie[i].split("(")[0].strip() # remove dbpedia (film) info
      queryString += """SELECT ?Movie ?nameOfRole ?name WHERE {?movie rdfs:label """
      queryString += '"' + movie[i] + '"'
      # ugly this way but needed to save chars in the query
      queryString +="""@en;p:P161 ?member;p:P1476 [ps:P1476 ?Movie].?member pq:P453 [rdfs:label ?nameOfRole];ps:P161 [rdfs:label ?name]. filter(lang(?nameOfRole) ='en') filter regex(?name, '""" + actor + """') }limit 1"""
      if(i != lenght-1):
        queryString += """ } union { """
      else:
        queryString += """} }"""
  else: # get all actors in one movie
    movie = movie.split("(")[0].strip() # remove dbpedia (film) info
    queryString = """SELECT ?Movie ?nameOfRole ?name WHERE { 
    ?movie rdfs:label '"""+ movie + """'@en;
           p:P161 ?member;
           p:P1476 [ps:P1476 ?Movie].
    
    ?member pq:P453 [rdfs:label ?nameOfRole];
            ps:P161 [rdfs:label ?name].
    filter(lang(?name)='en')
    filter(lang(?nameOfRole) ='en')
  }"""

  sparql.setQuery(queryString)
  result = sparql.queryAndConvert()
  roles = convertJson(result)
  
  
  return extractStringWikidata(roles)


def getActorDetailedInformation(actor):
  sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
  sparql.setReturnFormat(JSON)

  queryString = """SELECT ?dateOfBirth ?placeOfBirth ?numberOfChildren WHERE {
    ?actor rdfs:label '""" + actor + """'@en;
           p:P106 [ps:P106 wd:Q10800557];
           p:P569 [ps:P569 ?dateOfBirth];
           p:P19 [ps:P19 [rdfs:label ?placeOfBirth]].
  optional{ ?actor p:P1971 [ps:P1971 ?numberOfChildren]}.
  filter(lang(?placeOfBirth)='en')
}"""

  sparql.setQuery(queryString)
  result = sparql.queryAndConvert()
  roles = convertJson(result)
  stringData = extractStringWikidata(roles)
  return stringData

def convertJson(result):
  body = result.popitem() 
  information = body[1]
  bindings = information.get('bindings')
  return bindings

def extractStringWikidata(resources):
    values = []
    if(len(resources) == 0): return values
    keys = resources[0].keys()
    if type(resources) != list:
        resources = [resources]

    if(len(keys) > 1):
        value = []
    else:
        value = ""

    for resource in resources:
        for key in keys:
            if(type(value) == list):
                value.append(resource[key]['value'])
            else:
                value = resource[key]['value']
        values.append(value)
        if(type(value) == list):
            value = []
        else:
            value = ""

    return values