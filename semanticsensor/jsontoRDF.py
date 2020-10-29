import json
import rdflib

with open("microeco.json","rb") as jsonfile:
    data=json.load(jsonfile)
gg=rdflib.Graph()

for i in range(0,len(data)):
    txt=data[i]
    try:
        s=rdflib.URIRef('http://www.openkg.cn/dataset/microeconomy/' + txt['subject'])
        p=rdflib.URIRef('http://www.openkg.cn/dataset/microeconomy/'+txt['relation'])
        o=rdflib.URIRef('http://www.openkg.cn/dataset/microeconomy/'+txt['object'])
        gg.add((s,p,o))
    except Exception as e:
        pass
gg.serialize('data.rdf')

jsonfile.close()