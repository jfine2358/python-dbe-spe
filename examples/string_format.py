
"""
>>> print("Hello world, My name is {} and your name is {}. His name is {}".format("Ryan", "Bruce", "Dave"))
Hello world, My name is Ryan and your name is Bruce. His name is Dave

print("Hello world, My name is {0} and your name is {1}. His name is {2}".format("Ryan", "Bruce", "Dave"))
Hello world, My name is Ryan and your name is Bruce. His name is Dave

print("Hello world, My name is {2} and your name is {0}. His name is {1}".format("Ryan", "Bruce", "Dave"))
Hello world, My name is Dave and your name is Ryan. His name is Bruce

print("Hello world, My name is {2} and your name is {1}. His name is {}".format("Ryan", "Bruce", "Dave"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: cannot switch from manual field specification to automatic field numbering

>>> print("The value of pi is {0:.3f}".format(3.14159)) 
The value of pi is 3.142
>>> print("The value of pi is {0:.7f}".format(3.14159))
The value of pi is 3.1415900

>>> from datetime import datetime
>>> today = datetime.now()
>>> print("The date today is {:%B %d, %Y}" .format(today))
The date today is September 19, 2018

>>> print("Hello world, My name is {} and your name is {}. His name is {}".format(*list))
Hello world, My name is Ryan and your name is Bruce. His name is Dave

>>> my_dict = {'Alice': 'December', 'Jack': 'February'}
>>> print('Alice was born in {Alice}, while Jack was born in {Jack}'.format(*my_dict))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Alice'
>>> print('Alice was born in {Alice}, while Jack was born in {Jack}'.format(**my_dict))
Alice was born in December, while Jack was born in February



"""







if __name__ == '__main__':
    import doctest
    print(doctest.testmod())