print"\t festival discount"
print"enter your cost"
user=input()
if user<2000:
    discount=user*5/100
    print"discount","=",discount
    totalcost=user-discount
    print"paidamount","=",totalcost
elif user>=2001 and user<=5000:
    discount=user*25/100
    print"discount","=",discount
    totalcost=user-discount
    print"paidamount","=",totalcost
elif user>=5001 and user<=10000:
    discount=user*35/100
    print"discount","=",discount
    totalcost=user-discount
    print"paidamount","=",totalcost
elif user>10000:
    discount=user*50/100
    print"discount","=",discount
    totalcost=user-discount
    print"paidamount","=",totalcost
print"------------------"  