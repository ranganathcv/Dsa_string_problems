my_list=[1,2,3,4,5,6,7,8,9,10]
Extract_list=[]
for number in my_list:
    if number <=5 :
        Extract_list.append(number)
Reverse_list=Extract_list[: :-1]
print("Original list :",my_list)
print("Extracted first five Elements :",Extract_list)
print("Reversed extracted elements :",Reverse_list)