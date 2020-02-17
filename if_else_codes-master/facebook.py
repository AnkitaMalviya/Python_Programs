ID="nehaisrani"
Password=123456789
user_input=raw_input("enter your id")
user_input1=input("enter your password")
if user_input==ID and user_input1==Password:
    print"login sucessfully"
elif user_input!=ID and user_input1!=Password:
    print"Error"
elif user_input==ID or user_input1!=Password:
    print"check password"
elif user_input!=ID or user_input==Password:
    print"check id"