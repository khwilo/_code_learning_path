# Importing each function
import pizza

# Importing specific functions
from pizza import make_pizzas

# Making an alias of a function name
from pizza import make_pizzas as mp

# Giving a module an alias
import pizza as p

# Importing all functions in a module
# Using this approach you can call each function name
# without using the dot notation.
from pizza import *
pizza.make_pizza('pepperoni')
pizza.make_pizza('mushrooms', 'green peppers', 'extra cheese')

make_pizzas(16, 'pepperoni')
make_pizzas(12, 'mushrooms', 'green peppers', 'extra cheese')

print("\n---An alias of a function---")
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

print("\n---An alias of a module---")
p.make_pizza('pepperoni')
p.make_pizza('mushroons', 'green peppers', 'extra cheese')
