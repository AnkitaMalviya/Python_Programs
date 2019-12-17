print"shasha travels pvt.ltd"
print"enter your ticket charges"
ticket_charges=input()
if ticket_charges>70000:
    discount=ticket_charges*18/100
    print"discount","=",discount
    netamount=ticket_charges-discount
    print"netamount","=",netamount
elif ticket_charges>=55001 and ticket_charges<=70000:
    discount=ticket_charges*16/100
    print"discount","=",discount
    netamount=ticket_charges-discount
    print"netamount","=",netamount
elif ticket_charges>=35001 and ticket_charges<=55000:
     discount=ticket_charges*12/100
     print"discount","=",discount
     netamount=ticket_charges-discount
     print"netamount","=",netamount
elif ticket_charges>=25001 and ticket_charges<=35000:
    discount=ticket_charges*10/100
    print"discount","=",discount
    netamount=ticket_charges-discount
    print"netamount","=",netamount
elif ticket_charges<25001:
    discount=ticket_charges*2/100
    print"discount","=",discount
    netamount=ticket_charges-discount
    print"netamount","=",netamount
