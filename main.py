#empty list
empty=[]
#number list
num=[1,2,34,56,52,78]
#string list
string=["john","banana","Fufu","apple"]
#mixed list
mix=[1,2,"john",True,5.6,'Last word']
print(f"empty: {empty}\nnumber list: {num}\nstring list: {string}\nmixed list: {mix}")
#accessing an element in a list
print(string[1])

empty.append("NEW ELEMENT")
print(f"append list: {empty}")

#pop
num.pop(4)
print(num)

#iterate in a list
for i in mix:
    print(i)