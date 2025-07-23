# altri metodi di input, oltre a input() e input da file:
# argomenti da linea di comando -> ARGOMENTI
# ad esempio, è possibile chiamare un programma con l'interprete python con:
# $ python programma.py argomento1 argomento2
# qualunque quantità verrà salvata nella lista di argomenti argv del modulo sys
import sys
print(sys.argv) # output: ['lezione_3.py', 'arg1', 'arg3', ...]
# limiti di argv:   è fragile -> dipende dall'ordine
#                   poco chiaro -> difficile ricordare cosa fa ogni parametro

# argparse -> risolve questi limiti
# modulo: argparse
# sintassi: si crea un oggetto ArgumentParser
import argparse
parser = argparse.ArgumentParser()
# per aggiungere parametri si usa add_argument:
parser.add_argument('-n','--nome_esteso', help='Descrizione del parametro')
parser.add_argument('-b','--boolean_value', action='store_true', help="imposta il valore 'True' se trova il parametro")
parser.add_argument('-d','--con_default',  default='riferimento', help="Parametro che ha già un valore di default se non viene fornito l'argomento")
# lettura di tutti gli argomenti: viene fatta con parse_args()
args = parser.parse_args()
# oltre agli argomenti aggiunti da noi, ArgumentParser produrrà un parametro speciale -h
# -> permette di visualizzare le descrizioni (help) dei parametri
# HELP DA LINEA DI COMANDO:
"""
input: 
python programma.py  -h 
output:
['lezione_3.py', '-h']
usage: lezione_3.py [-h] [-n NOME_ESTESO] [-b] [-d CON_DEFAULT]

options:
  -h, --help            show this help message and exit
  -n, --nome_esteso NOME_ESTESO
                        Descrizione del parametro
  -b, --boolean_value   imposta il valore 'True' se trova il parametro
  -d, --con_default CON_DEFAULT
                        Parametro che ha già un valore di default se non viene     
                        fornito l'argomento
"""
# l'help può anche essere personalizzato in fase di creazione del parser
parser = argparse.ArgumentParser(prog="NomePrograma.py",
                                 description="Cosa fa il programma quando utilizzato",
                                 epilog="Altre informazioni come Autore o data")
args = parser.parse_args()
"""
input: 
python programma.py  -h 
output:
usage: NomeProgramma.py [-h] [-n NOME_ESTESO] [-b] [-d CON_DEFAULT]

Cosa fa il programma quando utilizzato

optional arguments:
  -h, --help            show this help message and exit
  -n NOME_ESTESO, --nome_esteso NOME_ESTESO
                        Descrizione del parametro
  -b, --boolean_value   imposta il valore 'True' se trova il parametro
  -d CON_DEFAULT, --con_default CON_DEFAULT
                        Parametro che ha già un valore di default se non viene
                        fornito l'argomento

Altre informazioni come Autore o data
"""