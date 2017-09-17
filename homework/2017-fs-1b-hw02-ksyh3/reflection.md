Homework 2 - Python 
=========================
I thoroughly enjoy the way that Python implements list / dictionary iteration
with respect to how it looks in the code. Personally, I think the `for in`
segments look extremely clean (even though I tend to abuse their usage quiet a
lot). Just a little tangent. But, I thought that this assignment was fairly easy
as I have used Python for about a year now on various internship / ACM things. I
did find using pytest initially a little difficult as I tend to stray towards
the vanilla unittest python testing library. However, I definitely enjoyed using
pytest and its overall look, and I definitely think I will use it for future
projects.

A challenge I did face was I attempted to be a little to fancy with my tests for
the `mood()` function. I tried to use the `itertools` library to create every
possible combination of the left and right offset, but in the implementation it
sometimes returned an empty list for the test. I solved this problem by just
scrapping it and doing some static tests of specific, known lists.
