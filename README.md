# Python Show and Tell

## Summary

Learning involves seeing evidence and building concepts.
In other words, seeing examples and telling a story.

DBE is a collection of Python code examples. SPE is
intended to be a dialect for talking about DBE examples.

(DBE = Document By Example, SPE = Simple Python English)

## Document by example

Here's a Python code snippet. How does it work?
```python
>>> tmp = iter(range(6))
>>> list(zip(tmp, tmp))
[(0, 1), (2, 3), (4, 5)]
```

Some people can learn a lot from this example. Others might
want warm-up exercises, such as
```python
>>> tmp = range(3)
>>> list(tmp), list(tmp)
([0, 1, 2], [0, 1, 2])
```

```python
>>> tmp = iter(range(3))
>>> list(tmp), list(tmp)
([0, 1, 2], [])
```

The main purpose of **Document By Example** is to
build a collection of such examples (and exercises).

## Simple Python English

Show-and-tell involves examples and words. Shared
languages aid global communication. How best to share
with the world our DBE examples?

English is a popular second (or third) language. But 
to work, it has to be simple. Prefer common words.
Explain unusual and technical terms. And it has to be
unambiguous. 
> Close the object.

> The object is close.

Does _close_ mean _near_, or _shut_? Also, we have
the technical term _closure_. How easy is this, when
English is the reader's third language?

Sometimes, language errors can be expensive and
dangerous. Aerospace experts developed
[Simplified Technical English](https://en.wikipedia.org/wiki/Simplified_Technical_English)
for aircraft maintenance manuals.

**Simple Python English** wishes to do something 
similar, but for Python. It is the companion to
the DBE examples.
