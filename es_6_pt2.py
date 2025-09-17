# 2) In un file separato importate la classe rubrica appena creata
import es_6
from es_6 import Rubrica
# e scrivete un programma che in modo interattivo chieda all’utente
# di quale delle 5 operazioni della classe rubrica svolgere.
def main_menu():
    print('Operazioni disponibili:')
    print('1 - APRI')
    print('2 - AGGIUNGI')
    print('3 - RIMUOVI')
    print('4 - SALVA')
    print('5 - STAMPA')
    print('0 - EXIT - esci.')

def main():
    rubrica = None
    # Se l’azione richiesta non esiste, il programma continua a chiedere l’azione da svolgere
    while True:
        main_menu()
        user_input = input('Seleziona un\'azione da effettuare. ').upper()
        match user_input:
            case 'APRI' | '1':          # OR
                filepath = input('Inserisci il percorso del file, in formato .json o .txt ').strip()
                if filepath.endswith('.json'):
                    rubrica = Rubrica.open_json(filepath)
                elif filepath.endswith('.txt'):
                    rubrica = Rubrica.open_txt(filepath)
                else:
                    print('Formato non supportato.')
            case 'AGGIUNGI' | '2':      # OR
                if not rubrica:
                    print('Prima apri una rubrica.')
                    continue
                nome = input('Nome del contatto: ')
                try:
                    giorno = int(input('Giorno di nascita: '))
                    mese = input('Mese di nascita: ')
                    anno = int(input('Anno di nascita: '))
                    eta = int(input('Età: '))
                    sesso = input('Sesso (M/F): ').upper()
                    mail = input('Email: ')
                    data = {
                        'giorno': giorno,
                        'mese': mese,
                        'anno': anno,
                        'età': eta,
                        'sesso': sesso,
                        'mail': mail
                    }
                    rubrica.add(nome, data)
                except ValueError:
                    print('Dati non validi!')
            case 'RIMUOVI' | '3':
                if not rubrica:
                    print('Prima apri una rubrica.')
                    continue
                nome = input('Nome del contatto da rimuovere: ')
                rubrica.remove(nome)
            case 'SALVA' | '4':
                if not rubrica:
                    print('Prima apri una rubrica.')
                    continue
                filepath = input('Nome del file di destinazione in formato .json o .txt: ').strip()
                rubrica.save(filepath)
            case 'STAMPA' | '5':
                if not rubrica:
                    print('Prima apri una rubrica.')
                    continue
                nome = input('Nome del contatto da stampare: ')
                rubrica.stampa(nome)
            # finchè non viene indicata la stringa “EXIT”
            case 'EXIT' | '0':
                print('EXIT - Chiusura')
                break
            case _:
                print('Azione non riconosciuta')

main()