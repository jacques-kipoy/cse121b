import sys
from termcolor import colored, cprint

cprint("Hello, World!", "green", "on_red")

#print("Hello, World!") to the terminal
print("Hello, World!")

""""""
text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)
cprint("Hello, World!", "green", "on_grey")
#####
#print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
#print_red_on_cyan("Hello, World!")
#print_red_on_cyan("Hello, Universe!")

#for i in range(10):
    #cprint(i, "magenta", end=" ")

#cprint("Attention!", "red", attrs=["bold"], file=sys.stderr)

#####

print()
###SOLUTION###

from termcolor import colored
print(colored("~~~~RAINBOW~~~~", "red"))
print(colored("~~~~RAINBOW~~~~", "yellow"))
print(colored("~~~~RAINBOW~~~~", "green"))
print(colored("~~~~RAINBOW~~~~", "cyan"))
print(colored("~~~~RAINBOW~~~~", "blue"))
print(colored("~~~~RAINBOW~~~~", "mangeta"))


print()

a = [1,2,3]
b = a
a = [4,5,6]

print(b)

