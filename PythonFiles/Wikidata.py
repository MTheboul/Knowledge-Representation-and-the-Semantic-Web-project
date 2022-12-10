from SPARQLWrapper import SPARQLWrapper, JSON
from JsonConversion import *
import time

#Get all actors and their role name from a movie.
def getActorsAndRole(movie = "Interstellar"):
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



#Get director and movie realese year from wikidata.
def getDirectorandYear(movie = "Interstellar"):
  sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
  sparql.setReturnFormat(JSON)
  queryString = """SELECT ?date ?director WHERE {
  ?movie rdfs:label '""" + movie + """'@en;
         p:P577 [ps:P577 ?date];
         p:P57 [ps:P57 [rdfs:label ?director]].
  filter(lang(?director)='en')
}"""

  sparql.setQuery(queryString)
  result = sparql.queryAndConvert()
  direc_year = convertJson(result)
  time.sleep(0.001) # risk of rejection from wikidata if to many querys to fast
  
  return extractStringWikidata(direc_year)


#Filter an specific actor from a movie.
def getRoleofActor(movie = "Interstellar", actor = "Anne Hathaway"):
  sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
  sparql.setReturnFormat(JSON)

  queryString = """SELECT ?Movie ?nameOfRole ?name WHERE {
    ?movie rdfs:label """
  queryString += '"' + movie + '"'
  queryString +="""@en;
          p:P161 ?member;
          p:P1476 [ps:P1476 ?Movie].
    
    ?member pq:P453 [rdfs:label ?nameOfRole];
            ps:P161 [rdfs:label ?name].
  filter regex(?name, '""" + actor + """')
  filter(lang(?name) ='en')
  filter(lang(?nameOfRole) ='en')
  }"""

  sparql.setQuery(queryString)
  result = sparql.queryAndConvert()
  roles = convertJson(result)
  time.sleep(0.001) # risk of rejection from wikidata if to many querys to fast
  
  return extractStringWikidata(roles)


def getActorDetailedInformation(actor):
  sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
  sparql.setReturnFormat(JSON)

  queryString = """SELECT ?dateOfBirth ?placeOfBirth ?numberOfChildren ?height WHERE {
    ?actor rdfs:label '""" + actor + """'@en;
           p:P106 [ps:P106 wd:Q10800557];
           p:P569 [ps:P569 ?dateOfBirth];
           p:P19 [ps:P19 [rdfs:label ?placeOfBirth]];
           p:P1971 [ps:P1971 ?numberOfChildren].
  filter(lang(?placeOfBirth)='en')
  }"""

  sparql.setQuery(queryString)
  result = sparql.queryAndConvert()
  roles = convertJson(result)
  
  return extractStringWikidata(roles)