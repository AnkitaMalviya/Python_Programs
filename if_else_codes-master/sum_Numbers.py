print"enter your first number"
first=input()
print"enter your second number"
second=input()
print"enter your third number"
third=input()
if first!=second and second!=third and third!=first:
    print"sum","=",first+second+third
elif first==second :
    print first-second 
elif first==third:
    print first-third
else:
    print second-third