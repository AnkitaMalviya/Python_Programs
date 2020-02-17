book={"name":
[{"neha":"ekta",
"surname":"israni"},
# "title":
{"bfjgusdkg":"jusgvgfv",
"surname":"huisgi",
"vggsavjsh":"dfyuerw"}]
}
print (len(book))
j=0
for i in book:
   print (book [i][j]["surname"])
   j=j+1



# here it will be print only values because dictionary inside the list
book={"name":
[{"neha":"ekta",
"surname":"israni"}],
"title":
[{"neha":"jusgvgfv",
"vysudvfsuf":"huisgi",
"vggsavjsh":"dfyuerw"}]
}
print len(book)
for i in book:
    print book[i][0]["neha"]


#here it will be print only values because here is not list between the dictionary
book={"name":
{"neha":"ekta",
"zeba":"kajal"},
"surname":
{"neha":"jusgvgfv",
"zeba":"dfyuerw"}
}
print (len(book))

for i in book:
   print (book[i]["neha"])