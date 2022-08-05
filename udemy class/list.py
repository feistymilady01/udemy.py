#All about List
#List
#amazon_of_array =[1,1.2,'a',True]
#print(amazon_of_array[2])


#list slicing
# shopping_cart = ['biro', 'perfumes','grapes','motor', 'cards', 'pigs']
# shopping_cart[3] = 23456
# new_cart = shopping_cart
# new_cart[3] = 'sing'
# #new_carts = shopping_cart[0:2] #this is giving error because it is only being modified not being stored
# print(shopping_cart[::2])#stepping over two places
# print(shopping_cart[0:4])
# print(shopping_cart)

#Matix 2 by 2
# shoping1 = [
#     [0,1,0],
#     [1,0,1],
#     [0,1,0],
#     ]
# print(shoping1[1][2])

#list Method
#shopping2 = ['biro', 'perfumes','grapes','motor', 'cards', 'pigs']

#add [append:adding to the end list of array,insert(2,"ade"):takes both the index and value,extend([])]
#shopping2.extend(['pencil',12345,'inking'])
#print(shopping2)

#remove [pop:is to remove the las item in the array,remove:takes the specific value in the array,clear] 
#shopping2.pop()
#shopping2.clear()
#print(shopping2)

#keywords: they are words that are built in python
#cart1 = ['c','d','f','t','e','r','p','t','s','r','e','r']
#print(shopping2.index('pigs',4,7))
#print(shopping2.count('cards'))
#print(shopping2.sort())#it cant be modified or returned meaning:it cant create a new set of variable
#cart1.sort()
#print(cart1)
#print('d' in cart1)#keyward in
#print('o' in 'ketchup')
#print(sorted(cart1))
#cart1.reverse()
#print(cart1)

#Sorted is a function and sort is a method but they give the same result
#basket = ['c','d','f','t','e','r','p','t','s','r','e','r','a']
#print(sorted(basket))
#using sort and list slicing
# new_item = basket[:]#which you can also use .copy()
# new_item.sort()
# print(new_item)

#common list pattern(len,list slicing)
#print(len(basket))
#print(basket[::-1])# also used for reversing like reverse method without sorting

#Range
#print(list(range(1,100)))

#join is a string method
# word = ' '
# #word.join(['hello','my', 'name', 'is','ade'])#this is not possible because 
# #it has to be stored in a new variable to be red
# new_word = word.join(['hello','my', 'name', 'is','ade'])
# print(new_word)

#list unpacking
a,b,c, *other,d = ['hello','my', 'name', 'is','ade','hate','school']

print(a)
print(b)
print(c)
print(other)
print(d)
