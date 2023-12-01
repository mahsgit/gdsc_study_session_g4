# sum of all positive numbers
num_list=[]
sum=0
while True:
    nums=input("enter list of numbers or enter x when u finish")
    if nums=='x':
         break
    nums=int(nums)
    num_list.append(nums)
print(f"num of list you ented {num_list}")
for i in num_list:
    if i>0:
        sum+=i
print(f"total sum of positive numbers are {sum}")









