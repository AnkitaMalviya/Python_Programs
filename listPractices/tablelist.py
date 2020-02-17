# user=int(input("enter your number"))
# user1=int(input("enter your number"))
# while user<=user1:
#     j=1
#     while j<=10:
#         table=j*user
#         print table
#         j=j+1
#     print"\n"
#     user=user+1

list=[3,5,6,7,8,9,1,8]
index=0
while index<len(list):
    var=1
    while var<=10:
        Table=var*list[index]
        print (Table),
        var=var+1
    print("\t")
    index=index+1   

