'''Dictionaries are used to
store data values in key:value pairs.

A dictionary is a collection which is ordered*,
changeable and do not allow duplicates.'''

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print( thisdict )

'''Dictionary Items:
Dictionary items are ordered, changeable,
and does not allow duplicates.
Dictionary items are presented in key:value pairs,
and can be referred to by using the key name.'''
print( thisdict["brand"] )
print( len( thisdict ) )
print(type ( thisdict ))

'''The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary.'''
Dict = dict( name = "John" , age = "20" , country = "Norway")
print( Dict )

#Accessing Items
x= thisdict["year"]
print( x )
x = thisdict.get("year")
print( x )

#access the keys
x= thisdict.keys()
print( x )

thisdict["model"] = "Mustang"
print( thisdict )
print( thisdict.keys())

#Get values use values()
y = ( thisdict.values() )
thisdict["year"] = 2002
print(y)

#get items
x= thisdict.items()
print(x)
if "model" in thisdict:
  print ("Yes,model is one of the keys in the thisdict dictionary")

#update dictionary
thisdict.update({"year" : 2020})
print( thisdict )

#remove a item from dictionary
#thisdict.pop("model")
del thisdict["model"]
print( thisdict )
''''The popitem() method removes the last inserted item (in versions before 3.7,
 a random item is removed instead):'''
thisdict.popitem()
print( thisdict )

thisdict.clear()
print(thisdict)
