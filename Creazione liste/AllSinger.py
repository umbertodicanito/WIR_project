from SPARQLWrapper import SPARQLWrapper, JSON
#lista per visualizzare file JSON#
singers = []
#costruzione query: select all singers with type Singer#
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery(
"""select ?singer where {?singer a yago:Singer110599806.} """)
#aggiunti risultati in forma JSON alla lista#
sparql.setReturnFormat(JSON)
resultsSingers = sparql.query().convert()
singers.append(resultsSingers)
#getting second page#
sparql.setQuery(
"""select ?singer where {?singer a yago:Singer110599806.} OFFSET 10000 LIMIT 10000""")
#aggiunti risultati in forma JSON alla lista#
sparql.setReturnFormat(JSON)
resultsSingers = sparql.query().convert()
singers.append(resultsSingers)
#getting third page#
sparql.setQuery(
"""select ?singer where {?singer a yago:Singer110599806.} OFFSET 20000 LIMIT 10000""")
#aggiunti risultati in forma JSON alla lista#
sparql.setReturnFormat(JSON)
resultsSingers = sparql.query().convert()
singers.append(resultsSingers)
#4°#
sparql.setQuery(
"""select ?singer where {?singer a yago:Singer110599806.} OFFSET 30000 LIMIT 10000""")
#aggiunti risultati in forma JSON alla lista#
sparql.setReturnFormat(JSON)
resultsSingers = sparql.query().convert()
singers.append(resultsSingers)
#5°#
sparql.setQuery(
"""select ?singer where {?singer a yago:Singer110599806.} OFFSET 40000 LIMIT 10000""")
#aggiunti risultati in forma JSON alla lista#
sparql.setReturnFormat(JSON)
resultsSingers = sparql.query().convert()
singers.append(resultsSingers)

#creating list of singers (only name)#
singerNames = []
#per ogni risultato in "bindings"#
for page in singers:
    for result in page["results"]["bindings"]:
        try:
            #get stringa in "singer" in "value", dopo il divisore "/resource/"#
            cantante = result["singer"]["value"].split("/resource/")[1]
            #aggiungi stringa in lista#
            singerNames.append(cantante)
        except:
            print("",end="")

#writing file with all singers#
file = open("Singers.txt","w",encoding='utf-8')
for s in singerNames:
    file.write(s + "\n")
file.close()
