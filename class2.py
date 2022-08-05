#Mutable and immutable variable
#1.mutable object can be changed or modified without affecting its content,
# object refernce or memory addres e.g list and dictionary
a=[1,12,21,33,21]
b = a
b[0]=333
print(a is b)
print(a)

#2. immutable objects can not ba changed e.g are list, float,strings,integers

#Dictionary: storing stings with a value e.g{"joe":20, "sade":10} it cant be added or concatinated like list.

> a=[1,12,21,33,21]
b = a
b[0]=333
>>> a=[1,12,21,33,21]
>>> b = a
>>> b[0]= 456
>>> d
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> b
[456, 12, 21, 33, 21]
>>> a
[456, 12, 21, 33, 21]
>>> a is b
True
>>> [2,3,4] + [5,6,7]
[2, 3, 4, 5, 6, 7]
>>> {"joe":10,"sam":21,"ali":3}
{'joe': 10, 'sam': 21, 'ali': 3}
>>> noTwo = "Two"
>>> noTwo[0:2]
'Tw'
>>> "Hello world"*5
'Hello worldHello worldHello worldHello worldHello world'