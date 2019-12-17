print("enter your password")
user=raw_input()
if len(user)>=6 and len(user)<=16:
    if "$" in user:
        if "2" in user or "8" in user:
            if  "A" in user or "Z" in user:
                print"strong password"
            else:
                print"weak password"
        else:
            print"weak password"
    else:
        print"weak password"
else:
    print"weak password"



