from SPARQLWrapper import SPARQLWrapper, JSON
from JsonConversion import *
import time

#Get all actors and their role name from a movie.
def getActorsAndRole(movie):
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

#Get Genre of movie
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
  time.sleep(1) # risk of rejection from wikidata if to many querys to fast
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