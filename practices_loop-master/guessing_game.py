guess_num=5
index=1
print"enter number 1 to 10"
while index<=10:
    user=input()
    if index==10:
        if user==guess_num:
            print"wahh! guess kar liya"
        else:
            print"chances finish user ne guess hi nahi kiya"
    elif user==guess_num:
        print"wahh!guess kar liya"
        break
    elif user>5:
        print"apka number bada hai"
    elif user<5:
        print"aapka number chota hai"
    index=index+1

