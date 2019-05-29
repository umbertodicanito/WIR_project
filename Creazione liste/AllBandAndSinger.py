from SPARQLWrapper import SPARQLWrapper, JSON
#lista di tutte la bands con i membri attuali#
bandAndMembers = []
#costruzione query#
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery(
"""select ?bandName ?member 
where{?band a dbo:Band.
?band rdfs:label ?bandName. 
?band dbo:bandMember ?member. 
?member rdf:type ?type. 
filter(?type IN (yago:Singer110599806)).
filter(lang(?bandName)="en")}  """)
#risultati aggiunti alla lista#
sparql.setReturnFormat(JSON)
resultsBandNoFormers = sparql.query().convert()
bandAndMembers.append(resultsBandNoFormers)

#risultati aggiunti alla lista#
sparql.setReturnFormat(JSON)
resultsBandNoFormers = sparql.query().convert()
bandAndMembers.append(resultsBandNoFormers)
#creating list of tuples of band and members (only name)#
bandAndMember = []
#per ogni risultato in "bindings"#
for b in bandAndMembers:
    for result in b["results"]["bindings"]:
        try:
            #get band and member name#
            band = result["bandName"]["value"]
            member = result["member"]["value"].split("/resource/")[1]
            #create tuple and attach it to the list#
            couple = (band, member)
            bandAndMember.append(couple)
        except:
            print("",end="")

file = open("BandAndSinger.txt","w",encoding='utf-8')
for c in bandAndMember:
    bandName = c[0]
    memberName = c[1]
    file.write(bandName + " -> " + memberName + "\n")
file.close()