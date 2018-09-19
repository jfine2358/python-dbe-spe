"""
>>> fahr = 212
>>> cent = (fahr - 32) * 5 / 9
>>> cent
100.0

>>> fahr = 32
>>> cent = (fahr - 32) * 5 / 9
>>> cent
0.0

>>> def cent_from_fahr(fahr):
...     cent = (fahr - 32) * 5 / 9
...     return cent

>>> cent_from_fahr(212)
100.0
>>> cent_from_fahr(32)
0.0

>>> anon = lambda fahr: (fahr - 32) * 5 / 9
>>> anon(32)
0.0
>>> anon(212)
100.0

>>> anon
<function <lambda> at 0x1080b0620>
>>> cent_from_fahr
<function cent_from_fahr at 0x10803be18>


"""




if __name__ == '__main__':
    import doctest
    print(doctest.testmod())