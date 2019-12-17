# taking input from user and that element present in list then pring yes
list1=[1,2,3,4,5,6,7,8,9,10]
user=input("enter your number")
list=map(int,str(user))
print"list",list
index=0
while index<len(list):
    if list[index] in list1:
        a=("yes")
    index=index+1
print a



#with function
def i(n):
    list=map(int,str(n))
    print (list)
user=input("enter your number")
i(user)


#with string

list=["a","b","c","d","e","f","g","h"]
user=raw_input("enter your string")
i=0
while i<len(user):
    if user[i] in list:
        print"yes"
    else:
        print"no"
    i=i+1