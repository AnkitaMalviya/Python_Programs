def list_change(list1,list2):
    index=0
    while index<len(list1):
        a=list1[index]*list2[index]
        print a 
        index=index+1
multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])
