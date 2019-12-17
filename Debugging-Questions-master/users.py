import json
data_file=open("users.json","r")
data = json.load(data_file)
print data
print type(data)
# users = data["users"]
# print users
# counter=0
# while counter<len(users):
#     print ("users full name is " + users[counter]['firstName'] + ' ' + users[counter]['lastName'])
#     print ("users mobile number is " + str(users[counter]['details']['mobileNo']))
#     print ("users age  is " + str(users[counter]['details']['age']))
#     print ("users city is " + users[counter]['details']['City'])
#     counter=counter+1  