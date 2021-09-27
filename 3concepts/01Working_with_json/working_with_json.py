#JSON(Javascript Object Notation)
#We commonly use json format to transfer data between web application and server.

#In python, JSON exists as a string, for example:
p='{"name":"yash", "languages":["python","java"]}'
#or as a JSON object in a file.

import json
#parsing JSON in python

#parsing JSON string:
person='{"name":"yash", "languages":["English","French"]}'
person_dict=json.loads(person)
print(person_dict)

#python reading json file:
