def list_change(list1,list2):
    index=0   
    new=[]   
    while index<len(list1):
        sec_index=0
        var=0
        while sec_index<list2[index]:
            var=list1[index]+var
            sec_index=sec_index+1
        new.append(var)
        index=index+1
    print new
list_change([5, 10, 50, 20], [2, 20, 3, 5])

# def multiplication(number1,number2):
#     num=1
#     multiple=0
#     while (num<=number1):
#         multiple=multiple+number2
#         num=num+1
#     return multiple
# list1=[5, 10, 50, 20]
# list2=[2, 20, 3, 5]
# new_list=[]
# index=0
# while index<len(list1):
#     multiple=multiplication(list1[index],list2[index])
#     new_list.append(multiple)
#     index=index+1
# print new_list
