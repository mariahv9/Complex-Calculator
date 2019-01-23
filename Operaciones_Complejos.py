from sys import stdin
import math 
def pretty_printer (t):
     if t [1] >= 0:
          print (t[0], '+', t[1], 'i')
     else:
          print (t[0], t[1], 'i')
     
def addition (c1, c2):
     '''c1 + c2 ---> z
     addition of tuples ---> tuple'''
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = a1 + a2
     y = b1 + b2
     z = (x, y)
     return pretty_printer(z)

def product (c1, c2):
     '''c1 * c2 ---> z
     product of tuples ---> tuple'''
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = (a1 * a2) - (b1 * b2)
     y = (a1 * b2) + (a2 * b1)
     z = (x, y)
     return pretty_printer(z)

def substraction (c1, c2):
     '''c1 - c2 ---> z
     substraction of tuples ---> tuple'''
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = a1 - a2
     y = b1 - b2
     z = (x, y)
     return pretty_printer(z)

def division (c1, c2):
     '''c1 / c2 ---> z
     division of tuples ---> tuple'''
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = ((a1 * a2) + (b1 * b2)) / ((a2 ** 2) + (b2 ** 2))
     y = ((a2 * b1) - (a1 * b2)) / ((a2 ** 2) + (b2 ** 2))
     z = (x, y)
     return pretty_printer(z)

def module (c):
     '''c ----> x
     tuple ---> int'''
     x = ((c[0] ** 2) + (c[1] ** 2)) ** (1/2)
     return x

def conjugate (c):
     '''c ---> c
     tuple ---> tuple'''
     x = c[0]
     y = -c[1]
     z = (x, y)
     return pretty_printer(z)

def car_pol (c):
     '''(a, b) ---> (p, θ)
     tuple ---> tuple'''
     p = ((c[0] ** 2) + (c[1] ** 2)) ** (1/2)
     g = math.atan((c[1]) / (c[0]))
     z = (p, g)
     return z

def pol_car (c):
     '''(p, θ) ---> (a, b)
     tuple ---> tuple'''
     p = c[0]; g = c[1]
     a = p * (math.cos (g))
     b = p * (math.sin (g))
     z = (a, b)
     return pretty_printer(z)















