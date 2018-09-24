
"""
>>> "{} and his son {}, adopted a dog called {}".format("Mark", "David", "Michael")
'Mark and his son David, adopted a dog called Michael'

>>> "{0} and his son {1}, adopted a dog called {2}".format("Mark", "David", "Michael")
'Mark and his son David, adopted a dog called Michael'

>>> "{2} and his son {0}, adopted a dog called {1}".format("Mark", "David", "Michael")
'Michael and his son Mark, adopted a dog called David'

>>> "{0} and his son {1}, adopted a dog called {}".format("Mark", "David", "Michael")
Exception raised:
      File "<doctest string_format[3]>", line 1, in <module>
        "{0} and his son {1}, adopted a dog called {}".format("Mark", "David", "Michael")
    ValueError: cannot switch from manual field specification to automatic field numbering

>>> "{} and his son {1}, adopted a dog called {2}".format("Mark", "David", "Michael")
Exception raised:
       File "<doctest string_format[4]>", line 1, in <module>
        "{} and his son {1}, adopted a dog called {2}".format("Mark", "David", "Michael")
    ValueError: cannot switch from automatic field numbering to manual field specification

>>> "The value of pi is {0:.3f}".format(3.14159)
'The value of pi is 3.142'
>>> "The value of pi is {0:.7f}".format(3.14159)
'The value of pi is 3.1415900'

>>> from datetime import date
>>> date_ = date(2018, 6, 10)
>>> "The date is {:%B %d, %Y}" .format(date_)
'The date is June 10, 2018'

>>> 'The coordinates of this location are: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
'The coordinates of this location are: 37.24N, -115.81W'

>>> fruit_quantity = (3, 5)
>>> 'apples: {0[0]};  oranges: {0[1]}'.format(fruit_quantity)
'apples: 3;  oranges: 5'

>>> birth = {'Alice_month': 'December', 'Jack_month': 'February'}
>>> 'Alice was born in {Alice_month}, while Jack was born in {Jack_month}'.format(*birth)
Exception raised:
File "<doctest string_format[10]>", line 1, in <module>
        'Alice was born in {Alice_month}, while Jack was born in {Jack_month}'.format(*birth)
    KeyError: 'Alice_month'
>>> 'Alice was born in {Alice_month}, while Jack was born in {Jack_month}'.format(**birth)
'Alice was born in December, while Jack was born in February'


"""






if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
