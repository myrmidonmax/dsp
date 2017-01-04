# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

**Both are sequences of values. Those can be of different types. List are mutable whereas tuples are immutable meaning that individual items cannot be changed. Since tuples are immutable they can serve as keys in dictionaries, lists cannot.**

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

**Both are a sequence of values. Lists are ordered, while sets are not. Lists can containt duplicates while sets only contain distinct hashable objects. The performance is better for sets as the are hashable. They can be searched much faster.**

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

**Like def, `lambda` is a way to create function (objects). It is applied to functions that are very simple or only applied once. It is defined just in the place where it is used and is not assigned a name. Lambda has to contain an expression.**
```python
sorted(list_of_tuples, key = lambda dummy: dummy[2]) # sort by 3rd list item
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

**937 days**

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

**513 days**

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

**7850 days**

Place code in this file: [q5_datetime.py](python/q5_datetime.py)
**Done**

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)
**Done**

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

**Done**


---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





