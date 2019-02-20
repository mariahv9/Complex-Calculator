from sys import stdin
import math
import unittest
'---------------------------------------o---------------------------------------'
#operaciones ecuaciones con complejos 
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

def subtraction (c1, c2):
     '''c1 - c2 ---> z
     subtraction of tuples ---> tuple'''
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

def inverse (c):
     '''c ---> -c
     tuple ---> tuple'''
     x = -c[0]
     y = -c[1]
     z = (x, y)
     return z

'---------------------------------------o---------------------------------------'
#operaciones vectores con complejos 
def ad_vec (v1, v2):
    '''v1 = [(c1, c2), (c1, c2),...,(c1, c2)] +
    v2 = [(c1, c2), (c1, c2),...,(c1, c2)] =
    v = [(c1, c2), (c1, c2),...,(c1, c2)]'''
    par = []
    for i in range (len (v1)):
        for j in range (len (v2)):
            if len (v1) != len (v2): print ('Esta suma no es posible por dimensiones de los vectores')
            else: a = addition (v1[i], v2[i])
        par.append (a)
    return (par)

def prod_vec (c, v):
    '''c = (a1, b1) x v = [(c1, c2), (c1, c2),...,(c1, c2)]
    tuple x matrix ---> matrix'''
    pr = []
    for i in range (len (v)):
        pr.append(product (c, v [i]))
    return (pr)

def sub_vec (v1, v2):
    '''v1 = [(c1, c2), (c1, c2),...,(c1, c2)] -
    v2 = [(c1, c2), (c1, c2),...,(c1, c2)] =
    v = [(c1, c2), (c1, c2),...,(c1, c2)]'''
    par = []
    for i in range (len (v1)):
        for j in range (len (v2)):
            if len (v1) != len (v2): print ('Esta resta no es posible por dimensiones de los vectores')
            else: a = subtraction (v1[i], v2[i])
        par.append (a)
    return (par)

def inv_vect (v):
     '''v = [(c1, c2), (c1, c2),...,(c1, c2)]
     vector ---> vector'''
     inv = []
     for i in range (len (v)):
          inv.append (inverse (v[i]))
     return inv

def conjugate_vec (v):
     '''v = [(c1, c2), (c1, c2),...,(c1, c2)]
     vector ---> vector'''
     con = []
     for i in range (len (v)):
          con.append (conjugate (v[i]))
     return con

def norm_vec (v):
     '''v = [(c1, c2), (c1, c2),...,(c1, c2)]
     vector ---> tuple'''
     c = 0
     for i in range (len (v)):
          c += (module (v[i]))
     return c

def vec_equal (v1, v2):
     '''v1 = [(c1, c2), (c1, c2),...,(c1, c2)];
     v2 = [(c1, c2), (c1, c2),...,(c1, c2)]
     vector, vector ---> boolean'''
     for i in range (len (v1)):
          if v1[i] == v2[i]:
               return True
          else: return False

def prod_intern_vec (v1, v2):
     '''vector, vector ---> tuple'''
     if len (v1) != len (v2):
          print ('Esta operacion no es posible por dimension de los vectores')
     else:
          prod = (0, 0)
          conj = conjugate_vec (v1)
          for i in range (len (v1)):
               prod = addition (prod, product(conj[i], v2 [i]))
          return prod
        
def distance_vec (v1, v2):
     '''vector, vector ---> real'''
     solve = ad_vec (v1, inv_vect (v2))
     return module (prod_intern_vec (solve, solve))
          
def tensor (v1, v2):
     for i in range (len (v1)):
          tensor = []
          for j in range (len (v2)):
               tensor.append (product (v1 [i], v2 [j]))
          v1 [i] = tensor
     return v1
          
'---------------------------------------o---------------------------------------'
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

def m_subtraction (m1, m2):
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
                a = subtraction (m1 [i][j], m2 [i][j])
                par.append (a)
        su.append (par)
    return (su)                

def m_product (m1, m2):
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
                        add = addition (product(m1[l][k],m2 [j][l] ), add)
                   res.append(add)
              pro.append(res)
         return pro

def m_escale (c, m):
    '''c = (a, b) x
    m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] =
    M = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
    tuple, matrix ---> matrix'''
    pro = []
    for i in range (len (m)):
         for j in range (len (m[0])):
              pro.append (product (m [i][j]), c)
    return pro

def m_traspouse (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
     matrix ---> matrix'''
     mat = []
     for i in range (len (m[0])):
          line = []
          for j in range (len (m)):
               line.append (m[j][i])
          mat.append (line)
     return mat

def m_conjugate (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
     matrix ---> matrix'''
     mat = []
     for i in range (len (m)):
          line = []
          for j in range (len (m [0])):
               line.append (conjugate (m[i][j]))
          mat.append (line)
     return mat

def m_adjoint (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
     matrix ---> matrix'''
     return m_conjugate (m_traspouse (m))

def m_inverse (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
     matrix ---> matrix'''
     mat = []
     for i in range (len (m)):
          inv = []
          for j in range (len (m [0])):
               inv.append (conjugate (m[i][j]))
          mat.append (inv)
     return mat      

def m_trace (m):
     '''matrix ---> tuple'''
     b = (0, 0)
     for i in range (len (m)):
          b = addition (b, m [i][i])
     return (b)

def m_prod_intern (m1, m2):
     '''matrix, matrix ---> tuple'''
     m = m_product (m_adjoint (m1), m2)
     return m_trace (m)

def action_mat_vec (m, v):
     '''matrix, vector ---> tuple'''
     if len (m[0]) != len (v):
          print ('No es posible hacer la accion por las dimensiones vector-matriz')
     else:
          ac = (0, 0)
          for i in range (len (v)):
               for j in range (len (m[0])):
                    ac = addition (ac, product (m[i][j], v[j]))
          return ac
   
def m_equal(m1, m2):
     '''matrix, matrix ---> boolean'''
     if m1 == m2 : return True
     else: return False
                 
def m_hermitian (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
     matrix ---> boolean'''
     if len (m) != len (m[0]):
          print ('Matriz no cuadrada')
     else:
          adj = m_adjoint (m)
     return m_equal (adj, m)

def m_identity (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
     matrix ---> boolean'''
     for i in range (len (m)):
          for j in range (len (m [0])):
               if m [i][i] == (1, 0): return True
               else: return False
               
def m_unitary (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
     matrix ---> boolean'''
     if len (m) != len (m[0]):
          print ('Matriz no cuadrada')
     else:
          mat_adj = m_product (m, m_adjoint (m))
     return m_identity (mat_adj)

'---------------------------------------o---------------------------------------'
#pruebas ecuaciones con complejos 
class TestCases (unittest.TestCase):
     def test_addition (self):
          result = addition ((2, 5), (3, 3))
          self.assertEqual (result, (5, 8))

     def test_product (self):
          result = product ((2, 5), (3, 3))
          self.assertEqual (result, (-9, 21))

     def test_subtraction (self):
          result = subtraction ((2, 5), (3, 3))
          self.assertEqual (result, (-1, 2))

     def test_division (self):
          result = division ((2, 5), (3, 3))
          self.assertEqual (result, (1.1666666666666667, 0.5))

     def test_module (self):
          result = module ((2, 5))
          self.assertEqual (result, (5.385164807134504))

     def test_conjugate (self):
          result = conjugate ((2, 5))
          self.assertEqual (result, ((2, -5)))

     def test_car_pol (self):
          result = car_pol ((2, 5))
          self.assertEqual (result, (5.385164807134504, 1.1902899496825317))

     def test_pol_car (self):
          result = pol_car ((2, 5))
          self.assertEqual (result, (0.5673243709264525, -1.917848549326277))

     def test_inverse (self):
          result = inverse ((2, 5))
          self.assertEqual (result, ((-2, -5)))

#pruebas vectores con complejos 
     def test_ad_vec (self):
          result = ad_vec (([(3,2),(0,0),(5,-6)]), ([(1,0),(4,2),(0,1)]))
          self.assertEqual (result, ([(4, 2), (4, 2), (5, -5)]))

     def test_prod_vec (self):
          result = prod_vec (((3,2)), ([(1,0),(4,2),(0,1)]))
          self.assertEqual (result, ([(3, 2), (8, 14), (-2, 3)]))

     def test_sub_vec (self):
          result = sub_vec (([(3,2),(0,0),(5,-6)]), ([(1,0),(4,2),(0,1)]))
          self.assertEqual (result, ([(2, 2), (-4, -2), (5, -7)]))

     def test_inv_vect (self):
          result = inv_vect (([(3,2),(0,0),(5,-6)]))
          self.assertEqual (result, ([(-3, -2), (0, 0), (-5, 6)]))

     def test_conjugate_vec (self):
          result = conjugate_vec (([(3,2),(0,0),(5,-6)]))
          self.assertEqual (result, ([(3, -2), (0, 0), (5, 6)]))

     def test_norm_vec (self):
          result = norm_vec (([(3,2),(0,0),(5,-6)]))
          self.assertEqual (result, (11.415800951370644))

     def test_vec_equal (self):
          result = vec_equal (([(3,2),(0,0),(5,-6)]), ([(1,0),(4,2),(0,1)]))
          self.assertEqual (result, (False))

     def test_prod_intern_vec (self):
          result = prod_intern_vec (([(3,2),(0,0),(5,-6)]), ([(1,0),(4,2),(0,1)]))
          self.assertEqual (result, ((-3, 3)))

     def test_distance_vec (self):
          result = distance_vec (([(3,2),(0,0),(5,-6)]), ([(1,0),(4,2),(0,1)]))
          self.assertEqual (result, (102.0))

     def test_tensor (self):
          result = tensor (([(3,2),(0,0),(5,-6)]), ([(1,0),(4,2),(0,1)]))
          self.assertEqual (result, ([[(3, 2), (8, 14), (-2, 3)], [(0, 0), (0, 0), (0, 0)], [(5, -6), (32, -14), (6, 5)]]))    

#pruebas matrices con complejos
     def test_ad_mat (self):
          result = ad_mat (([[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]]), ([[(5,0),(2,-1),(6,-4)],[(0,0),(4,5),(2,0)],[(7,-4),(2,7),(0,0)]]))
          self.assertEqual (result, [[(8, 2), (2, -1), (11, -10)], [(1, 0), (8, 7), (2, 1)], [(11, -5), (2, 7), (4, 0)]])

     def test_m_subtraction (self):
          result = m_subtraction (([[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]]), ([[(5,0),(2,-1),(6,-4)],[(0,0),(4,5),(2,0)],[(7,-4),(2,7),(0,0)]]))
          self.assertEqual (result, [[(-2, 2), (-2, 1), (-1, -2)], [(1, 0), (0, -3), (-2, 1)], [(-3, 3), (-2, -7), (4, 0)]])

     def test_m_product (self):
          result = m_product (([[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]]), ([[(5,0),(2,-1),(6,-4)],[(0,0),(4,5),(2,0)],[(7,-4),(2,7),(0,0)]]))
          self.assertEqual (result, [[(37, -13), (12, 3), (31, 9)], [(10, 0), (6, 28), (-6, 32)], [(50, -44), (3, 4), (4, -60)]])

     def test_m_traspouse (self):
          result = m_traspouse (([[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]]))
          self.assertEqual (result, [[(3, 2), (1, 0), (4, -1)], [(0, 0), (4, 2), (0, 0)], [(5, -6), (0, 1), (4, 0)]])

     def test_m_conjugate (self):
          result = m_conjugate (([[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]]))
          self.assertEqual (result, [[(3, -2), (0, 0), (5, 6)], [(1, 0), (4, -2), (0, -1)], [(4, 1), (0, 0), (4, 0)]])

     def test_m_adjoint (self):
          result = m_adjoint (([[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]]))
          self.assertEqual (result, [[(3, -2), (1, 0), (4, 1)], [(0, 0), (4, -2), (0, 0)], [(5, 6), (0, -1), (4, 0)]])

     def test_m_inverse (self):
          result = m_inverse (([[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]]))
          self.assertEqual (result, [[(3, -2), (0, 0), (5, 6)], [(1, 0), (4, -2), (0, -1)], [(4, 1), (0, 0), (4, 0)]])

     def test_m_trace (self):
          result = m_trace (([[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]]))
          self.assertEqual (result, (11, 4))
  
if __name__ == '__main__':
    unittest.main()
