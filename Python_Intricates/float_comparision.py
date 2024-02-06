if 0.1+0.1==0.2:
    print("0.1+0.1 is 0.2")

if 0.1+0.1+0.1==0.3:
    print("0.1+0.1+0.1 is 0.3")
else:
    print("0.1+0.2!=0.3 because python evaluates floating points as x dicided by 2 powerx  ")


#     GitHub Copilot
# This behavior is due to the way floating point numbers are represented in computer systems. 
# Computers use binary (base 2) number system, while humans use decimal (base 10) system.

# When you write 0.1 in your source code, Python automatically translates this to an exact binary 
# fraction which is close to, but not exactly equal to, 0.1. It's actually a bit more than 0.1. 
# Similarly, Python translates 0.2 into a binary fraction slightly more than 0.2,
#  and 0.3 into a binary fraction slightly less than 0.3.

# So, when you add 0.1 + 0.1 in Python, the result is slightly more than 0.2, but when compared to 0.2 
# (which is also slightly more than 0.2), 
# they are close enough to be considered equal, hence 0.1 + 0.1 == 0.2 is True.

# However, when you add 0.1 + 0.1 + 0.1, the result is slightly more than 0.3. But when compared to 0.3
#  (which is slightly less than 0.3), they are not close enough to be considered equal,
#  hence 0.1 + 0.1 + 0.1 == 0.3 is False.

# This is a common issue in all languages that use IEEE 754 floating point numbers 
# (which is nearly all of them), not just Python. To handle this, you should use a tool 
# suited for the job such as decimal module in Python or be careful with equality comparisons of floating point numbers.