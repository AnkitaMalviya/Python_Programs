print"enter your type laptop and desktop"
type=raw_input()
print"enter your amount"
amount =input()
if type=="L":
    if amount>=0 and amount<=25000:
        discount=amount*0.0/100
        print"discount","=",discount
        netamount=amount-discount
        print"net-amount","=",netamount
    elif amount>=25001 and amount<=57000:
        discount=amount*5.0/100
        print"discount","=",discount
        netamount=amount-discount
        print"net-amount","=",netamount
    elif amount>57000 and amount<=100000:
        discount=amount*7.5/100
        print"discount","=",discount
        netamount=amount-discount
        print"net-amount","=",netamount
    elif amount>100000:
        discount=amount*10.0/100
        print"discount","=",discount
        netamount=amount-discount
        print"net-amount","=",netamount


