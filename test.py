import json
with open ('data.json', "r") as f:
    data = json.load(f)
print(data)
a = data[0]
b = data[1]
c = data[2]
d = data[3]
e = data[4]
f = data[5]
g = data[6]
print(a,b,c,d,e,f,g)
a = 0
b = 0
c = 0
newData = [a,b,c,d,e,f,g]

