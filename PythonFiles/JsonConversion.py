#Extract the name of the resource from DBPedia
def extractStringDataDBpedia(resources):
    values = []

    if type(resources) != list:
        resources = [resources]

    for resource in resources:
        name = str(resource).replace("http://dbpedia.org/resource/", "")
        name = name.replace("_", " ")
        values.append(name)

    return values

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

#Return bindings from response of sparql query
def convertJson(result):
    body = result.popitem() 

    information = body[1]
    bindings = information.get('bindings')

    return bindings