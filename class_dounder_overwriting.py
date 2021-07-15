# In this example class will use + and performe minus operation. __add__ is mapped to + by python language definiton
# but ones inside we will instruct py. to perform substraction operation

# Again if you dont code overwrite dounder or you dont inherit one your class simple doesn`t support that operation

class Ilija:
    def __init__(self, name, last):
        self.name = name
        self.last = last
        
    def __add__(self, other):
        return self.name - other
    
ok
2 + 2
0

# Second example indexing:
# When and instance X appears in an indexing expression like X[i] python calls __getitem__ method inherited by 
# instance passing X as first argument and index in brackets as second

a = [1,2,3,4]
a[3] # under the hood py. is calling __getitem__ method passing a var. on place of first argument and 3 as second

# same method __getitems__ is also used for slicing 
a = [1,2,3,4,5]
a[:3]

x = [1,2,3,4]
x.__getitem__(1)

# Now let`s twik it. Overvrite __getitem__ dounder, and ajust to our specific need: squer every number from cliced part of list 
class Indexer:
    def __init__(self, name):
        self.name = name
        
    def __getitem__(self, index):
        for x in self.name[index]:
            print (x ** 2)
        
    
a = Indexer([2,3,4,5,6,7,8,9,10])
a[:10]

4
9
16
25
36
49
64
81
100

# one intresting corner case
# we can check just index from instance attribut
            
a = Indexer('Ilija petroniejvic')
a.name[:8]

# in this case py. use unchanged __getitem__ and apply to str instead of using custom class version of __getitem__. Most probbaly because it comes from str. class itself
# same case if we use 

class Indexer:
    def __init__(self, name):
        self.name = name[:4]
        
# Here we have same case __getitem__ is native paython version without our modification. Our version of __getiter__ will act upon just class general not to when it is call 
# __getitem__ from specific instance attribute

# In this case on other hand  we did`t give at all __getitem__method to our class but it inherite from list general 


class Indexer:
    def __init__(self, name):
        self.name = name

               
a = Indexer([1,2,3,4,5,6,7,7])
a.name[:4]
>>> [1,2,3,4,5]
