from SPARQLWrapper import SPARQLWrapper, JSON
#lista vuota per visualizzare i risultati#
writers=[]
#costruzione query#
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT *
    WHERE {
    ?writer a
    <http://dbpedia.org/ontology/Writer> .
    ?writer <http://dbpedia.org/ontology/influenced> ?hasInfluenced.
    } 
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
writers.append(results)

import networkx as nx
import matplotlib.pyplot as plt
import operator

G = nx.DiGraph()

for result in results["results"]["bindings"]:
    try:
        scrittore = result["writer"]["value"].split("/resource/")[1]
        influenzato = result["hasInfluenced"]["value"].split("/resource/")[1]
        
        #print(result["writer"]["value"])
        #print(result["influenced"]["value"])
        #print("_____________________________________")
    
        #print("(" + scrittore + "," + influenzato + ")")
        G.add_edge(influenzato, scrittore)


    except:
        print("",end="")

'''
val_map = {'A': 1.0,
           'D': 0.5714285714285714,
           'H': 0.0}
values = [val_map.get(node, 0.25) for node in G.nodes()]
nx.draw(G, cmap=plt.get_cmap('jet'), node_color=values)
plt.show()
'''

pr = nx.pagerank(G, alpha=0.85)
sorted_pr = sorted(pr.items(), key=operator.itemgetter(1))
sorted_pr.reverse()


for i in sorted_pr:
    #print(i + " " + str(pr.get(i)))
    print(i)