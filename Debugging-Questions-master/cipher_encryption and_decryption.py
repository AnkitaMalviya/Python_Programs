list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
print len(list)
print"enter your e and d"
user=raw_input()
print("kitne se incrypet and decript karna hai")
user_input=input()
if user=="e":
    print"enter your alphabet"
    user1=raw_input()
    index=0
    while index<len(user1):
        j=0
        while j<len(list):
            if user1[index]==list[j]:
                j=j+user_input
                print list[j]
            j=j+1
        index=index+1 
else:
    print"enter your alphabet"
    user1=raw_input()
    index=0
    while index<len(user1):
        j=0
        while j<len(list):
            if user1[index]==list[j]:
                j=j-user_input
                print list[j]
                break
            j=j+1
        index=index+1
        


