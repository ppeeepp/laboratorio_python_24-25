# numpy: libreria per il scientific computing in python
# fornisce oggetti come array multidimensionali (come matrici, vettori, ...)
# e un assortimento di routine per operazioni veloci su array,
# tra cui operazioni matematiche, logiche, di ordinamento, selezione, I/O,
# trasformate di Fourier discrete, algebra lineare di base, statistica, simulazioni random, ...
# -> permette di creare e manipolare dati numerici operando con vettori multidimensionali in modo efficiente
import numpy as np
# vettore di 5 elementi
vettore = np.array([1,2,4,3,5])
print(vettore)              # output:   [1 2 4 3 5]
print(type(vettore))        # output:   <class 'numpy.ndarray'>
# matrice 2 x 3
matrice = np.array([ [1,2,3] , [4,5,6] ])
print(matrice)              # output:   [[1 2 3]
#                                        [4 5 6]]
print(type(matrice))        # output: <class 'numpy.ndarray'>
print(matrice.ndim)         # output: 2
print(matrice.shape)        # output: (2,3)
print(matrice.size)         # output: 6
# funzioni per creare array
# array di elementi equispaziati in un range intero
vettore = np.arange(5)
print(vettore)              # output: [0 1 2 3 4]
print(type(vettore))        # output: <class 'numpy.ndarray'>
# array di elementi equispaziati in un range conoscendo range e numero di punti voluti
vettore = np.linspace(0, 2, 6)
print(vettore)              # output: [0.  0.4 0.8 1.2 1.6 2. ]
print(type(vettore))        # output: <class 'numpy.ndarray'>
# array di elementi casuali
vettore = np.random.rand(6)
print(vettore)              # output: [0.28916635 0.89594151 0.02676755 0.86228301 0.53028847 0.7094391 ]
print(type(vettore))        # output: <class 'numpy.ndarray'>
# array vuoti
vettore = np.zeros(6)
print(vettore)              # output: [0. 0. 0. 0. 0. 0.]
print(type(vettore))        # output: <class 'numpy.ndarray'>
# array di tutti 1
vettore = np.ones(6)
print(vettore)              # output: [1. 1. 1. 1. 1. 1.]
print(type(vettore))        # output: <class 'numpy.ndarray'>
# array inizializzati con un valore
vettore = np.full(6, 3)
print(vettore)              # output: [3. 3. 3. 3. 3. 3.]
print(type(vettore))        # output: <class 'numpy.ndarray'>
# matrici speciali
matrice = np.eye(6)
print(matrice)              # output:   [[1. 0. 0. 0. 0. 0.]
#                                        [0. 1. 0. 0. 0. 0.]
#                                        [0. 0. 1. 0. 0. 0.]
#                                        [0. 0. 0. 1. 0. 0.]
#                                        [0. 0. 0. 0. 1. 0.]
#                                        [0. 0. 0. 0. 0. 1.]]
print(type(matrice))        # output: <class 'numpy.ndarray'>
# specificare il tipo di dati nel vettore
import numpy as np
vettore = np.array([1,2,3,4], dtype='float64')
print(vettore)
print(type(vettore))
print(type(matrice))
# operazioni: +, -, *, /, %, **
# metodi che agiscono su tutti gli elementi
'''
min()
max()
mean()
std()
sort() (sulle MxN sort delle righe)
copy()
where()
'''
# slicing - gli array supporatno lo slicing, come gli oggetti lista
vettore = np.arange(9) +1
print(vettore)          # [1 2 3 4 5 6 7 8 9]
# primi 3 elementi
print(vettore[0:3])     # [1 2 3]\
# slicing su più dimensioni
matrice = np.arange(9) + 1
matrice.shape = (3,3)
print(matrice)
# primna riga
riga_0 = matrice[0:1]
print(riga_0)
# seconda dimensione
colonna_0 = matrice[ : , 0:1]
print(colonna_0)
# elemento specifico
elemento_centrale = matrice[1:2 , 1:2]
print(elemento_centrale)



































