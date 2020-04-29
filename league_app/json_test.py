import json
from urllib.request import urlopen

with urlopen("http://ddragon.leagueoflegends.com/cdn/10.9.1/data/en_US/champion.json") as response:
    source = response.read()


data = json.loads(source)
keys = data.keys()
# dictionary
champdict = data.get('data')
champvals = champdict.values()
# print(champvals)

# champvals_keys = champvals.keys()
# print(len(champvals)) 148 champions

for values in champdict.values():
    print (values['id'])

# for i in champvals:
#     print(i['title'])


# dictionary keys
champkeys = champdict.keys()
# print(type(champkeys))

# print(type(champdict))




# def champions(x):
#     champs = []
#     for k in x:
#         print (k)

# champions(champkeys)

# print(json.dumps(data, indent=2))
# print(type(data))

# for key, value in data.items():
#     print (f' this is the key{key} this is the value {value}')

# for key in data.items():
#     print(key)



# this is the key type this is the value champion
# this is the key format this is the value standAloneComplex
# this is the key version this is the value 10.9.1

# {"type":"champion","format":"standAloneComplex","version":"10.9.1","data":{"Aatrox":{"version":"10.9.1","id":"Aatrox","key":"266","name":"Aatrox","title":"the Darkin Blade","blurb":"Once honored defenders of Shurima against the Void, Aatrox and his brethren would eventually become an even greater threat to Runeterra, and were defeated only by cunning mortal sorcery. But after centuries of imprisonment, Aatrox was the first to find...","info":{"attack":8,"defense":4,"magic":3,"difficulty":4},"image":{"full":"Aatrox.png","sprite":"champion0.png","group":"champion","x":0,"y":0,"w":48,"h":48},"tags":["Fighter","Tank"],"partype":"Blood Well","stats":{"hp":580,"hpperlevel":90,"mp":0,"mpperlevel":0,"movespeed":345,"armor":38,"armorperlevel":3.25,"spellblock":32.1,"spellblockperlevel":1.25,"attackrange":175,"hpregen":3,"hpregenperlevel":1,"mpregen":0,"mpregenperlevel":0,"crit":0,"critperlevel":0,"attackdamage":60,"attackdamageperlevel":5,"attackspeedperlevel":2.5,"attackspeed":0.651}}
