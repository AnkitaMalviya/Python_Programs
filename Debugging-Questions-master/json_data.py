{
    "users": [{
            "firstName": "vidur",
            "lastName": "singla",
            "details": {
                "age": 21,
                "mobileNo": 1234567890,
                "City": "Delhi"
            }
        },
        {
            "firstName": "rishabh",
            "lastName": "verma",
            "details": {
                "age": 22,
                "mobileNo": 12345678320,
                "City": "Chandigarh"
            }
        },
        {
            "firstName": "abhishek",
            "lastName": "gupta",
            "details": {
                "age": 25,
                "mobileNo": 12332567890,
                "City": "Gurgaon"
            }
        }
    ]
}

import json 
data_file=open("users.json","r") 
data = json.load(data_file)
print data
users1 = data["users"]
print users1
counter=0
while counter<len(users1):
    print ("users full name is " + users1[counter]['firstName'] + ' ' + users1[counter]['lastName'])
    print ("users mobile number is " + str(users1[counter]['details']['mobileNo']))
    print ("users age is"+str(users1[counter]['details']['age']))
    print ("users City"+(users1[counter]['details']['City']))
    counter=counter+1 