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

## Instructions for novices to contribute

1. **Install** Python 3

Follow the instructions here https://www.python.org/downloads/

2. **Create** a Github account if you don't already have one

https://github.com/join?source=header-home

3. **Fork** the repo on GitHub

Fork this repo by clicking on the fork button on the top of the page. This will create a copy of this repository in your account.
 
4. **Clone** the project to your own machine. 

Open a terminal and run the following git command:

```
git clone "https://github.com/username/python-show-and-tell.git"
```

where you need to replace "username" in the url above with your github username

5. Add links to your remote repositories: your forked repo and the original repository

```
  git remote add origin "https://github.com/username/python-show-and-tell.git"

  git remote add upstream "https://github.com/jfine2358/python-show-and-tell.git"
```

This is a way of telling git that other versions of this project exists in the specified urls and we’re calling the forked version ```origin``` and original repo ```upstream``` respectively

6. **Create** a new branch and checkout into that branch

```
cd first-contributions
git checkout -b <add-branch-name>
```

7. Make necessary changes and **Commit** those changes

```

git add Contributors.md

git commit -m "Add <your-name> to Contributors list"
```

8. **Push** your work back up to your fork

```
 git push origin <add-your-name>
```

9. Submit a **Pull request** so that we can review your changes

If you go to your repository on GitHub, you’ll see a Compare & pull request button. 
Click on that button and Create Pull Request.

NOTE: Be sure to merge the latest from "upstream" before making a pull request!

```git pull upstream <your branch name>```

10. Keeping your fork synced with this repository

* First, switch to the master branch.

```git checkout master```

* Fetch and merge the new version of my repository after pull request is merged:

```git fetch upstream```

Here we’re fetching all the changes in my fork (upstream remote). 
Now, you need to merge the new revision of my repository into your master branch.

```git merge upstream/master```

* Push the master branch now, your fork will also have the changes:

```git push origin master```

