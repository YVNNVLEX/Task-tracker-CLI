import json

# f = open('listeTask.json','r')
# convertfile = json.load(f)
# for task in convertfile:
#     if task['id'] == 'in-progress':
#         done.append(task)
#     else:
#         continue

name = "bonjour chien"
args = name.split()
for arg in args:
    arg1 = args[0]
    arg2 = args[1]

print(f"arg1: {arg1} && arg2:{arg2}")
print(len(arg1))

# toto = "bonjour"
# print(toto[2])