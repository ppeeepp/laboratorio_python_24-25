import sympy
# libreria per il calcolo simbolico:
# gli oggetti son trattati come simboli e rappresentati in modo esatto, senza approssimazioni
# inoltre è possibile avere nelle espressioni matematiche dei simboli a cui non è passato nessun valore

# se un numero ha una rappresentazione esatta, l'espressione è risolta
n = sympy.sqrt(9)
print(n)
# per i numeri il cui risultato sarebbe un'approssimazione, rimane la rappresentazione simbolica
n = sympy.sqrt(8)
print(n)            # 2*sqrt(2)
# e l'oggetto è utilizzabile in una espressione matematica
n = sympy.sqrt(8)
n2 = n/2
print(n2)           # sqrt(2)

# SIMBOLI - simboli a cui non è associato un valore
x = sympy.symbols('x')
expr = x*x
print(expr)         # x**2
# si possono combinare simboli ed espressioni
x, y = sympy.symbols('x y')
expr = 2*x + 3*y
print(expr)         # 2*x + 3*y
# e utilizzare le espressioni
x = sympy.symbols('x')
expr = 2*x + 3*y
r = expr - 2*x
print(r)            # 3*y
# o combinarle
x = sympy.symbols('x')
expr = 2*x + 3*y
r = expr * expr
print(r)            # (2*x + 3*y)**2

# MATRICI - sai possono usare i simboli per fare operazioni con matrici
# esempio matrici di rotazione
cos ,sin = sympy.symbols('cos sin', real=True)
Rot_z = sympy.matrices.Matrix( ([ cos, sin, 0],
                                [-sin, cos, 0],
                                [  0 ,  0 , 1]), real=True)
Rot_y = sympy.matrices.Matrix( ([ cos, 0, sin],
                                [  0,  1,  0 ],
                                [-sin, 0, cos]), real=True)
Rot_x = sympy.matrices.Matrix( ([  1,  0,  0],
                                [  0, cos, sin],
                                [  0,-sin, cos]), real=True)
print(Rot_z)        # Matrix([[cos, sin, 0], [-sin, cos, 0], [0, 0, 1]])
# possiamo combinare le rotazioni
r_xy = Rot_y*Rot_x
print(r_xy)         # Matrix([[cos, -sin**2, cos*sin], [0, cos, sin], [-sin, -cos*sin, cos**2]])
# o agire direttamente sulle matrici
determinante = Rot_x.det()
print(determinante) # cos**2 + sin**2
traccia = Rot_x.trace()
print(traccia)      # 2*cos + 1
trasposta = Rot_x.transpose()
print(trasposta)    # Matrix([[1, 0, 0], [0, cos, -sin], [0, sin, cos]])
# in caso di combinazione di molte matrici, possiamo scegliere se visualizzare il risultato “semplificato” o espandere le espressioni
r_xyz = Rot_x*Rot_z*Rot_y*Rot_x
print(r_xyz)        # Matrix([[cos**2, -cos*sin**2 + cos*sin, cos**2*sin + sin**2], [-cos**2*sin - sin**2, cos**3 - sin*(-cos*sin**2 + cos*sin), cos**2*sin + cos*(-cos*sin**2 + cos*sin)], [cos*sin**2 - cos*sin, -cos**2*sin - sin*(cos**2 + sin**3), -cos*sin**2 + cos*(cos**2 + sin**3)]])
r_xyz_expand = (Rot_x*Rot_z*Rot_y*Rot_x).expand()
print(r_xyz_expand) # Matrix([[cos**2, -cos*sin**2 + cos*sin, cos**2*sin + sin**2], [-cos**2*sin - sin**2, cos**3 + cos*sin**3 - cos*sin**2, -cos**2*sin**2 + 2*cos**2*sin], [cos*sin**2 - cos*sin, -2*cos**2*sin - sin**4, cos**3 + cos*sin**3 - cos*sin**2]])
# e sostituire i simboli con i numeri solo alla fine delle operazioni
import math
r_xy = Rot_y*Rot_x
r_xy = r_xy.subs({cos:math.cos(10), sin:math.sin(10)})
print(r_xy)     # Matrix([[-0.839071529076452, -0.295958969093304, 0.456472625363814], [0, -0.839071529076452, -0.544021110889370], [0.544021110889370, -0.456472625363814, 0.704041030906696]])
# esistono anche dei metodi specifici che permettono ad esempio di trovare gli autovalori in modo esatto
ev = sympy.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).eigenvals()
print(ev)       # {1: 3}

# CALCOLO SIMBOLICO - posso anche risolvere algebricamente le espressioni
# derivate
x = sympy.symbols('x')
expr = 3*x + sympy.cos(x)*sympy.exp(x)
expr_d = sympy.diff(expr, x)
print(expr_d)       # -exp(x)*sin(x) + exp(x)*cos(x) + 3
# integrali
expr = sympy.integrate(expr_d, x)
print(expr)         # 3*x + exp(x)*cos(x)
# integrali con valore
x = sympy.symbols('x')
val = sympy.integrate(sympy.sin(x), (x, 0, (sympy.pi/2)) )
print(val)          # 1
















