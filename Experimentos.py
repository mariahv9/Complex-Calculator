from sys import stdin
import math
import unittest
from numpy import linalg as operation
'---------------------------------------o---------------------------------------'
#ase operations
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

def m_product (A, B):
    filasB = len(B)
    columnasA = len(A[0])
    if filasB == columnasA:
        filas = len(A)
        columnas = len(B[0])
        matriz = [[(0, 0)] * columnas for x in range(filas)]
        for i in range(0, filas):
            for j in range(0, columnas):
                for k in range(0, len(B)):
                    m = product(A[i][k], B[k][j])
                    n = matriz[i][j]
                    matriz[i][j] = (m[0]+n[0], m[1]+n[1])
        return matriz
    else:
        print("La dimensión de la matriz es incorrecta")
        return False

def m_traspouse (matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    return [[matriz[j][i] for j in range(filas)] for i in range(columnas)]


def norm_vec (v):
     '''v = [(c1, c2), (c1, c2),...,(c1, c2)]
     vector ---> tuple'''
     r = 0
     t = 0
     for i in range (len (v)):
          r += (v[i][0]**2)
          t += (v[i][1]**2)
     return (r+t)**0.5

def conjugate (c):
     '''c ---> c
     tuple ---> tuple'''
     x = c[0]
     y = -c[1]
     z = (x, y)
     return z

def conjugate_vec (v):
     '''v = [(c1, c2), (c1, c2),...,(c1, c2)]
     vector ---> vector'''
     con = []
     for i in range (len (v)):
          con.append (conjugate (v[i]))
     return con

def prod_intern_vec (v1, v2):
     '''vector, vector ---> tuple'''
     if len (v1) != len (v2):
          print ('Esta operacion no es posible por dimension de los vectores')
     else:
          prod = (0, 0)
          for i in range (len (v1)):
               prod = addition (prod, product(v1[i], v2 [i]))
          return prod

def prod_vec (c, v):
    '''c = (a1, b1) x v = [(c1, c2), (c1, c2),...,(c1, c2)]
    tuple x matrix ---> matrix'''
    pr = []
    for i in range (len (v)):
        pr.append(product (c, v [i]))
    return (pr)

def m_hermitian (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
     matrix ---> boolean'''
     if len (m) != len (m[0]):
          print ('Matriz no cuadrada')
     else:
          adj = m_adjoint (m)
     return m_equal (adj, m)

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

def m_identity (n):
     m = [[(0, 0) for i in range (n)]for j in range (n)]
     for i in range (n):
          m [i][i] = (1, 0)
     return m

def m_adjoint (m):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
     matrix ---> matrix'''
     return m_conjugate (m_traspouse (m))

def m_equal(m1, m2):
     '''matrix, matrix ---> boolean'''
     if m1 == m2 : return True
     else: return False

def m_escale (c, m):
    '''c = (a, b) x
    m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]] =
    M = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]]
    tuple, matrix ---> matrix'''
    pro = []
    for i in range (len (m)):
         a = []
         for j in range (len (m[0])):
              a.append (product (m [i][j], c))
         pro.append(a)
    return pro

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

def module(c):
    '''|c| = |a + bi| -------> ((a)**2+(b)**2)**0.5'''
    a, b = c[0],c[1]
    return ((a)**2+(b)**2)**0.5

'---------------------------------------o---------------------------------------'
#operations cap3
def canics (m, v, N):
    '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]], 
    v = [(c1, c2), (c1, c2),...,(c1, c2)]
    N = int;
    (m ** N) * v = V;
    matrix, vector, int ---> vector'''
    mat_n = m
    for i in range (1, N-1):
        n = m_product (mat_n, m)
        mat_n = n
    return (m_product (mat_n, m_traspouse(v)))

def bullets (m, v, N):
    '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]], 
    v = [(c1, c2), (c1, c2),...,(c1, c2)]
    N = int;
    (m ** N) * v = V;
    matrix, vector, int ---> vector'''
    mat_n = m
    for i in range (1, N-1):
        n = m_product (mat_n, m)
        mat_n = n
    return (m_product (mat_n, m_traspouse(v)))

def count_bullets (m, N):
    '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]], 
    v = [(c1, c2), (c1, c2),...,(c1, c2)]
    N = int;
    (m ** N) * v = V;
    matrix, vector, int ---> vector'''
    mat_n = m
    for i in range (1, N):
        n = m_product (mat_n, m)
        mat_n = n
    n = m
    for i in range (len (m)):
         for k in range (len (m [0])):
              solve = (m [i][k][0]**2 + m [i][k][1]**2)
              n [i][k] = solve
    return n

def probability_ket (h, ket):
     '''h = indice, ket = vector (ket)'''
     result = norm_vec (ket)
     r = abs (sum (product (ket[h], ket [h])))
     ans = r / (result ** 2)
     return ans 

def amplitude_ket (n1, n2, k1, k2):
     '''k1, k2 ---> vector'''
     k3 = conjugate_vec (k2)
     r1 = prod_vec (n1, k1)
     r2 = prod_vec (n2, k3)
     return prod_intern_vec (r1, r2)

def average_value (ket, m):
     kat = []
     for i in range (len (ket)):
          kat.append([ket [i]])
     r = m_product (m, kat)
     r = m_conjugate (r)
     y = []
     l = []
     for i in r:
          for j in i:
               y.append (j)
     return prod_intern_vec (y, ket)

def variance (m, k):
     '''m = [[(c1, c2)], [(c1, c2)],...,[(c1, c2)]],
     ket = vector (ket),
     m, k ---> tuple'''
     if m_hermitian (m):
          n = len (m)
          mat = m_escale ((average_value (k, m)), (m_identity (n)))
          u = m_subtraction (m,  mat)
          sol = m_product (u, u)
          res = 0
          for i in range (len (k)):
               a = module (k [i])**2
               res += a * sol [i][i][0]
     return res

def eigen_values(observable):
    aux = []
    for i in range(len(observable)):
        z = []
        for j in range(len(observable[0])):
            a = observable[i][j][0]
            b = observable[i][j][1]
            b = eval(str(b)+'j')
            z.append(a+b)
        aux.append(z)
    valores,vectores = operation.eigh(aux)
    rta = []
    for i in valores:
        rta.append(i)
    return rta

def eigen_vectors(observable):
    aux = []
    for i in range(len(observable)):
        z = []
        for j in range(len(observable[0])):
            a = observable[i][j][0]
            b = observable[i][j][1]
            b = eval(str(b)+'j')
            z.append(a+b)
        aux.append(z)
    valores,vectores = operation.eigh(aux)
    rta = []
    for i in vectores:
        w = []
        for j in i:
            aux = str(j)
            b = aux.index('j')
            a = b
            for i in range(len(aux)):
                if aux[::-1][i] == '-' or aux[::-1][i] == '+':
                    a = i
                    break
            try:
                a = len(aux)-a
                tupla = (float(aux[1:a-1]),float(aux[a:b]))
                w.append(tupla)
            except ValueError:
                tupla = (0,float(aux[:b]))
                w.append(tupla)
        rta.append(w)
    return rta

def transitor_probability(observable,estado):
    propios = eigen_vectors(observable)
    valores = eigen_values(observable)
    aux = []
    for i in range(len(estado)):
        aux.append([estado[i]])
    au = m_product (observable,aux)
    aux = []
    for i in au:
        for j in i:
            aux.append(j)
    pn = []
    for i in aux:
        pn.append(module (i)**2)
    ans = 0
    for i in range(len(valores)):
        ans += valores[i]*pn[i]
    return ans

def system_dynamic(n,M,estado):
    estado = [estado]
    for i in range(n):
        estado = m_product(estado,M)
    return estado[0]
       
'---------------------------------------o---------------------------------------'
#test experiments
class TestCases (unittest.TestCase):
     def test_canics (self):
          result = canics (([[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],[(0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (1, 0)],[(0, 0), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)],[(0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],[(1, 0), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)]]), [[(6, 0), (2, 0), (1, 0), (5, 0), (3, 0), (10, 0)]], 1)
          self.assertEqual (result, [[(0, 0)], [(0, 0)], [(12, 0)], [(5, 0)], [(1, 0)], [(9, 0)]])
          
     def test_bullets (self):
          result = bullets ([[(0, 0), (1/6, 0), (5/6, 0)],[(1/3, 0), (1/2, 0), (1/6, 0)],[(2/3, 0), (1/3, 0), (0, 0)]], [[(1/6, 0), (1/6, 0), (2/3, 0)]], 1)
          self.assertEqual (result, [[(0.5833333333333334, 0.0)], [(0.25, 0.0)], [(0.16666666666666666, 0.0)]])

     def test_count_bullets (self):
          result = count_bullets ([[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],[(1/(2)**(1/2), 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],[(1/(2)**(1/2), 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],[(0, 0), (-1/(6)**(1/2), 1/(6)**(1/2)), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)],[(0, 0), (-1/(6)**(1/2), -1/(6)**(1/2)), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],[(0, 0), (1/(6)**(1/2), -1/(6)**(1/2)), (-1/(6)**(1/2), 1/(6)**(1/2)), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)],[(0, 0), (0, 0), (-1/(6)**(1/2), -1/(6)**(1/2)), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)],[(0, 0), (0, 0), (1/(6)**(1/2), -1/(6)**(1/2)), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]], 1)
          self.assertEqual (result, [[0, 0, 0, 0, 0, 0, 0, 0], [0.4999999999999999, 0, 0, 0, 0, 0, 0, 0], [0.4999999999999999, 0, 0, 0, 0, 0, 0, 0], [0, 0.3333333333333334, 0, 1, 0, 0, 0, 0], [0, 0.3333333333333334, 0, 0, 1, 0, 0, 0], [0, 0.3333333333333334, 0.3333333333333334, 0, 0, 1, 0, 0], [0, 0, 0.3333333333333334, 0, 0, 0, 1, 0], [0, 0, 0.3333333333333334, 0, 0, 0, 0, 1]])
          
     def test_probability_ket (self):
          result = probability_ket (2, [(-3, -1), (0, -2), (0, 1), (2, 0)])
          self.assertEqual (result, 0.05263157894736841)

     def test_amplitude_ket (self):
          result = amplitude_ket (((2**0.5) / 2, 0), ((2**0.5) / 2, 0), [(1, 0), (0, 1)], [(0, 1), (-1, 0)])
          self.assertEqual (result, (0.0, -1.0000000000000002))

     def test_average_value (self):
          result = average_value ([((2**0.5) / 2, 0), (0, (2**0.5) / 2)], [[(1, 0), (0, -1)], [(0, 1), (2, 0)]])
          self.assertEqual (result, (2.5000000000000004, 0.0))

     def test_variance (self):
          result = variance ([[(1, 0), (0, -1)], [(0, 1), (2, 0)]], [((2**0.5) / 2, 0), (0, (2**0.5) / 2)])
          self.assertEqual (result, 2.2500000000000013)

     def test_transitor_probability(self):
          result = transitor_probability ([[(-1,0),(0,-1)],[(0,1),(1,0)]], [(1/2,0),(1/2,0)]) 
          self.assertEqual (result, 0)
          
     def test_system_dynamic (self):
          result = system_dynamic (4, [[(0,0),(1/(2)**0.5,0),(1/(2)**0.5,0),(0,0)],[(0,1/(2)**0.5),(0,0),(0,0),(1/(2)**0.5,0)],[(1/(2)**0.5,0),(0,0),(0,0),(0,1/(2)**0.5)],[(0,0),(1/(2)**0.5,0),(-1/(2)**0.5,0),(0,0)]], [(1,0),(0,0),(0,0),(0,0)])
          self.assertEqual (result, [(-0.49999999999999983, 0.49999999999999983), (0.0, 0.0), (0.0, 0.0), (0.49999999999999983, 0.49999999999999983)])
          
if __name__ == '__main__':
    unittest.main()
