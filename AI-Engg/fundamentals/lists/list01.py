#  List:- Lists are used to store multiple items in a single variable.

thislist = ["apple", "banana", "cherry"]
print(thislist)

# list item are ordered, changeable, and allow duplicate values.
# list can also contain different data types.




# access list
fruits = ["apple", "banana", "mango"]

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # mango (last item)




# changing in a list
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits)
# ['apple', 'orange', 'mango']





# len method
fruits = ["apple", "banana", "mango"]
print(len(fruits))  # 3



# list() Constructor
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)  # ['apple', 'banana', 'cherry']
