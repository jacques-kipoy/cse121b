var = 1
#The following conditions are pairwise equivalent:
# print(var > 0)
# print(not(var<=0))
""""""""""""""""""""""""""""""""""""""""""""""""""""""
# print()
# The following conditions are pairwise equivalent:
# print(var != 0)
# print(not(var==0))
""""""""""""""""""""""""""""""""""""""""""""""""""""""
# You may be familiar with De Morgan's laws. They say that:
# The negation of a conjunction is the disjunction of the negations.
# The negation of a disjunction is the conjunction of the negations.
# print()
# p = 1
# q = 1
# n= not (p and q) == (not p) or (not q)  # not can also be writen as op=
# m= not (p or q) == (not p) and (not p)
# print(n,m)
""""""""""""""""""""""""""""""""""""""""""""""""
#Logical values vs. single bits
# i = 1
# j = not not i
# print(j)
""""""""""""""""""""""""""""""""""""""""""""""""
#Bitwise operators
# & (ampersand) ‒ bitwise conjunction;
# | (bar) ‒ bitwise disjunction;
# ~ (tilde) ‒ bitwise negation;
# ^ (caret) ‒ bitwise exclusive or (xor).
# a = 0
# b = 1
# print(a|b)
# print(a & b)
# print(a^b)
""""""""""""""""""""""""""""""""""""""""""""""""
i = 15
j = 14
log = i and j
print(log)
