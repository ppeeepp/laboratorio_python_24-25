# matplotlib - creare visualizzazioni (statiche, animate e interattive) in Python
# Useremo l’interfaccia pyplot che è una collezione di funzioni che rendono matplotlib simile a MATLAB
# pyplot può essere utilizzato in due modi:
# seguendo la struttura degli oggetti che compongono l’immagine
# utilizzando le funzioni di pyplot che modificano una figura di default,
# memorizzando gli stati successivi che vengono creati dalle chiamate a funzioni che modificano l’immagine attiva
# IMMAGINE GENERATA: è costituita da:
#   - figura: contenitore principale
#   - axes: grafico/i contenuto/i nella figura
#   - axis: assi specifici delgrafico
import numpy as np
import matplotlib.pyplot as plt
# creazione oggetti
fig, _ = plt.subplots()
print(type(fig))        # <class 'matplotlib.figure.Figure'>
# rendere "attivo" il grafico
fig, _ = plt.subplots()
graph = fig.gca()       # Get Current Axes
print(type(graph))      # <class 'matplotlib.axes._axes.Axes'>
# prendere tutti i grafici disponibili nella figura
graph_list = fig.get_axes()
print(type(graph_list)) # <class 'list'>
# disegnare
fig, _ = plt.subplots()
graph = fig.gca()  # Get Current Axes
graph.plot([1,2,3])
# salvare o visualizzare l'immagine
import matplotlib.pyplot as plt
fig, _ = plt.subplots()
graph = fig.gca()  # Get Current Axes
graph.plot([1,2,3])
plt.show()  # matplotlib.pytplot.show per gestire finestra
fig.savefig('name.png')  # per salvare immagine su file
# più grafici nella stessa figura
fig, _ = plt.subplots(nrows=1, ncols=2)
graph_list = fig.get_axes()
# una volta ottenuti i grafici, si possono riempire (partendo da sinistra)
fig, _ = plt.subplots(nrows=1, ncols=2)
graph_list = fig.get_axes()
graph_list[0].plot([1,2,3])
graph_list[1].plot([-1,-2,-3])
plt.show()
# grafici come array
# Il secondo oggetto ritornato da subplots che finora abbiamo “buttato via” (_)
# è una scorciatoia per avere gli axes (grafici) come array np
'''fig, _    = plt.subplots(nrows=1, ncols=2)'''
fig, axes = plt.subplots(nrows=1, ncols=2)
print( type(axes) )
# tipi di grafico
fig, _ = plt.subplots(nrows=1, ncols=3)
gr_list = fig.get_axes()
gr_list[0].plot([1,2,3])                               # line plot
gr_list[1].scatter([1,2,3],[-1,5,3])             # scatter plot (dots)
gr_list[2].hist([1,2,1,2,1,3], np.arange(1,3))      # compute histogram (bars)
plt.show()
# personalizzare il grafico - titolo, tipo di tratto, colore,  ...
fig, _ = plt.subplots(nrows=1, ncols=1)
gr1 = fig.gca()
gr1.plot([1,2,3], color='r', label='esempio')
gr1.set_xlabel('asse x')        # titolo asse X
gr1.set_ylabel('asse y')        # titolo asse Y
gr1.set_title('grafico')        # titolo del grafico
gr1.set_xlim(xmin=-1, xmax=7)   # range plot X
gr1.set_ylim(ymin=-5, ymax=4)   # range plotY
gr1.legend()                    # visualizza legenda con titolo dei dataset
plt.show()
# tipo di tratto
fig, _ = plt.subplots(nrows=1, ncols=1)
gr1 = fig.gca()
gr1.plot([1,2,3], color='r', linestyle='--',marker='+',label='esempio')
# si possono disegnare più linee contemporaneamente con notazione matlab
val = np.arange(0, 5, 0.2)
fig, _ = plt.subplots(nrows=1, ncols=1)
gr1 = fig.gca()
gr1.plot(val, val, 'r--',  val, val**2, 'bs', val, val**3, 'g^')
plt.show()















