Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello")
Hello
print('Hello')
Hello
a="Hello"
print(a)
Hello
a="""lorem okjruigfojvovngbhirjvaokv
iufheioguoijvojvevjuidsiokvdiug9tug
oeiug9ew8ugeiwjgwe98grewfefjvejegio
... eoiugew09iew0v9iw=-t09g-w90geufifdi"""
>>> print
<built-in function print>
>>> print(a)
lorem okjruigfojvovngbhirjvaokv
iufheioguoijvojvevjuidsiokvdiug9tug
oeiug9ew8ugeiwjgwe98grewfefjvejegio
eoiugew09iew0v9iw=-t09g-w90geufifdi
>>> #strings are array
>>> a="HELLO, WORLD"
>>> print(a[1])
E
>>> for x in "banana"
SyntaxError: incomplete input
>>> for x in "banana":
...     print(x)
... 
...     
b
a
n
a
n
a
>>> a="Hello, World!"
>>> print(len(a))
13
>>> txt = "The best things in life are free!"
>>> print("free" in txt)
True
>>> txt = "The best things in life are free!"
>>> if "free" in txt:
...     print("Yes, 'free' is present.")
... 
...     
Yes, 'free' is present.
>>> txt = "The best things in life are free!"
>>> print("expensive" not in txt)
True
