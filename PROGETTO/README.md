<h3>Giuseppe Fedele - mat. IN0501039</h3>
<h3>Esame di Laboratorio di Programmazione in Python - A.A. 2024/2025</h3>
<h1>Progetto Software - Simulazione gioco "Affari Tuoi"</h1>
<h2>Descrizione</h2>
<p>
L'obiettivo del progetto è quello di svolgere simulazione semplificata del gioco a premi televisivo "Affari Tuoi".
Il gioco è strutturato nel seguente modo:
<li>All'inizio del gioco, sono presenti 20 pacchi, tutti quanti numerati dall'1 al 20 e ognuno contenente un montepremi, che va da 0 a 300.000 €.</li>
<li>Il concorrente sceglie un pacco, i restanti pacchi vengono assegnati casualmente ai "pacchisti".</li>
<li>Una volta che il concorrente ha scelto il pacco, il gioco ha inizio. Il concorrente deve effettuare dei "tiri", ovvero scegliere un pacco che verrà aperto per scoprirne il montepremi contenuto, che verrà dunque eliminato dalla lista dei montepremi disponibili.</li>
<li>L'avversario del concorrente è il "Dottore", un'entità che conosce il contenuto di tutti i pacchi in grado di proporre offerte al concorrente per terminare prima il gioco.</li>
<li>Le offerte del Dottore funzionano in questo modo: in base all'andamento del concorrente, propone una cifra da lui stabilita e un numero di tiri da effettuare in caso essa venga rifiutata. Può inoltre proporre lo scambio del pacco con un qualsiasi pacco disponibile, al posto di una quota in denaro.</li>
<li>All'inizio della partita, il concorrente ha da effettuare obbligatoriamente 6 tiri, prima della prima offerta ufficiale del Dottore.</li>
<li>L'obiettivo del concorrente è battere il Dottore e può avvenire in due modi:</li>
- arrivare alla fine del gioco con il pacco più alto rispetto ai montepremi offerti dal dottore;<br>
- accettare un'offerta del dottore che si riveli maggiore del contenuto del pacco in proprio possesso.
</p>
<h2>Struttura del progetto</h2>
<h3>doctor.py</h3>
<p>Contiene la classe Doctor, che rappresenta il personaggio del Dottore e la sua logica.<br>
La classe contiene un metodo statico <b>make_offer()</b>, che calcola l'offerta che verrà poi presentata al concorrente a partire da una cifra base, variabile in base al contenuto del pacco del concorrente, del suo andamento e della deviazione standard tra i pacchi rimanenti.<br>
Inoltre, la classe contiene un altro metodo statico <b>propose_swap()</b>, che simula la proposta del Dottore al concorrente di scambiare il suo pacco con uno a sua scelta.</p>
















