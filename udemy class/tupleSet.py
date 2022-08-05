#Tupple:is an immutabe data set which means it cant be changed
my_tupple = (1,2,2,2,2,1,1,3,4,5)
#it has two methods count and index and it cant be sorted
x = my_tupple.count(2)

y = my_tupple.index(2) 
#print(y)

#set:is an unordered colection of unique object or values
# my_set = {1,1,2,3,4,7,2,3,8,6,5,10}
# your_set = {2,7,3,4,5,6,2,3,1,1,4,5,8,11}
# my_set.add(100)
# my_set.add(1)#this wont get added because the set numbers are unique
# new_set = my_set.copy()
# #my_set.clear()
# #print(my_set)

# my_list = [1,3,4,2,5,3,2,3,5,6,3,5,4,2]
#print(set(my_list))#set as a function
#print(len(my_set))#len as a function

#to check if something is in the memory you cant use indexing
#print(new_set)
#print(list(new_set))
#print(3 in my_set)# cant use print(my_set[0])

#method of SETS
#.difference
#print(my_set.difference(new_set))

#.discard
#print(your_set.discard(1))#it has been modified
#print(your_set)

#.difference_update
# print(my_set.difference_update(your_set))#it has been modified so you need to print the main set again
# print(my_set)

# #intersection
# print(my_set.intersection(your_set))# short hand intersection is &

# #isdisjoint
# print(my_set.isdisjoint(your_set))

# #union
# print(my_set | (your_set))# short hand for union is |


my_set1 = {4,5}
your_set1 = {1,2,3,4,5}
#issubset
print(my_set1.issubset(your_set1))

#issuperset
print(my_set1.issuperset(your_set1))