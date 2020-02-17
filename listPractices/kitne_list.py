kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# i=0
# count=0
# counter=0
# Total=0
# while i<len(kitna_paisa_hai):
#     if kitna_paisa_hai[i]>=10000000:
#         count=count+1
#     elif kitna_paisa_hai[i]>=100000:
#         counter=counter+1
#     else:
#         Total=Total+1
#     i=i+1
# print count 
# print counter
# print Total

i=0
count=0
counter=0
Total=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        print"crorepati",kitna_paisa_hai[i]
        count=count+1
    elif kitna_paisa_hai[i]<=100000:
        print"lakhpati",kitna_paisa_hai[i]
        counter=counter+1
    else:
        print"dilwale",kitna_paisa_hai[i]
        Total=Total+1
    i=i+1
print count
print counter
print Total