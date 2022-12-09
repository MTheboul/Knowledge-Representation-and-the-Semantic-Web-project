from SPARQLWrapper import SPARQLWrapper, JSON


def printjson(result):
    body = result.popitem()
    head = result.popitem()
    print(head)
    information = body[1]
    bindings = information.get('bindings')
    for item in bindings:
        print(item)

def getActorsAndRole(movie = "Interstellar"):
  sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
  sparql.setReturnFormat(JSON)
  queryString = """SELECT ?Movie ?nameOfRole ?name WHERE {
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
  printjson(result)

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
  printjson(result)

def getRoleofActorFilter(movie = "Interstellar", actor = "Anne Hathaway"):
  sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
  sparql.setReturnFormat(JSON)
  queryString = """SELECT ?Movie ?nameOfRole ?name WHERE {
    ?movie rdfs:label '""" + movie +"""'@en;
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
  printjson(result)