# Realizzare un programma che calcoli l’integrale di una funzione iterativamente e disegni il grafico.
# Data una funzione, un intervallo di integrazione, ed un valore di approssimazione massima:
    # 1) calcolare l’integrale della funzione nell’intervallo campionando la funzione in un numero di punti massimo,
    #    selezionabile dall’utente, ma parta da un valore di default
    # 2) incrementi ciclicamente il numero di punti di campionamento per migliorare la stima dell’intervallo
    # 3) interrompa la stima dell’integrale quando la differenza tra valore precedente ed attuale
    #    è minore del valore di approssimazione massima definito
    # 4) visualizzi il valore finale dell’integrale ed il numero di iterazioni eseguito per ottenerla
    # 5) prepari un grafico che visualizzi la funzione campionata in 3 momenti:
    #    alla prima stima default, a metà del numero totale di interazioni, la curva finale corrispondente al risultato
    # 6) definita una soglia di valore (y) preparare un grafico con solo la porzione di funzione al di sopra della soglia
    # 7) gestisca 3 funzioni a vostra scelta, oltre a quella di default “profilo_gaussiano”
# La gestione della struttura del programma è libera,
# ma va implementato come una classe che getisce le operazioni i cui metodi dell’oggetto sono chiamate in un main
import numpy as np
import matplotlib.pyplot as plt

def profilo_gaussiano(x, sigma):
    # valore profilo gaussiano in posizione x, data apertura
    return np.exp(-0.5*((x/sigma)**2))

def retta(x, m, q):
    # retta data dall'equazione f(x) = mx+q
    return m*x+q

def parabola(x, a):
    # parabola data dall'equazione f(x) = ax^2
    return a*x**2

def esponenziale(x, a):
    # esponenziale f(x) = e^(ax)
    return np.exp(a*x)

class IntegrazioneFunzioni:
    """
    Classe per definire l'integrazione iterativa di una funzione.
    I parametri per inizializzare un oggetto di questa classe sono:
    funzione, intervallo, numero massimo di punti, soglia y, approssimazione massima.
    Tiene anche traccia del numero di iterazioni effettuate e dei campionamenti, che serviranno dopo.
    """
    def __init__(self, f, interval, max_approx, soglia, max_points=10):
        self.f = f
        self.interval = interval
        self.max_approx = max_approx
        self.soglia = soglia
        self.max_points = max_points
        # inizializzo anche il n di iterazioni e di campionamenti per tenerne traccia
        self.n_iterazioni = 0
        self.l_campionamenti = []       # lista che conterrà tuple (x, f(x)), calcolate ad ogni iterazione
    # punti 1), 2), 3), 4)
    def calc_integ(self):
        """
        Metodo che calcola iterativamente l'integrale della funzione, partendo da un certo numero di punti per il campionamento.
        In ogni iterazione, calcola l'integrale con quel numero di punti e salva il campionamento, per poi aumentare il numero di punti da campionare.
        Si ferma se la differenza tra il valore ottenuto e quello precedente è minore di un certo valore di approssimazione
        """
        a, b = self.interval
        points = self.max_points
        prev_value = 0
        value = 0
        while prev_value == 0 or abs(value - prev_value) > self.max_approx:
            x = np.linspace(a, b, points)
            f_x = self.f(x)
            value = np.trapezoid(f_x, x)         # np.trapz mi dava errore dicendo che è "deprecated"
            self.l_campionamenti.append((x, f_x))
            prev_value = value
            self.n_iterazioni += 1
            points += 10
        return value, self.n_iterazioni

    # punto 5)
    def plot_3_moments(self):
        """
        Metodo che crea un grafico della funzione in 3 momenti del campionamento:
        1. alla prima iterazione,
        2. a metà delle iterazioni totali,
        3. dopo l'ultima iterazione.
        """
        fig, axes = plt.subplots()
        colors = ['red', 'green', 'blue']
        labels = ['inizio', 'metà', 'fine']
        instants = [0, len(self.l_campionamenti)//2, len(self.l_campionamenti)-1]
        for i, color, label in zip(instants, colors, labels):
            x,y = self.l_campionamenti[i]       # REMIND: ogni elemento [i] è una tupla (x, y)
            axes.plot(x, y, label=f'{label} - punti: {len(x)}')
        axes.set_title('Funzione campionata in 3 momenti - INIZIO, METÀ, FINE')
        axes.set_xlabel('x')
        axes.set_ylabel('f(x)')
        axes.legend()
        axes.grid(True)
        plt.show()

    # punto 6)
    def plot_over_soglia(self):
        """
        Metodo che crea un grafico della funzione solo nei punti in cui essa supera una certa soglia y.
        Per farlo utilizza solo l'ultimo campionamento e mostra solo la porzione di curva
        in cui si va al di sopra della soglia.
        """
        x, f_x = self.l_campionamenti[-1]   # considero solo l'ultimo campionamento
        fig, axes = plt.subplots()
        x_over = []                         # creo due liste in cui i valori x e f(x) sono > soglia
        f_x_over = []
        for i in range(len(f_x)):
            if f_x[i] > self.soglia:
                x_over.append(x[i])
                f_x_over.append(f_x[i])
        axes.plot(x_over, f_x_over, label=f'Valori sopra la soglia {self.soglia}')
        axes.set_title(f'f(x) al di sopra della soglia {self.soglia}')
        axes.set_xlabel('x')
        axes.set_ylabel('f(x)')
        axes.legend()
        axes.grid(True)

        plt.show()

def menu():
    """
    Menù interattivo che permette all'utente di selezionare una funzione da integrare e definirne i parametri.
    """
    print('Scegli la funzione da integrare:\n'
    '1 - Profilo Gaussiano\n'
    '2 - Retta (f(x)=mx+q)\n'
    '3 - Parabola (f(x)=ax^2)\n'
    '4 - Esponenziale (f(x)=e^(ax))\n')
    user_input = input('Inserisci il numero della funzione: ').strip()
    if user_input == '1':
        sigma = float(input('Inserisci sigma per profilo gaussiano (es. 1.0): '))
        def f(x):
            return profilo_gaussiano(x, sigma)
    elif user_input == '2':
        m = float(input('Inserisci coefficiente m per retta: '))
        q = float(input('Inserisci intercetta q per retta: '))
        def f(x):
            return retta(x, m, q)
    elif user_input == '3':
        a = float(input('Inserisci coefficiente a della parabola: '))
        def f(x):
            return parabola(x, a)

    elif user_input == '4':
        a = float(input('Inserisci coefficiente a dell\'esponenziale: '))
        def f(x):
            return esponenziale(x, a)
    else:
        print('Scelta non valida')
    return f

def main():
    a = float(input('Inserisci il limite inferiore dell\'intervallo: '))
    b = float(input('Inserisci il limite superiore dell\'intervallo: '))
    interval = (a,b)
    max_approx = float(input('Scegli il valore di approssimazione massima: '))
    soglia = float(input('Inserisci il valore della soglia di y per il grafico: '))
    max_points = int(input('Inserisci il numero di punti per il campionamento iniziale (MINIMO = 10): '))
    if max_points < 10:
        max_points = 10
    f = menu()
    integ = IntegrazioneFunzioni(f, interval, max_approx, soglia, max_points)
    print(f'Risultato + numero iterazioni = {integ.calc_integ()}')
    integ.plot_3_moments()
    integ.plot_over_soglia()


main()






































