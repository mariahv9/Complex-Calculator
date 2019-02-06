from sys import stdin
import math 
#operaciones complejos 
def addition (c1, c2):
     '''c1 + c2 ---> z
     addition of tuples ---> tuple'''
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = a1 + a2
     y = b1 + b2
     z = (x, y)
     return z

def product (c1, c2):
     '''c1 * c2 ---> z
     product of tuples ---> tuple'''
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = (a1 * a2) - (b1 * b2)
     y = (a1 * b2) + (a2 * b1)
     z = (x, y)
     return z

def substraction (c1, c2):
     '''c1 - c2 ---> z
     substraction of tuples ---> tuple'''
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = a1 - a2
     y = b1 - b2
     z = (x, y)
     return z

def division (c1, c2):
     '''c1 / c2 ---> z
     division of tuples ---> tuple'''
     a1 = c1 [0]; a2 = c2 [0]
     b1 = c1 [1]; b2 = c2 [1]
     x = ((a1 * a2) + (b1 * b2)) / ((a2 ** 2) + (b2 ** 2))
     y = ((a2 * b1) - (a1 * b2)) / ((a2 ** 2) + (b2 ** 2))
     z = (x, y)
     return z

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
     return z

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
     return z

#operaciones matrices con complejos
def ad_mat (m1, m2):
    '''m1 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] +
    m2 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] =
    SM = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
    matrix, matrix ---> matrix'''
    ad = []
    for i in range (len (m1)):
        par = []
        for j in range (len(m2)):
            if len (m1 [i]) != len (m2 [i]):
                print ('Esta suma no es posible por dimensiones de las matrices')
            else:
                a = addition (m1 [i][j], m2 [i][j])
                par.append (a)
        ad.append (par)
    return (ad)

def sus_mat (m1, m2):
    '''m1 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] -
    m2 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] =
    SM = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
    matrix, matrix ---> matrix'''
    su = []
    for i in range (len (m1)):
        par = []
        for j in range (len(m2)):
            if len (m1 [i]) != len (m2 [i]):
                print ('Esta resta no es posible por dimensiones de las matrices')
            else:
                a = substraction (m1 [i][j], m2 [i][j])
                par.append (a)
        su.append (par)
    return (su)                

def pro_mat (m1, m2):
    '''m1 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] x
    m2 = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] =
    SM = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
    matrix, matrix ---> matrix'''
    if len (m1 [0]) == len (m2):
         pro = []
         for k in range (len (m1 [0])):
              res=[]
              for j in range (len (m2)):
                   add = (0,0)
                   for l in range (len (m2 [0])):
                        add = addition (product(m1[k][l],m2 [l][j] ), add)
                   res.append(add)
              pro.append(res)
         return pro

def esc_mat (c, m):
    '''c = (a, b) x
    m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] =
    M = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
    tuple, matrix ---> matrix'''
    pro = []
    for i in range (len (m)):
         pro.append (product (m [i]), c)
    return pro

def m_traspouse (m):
     '''matrix ---> matrix'''
     mat = []
     for i in range (len (m[0])):
          line = []
          for j in range (len (m)):
               line.append (m[j][i])
          mat.append (line)
     return mat

def m_conjugate (m):
     '''matrix ---> matrix'''
     mat = []
     for i in range (len (m)):
          line = []
          for j in range (len (m [0])):
               line.append (conjugate (m[i][j]))
          mat.append (line)
     return mat

def m_adjoint (m):
     '''matrix ---> matrix'''
     return m_conjugate (m_traspouse (m))

#operaciones con vectores 
def prod_vec (c, v):
    '''c = (a1, b1) x v = [(c1, c2), (c1, c2),...,(c1, c2)]
    tuple x matrix ---> matrix'''
    pr = []
    for i in range (len (v)):
        pr.append(product (c, v [i]))
    return (pr)
def ad_vec (v1, v2):
    '''v1 = [(c1, c2), (c1, c2),...,(c1, c2)] +
    v2 = [(c1, c2), (c1, c2),...,(c1, c2)] =
    v = [(c1, c2), (c1, c2),...,(c1, c2)]'''
    par = []
    for i in range (len (v1)):
        for j in range (len (v2)):
            if len (v1) != len (v2):
                print ('Esta suma no es posible por dimensiones de los vectores')
            else:
                a = addition (v1[i], v2[i])
        par.append (a)
    return (par)

def sus_vec (v1, v2):
    '''v1 = [(c1, c2), (c1, c2),...,(c1, c2)] -
    v2 = [(c1, c2), (c1, c2),...,(c1, c2)] =
    v = [(c1, c2), (c1, c2),...,(c1, c2)]'''
    par = []
    for i in range (len (v1)):
        for j in range (len (v2)):
            if len (v1) != len (v2):
                print ('Esta resta no es posible por dimensiones de los vectores')
            else:
                a = substraction (v1[i], v2[i])
        par.append (a)
    return (par)
