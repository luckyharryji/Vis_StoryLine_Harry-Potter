__author__ = 'xiangyu'


import json
import os

with open("HP_network_clean.json") as f_in:
    connection = json.load(f_in)

parse_data={}
parse_data['person']=[]
parse_data['links']=[]

for i in connection['nodes']:
    parse_data['person'].append({"id":i['id'],"name":i['label']})
parse_data['person']=sorted(parse_data['person'],key=lambda d:(d['id']))
print parse_data['person']
for i in connection['edges']:
    parse_data['links'].append({'source':int(i['source']),'target':int(i['target'])})

with open("parsed_data.json",'w') as f_out:
    f_out.write(json.dumps(parse_data))

print "end"
