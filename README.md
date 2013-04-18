pysandbox
=========

sqrt.py:
---------

Implemented the square root function using Newton's method.
To compute the square root, it finds roots of f(x) = x^2 - n by iterations. The derivative of f(x) is f'(x) = 2x.
The initial guess, x0 is the average/mid-value of the number. The subsqeuent iterations are obtained by evaluating at previous iteration: x1 = x0 - f(x0)/f'(x0), so on and so forth until the desired accuracy has been achieved. The default accuracy here is 10^-5

Usage: ```python sqrt.py <number>```
