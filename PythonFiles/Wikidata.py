from SPARQLWrapper import SPARQLWrapper, JSON


def printjson(result):
    body = result.popitem()
    head = result.popitem()
    print(head)
    information = body[1]
    bindings = information.get('bindings')
    for item in bindings:
        print(item)

movie = "Interstellar" #able to change movie here
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


