water=raw_input("enter your quantity")
water=int(water)
if water<1L:
    print"pani bharna hai"
elif water>1L and water <10L:
    print"aur nahi bharna"
elif water>10L:
    print"pani overflow ho raha hai"