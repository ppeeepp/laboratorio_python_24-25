import sys
import argparse

rubrica = {
  'Paolino Paperino': {'giorno': 9,
                      'mese': 'giugno',
                      'anno': 1934,
                      'età': 89,
                      'sesso': 'M',
                      'mail': 'paolino.paperin0@disney.org'},
  'Ron Weasley': {'giorno': 1,
                'mese': 'marzo',
                'anno': 1980,
                'età': 43,
                'sesso': 'M',
                'mail': 'ron_weasley80@hogwards.uk'},
  'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 19, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
  'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 54, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}
# 1) Partendo dal dizionario annidato rubrica, visualizzate il contenuto del dizionario
# stampando a schermo delle stringhe formattate che contengano la chiave ed il valor di ognuno degli elementi
# (Esempio: ‘Paolino Paperino’, ‘giorno’ 9, ‘mese’ ‘giugno’, …)
def view_dict_content(input_dict):
    for name, details in input_dict.items():
        print(f'"{name}":', end=' ')
        details = [f'"{key}" {value}' for key, value in details.items()]
        print(', '.join(details))

# 2) A partire dalla rubrica, costruire la lista delle età, ordinata in ordine crescente
# e visualizzate i nomi in ordine crescente di età
def get_age(age_tuple):
    return age_tuple[1]['età']
def view_sorted_ages(rubrica_dict):
    sorted_items = sorted(rubrica_dict.items(), key=get_age)
    sorted_ages = [dati['età'] for _, dati in sorted_items]
    sorted_age_names = [nome for nome, _ in sorted_items]
    return sorted_ages, sorted_age_names

# 3) Invertire l’ordine della lista precedentemente costruita e visualizzatela
def invert_list(rubrica_dict):
    age, names = view_sorted_ages(rubrica_dict)
    age.reverse()
    names.reverse()
    print(age, names)

# 4) Utilizzare la rubrica e scrivere su schermo per OGNI membro della rubrica, il seguente messaggio:
'''Car[o/a] [Nome],
sei nat[o/a] il [giorno] di [mese] del [anno] e quindi a breve compirai [età] anni.
Ti manderemo gli auguri a [mail]'''
# dove [o/a] deve essere adattato all’attributo [M/F]
def send_custom_msg(rubrica_input, name=None):
    if name:
        if name in rubrica_input:
            details = rubrica_input[name]
            if details['sesso'] == 'M':
                suffix = 'o'
            else:
                suffix = 'a'
            print(f"Car{suffix} {name},\n"
                  f"sei nat{suffix} il {details['giorno']} di {details['mese']} del {details['anno']} e quindi a breve compirai {details['età']} anni.\n"
                  f"Ti manderemo gli auguri a {details['mail']}\n")

    else:
        for name, details in rubrica_input.items():
            if details['sesso'] == 'M':
                suffix = 'o'
            else:
                suffix = 'a'
            print(f"Car{suffix} {name},\n"
                    f"sei nat{suffix} il {details['giorno']} di {details['mese']} del {details['anno']} e quindi a breve compirai {details['età']} anni.\n"
                    f"Ti manderemo gli auguri a {details['mail']}"
                    f"\n")

# 5) Utilizzando args passate in input al vostro programma una chiave [giorno, mese, anno, età, sesso, mail]
# e visualizzate tutto il contenuto della rubrica (valori) che corrispondono a questa chiave
def view_by_key(rubrica_input, key):
    if len(sys.argv) != 2:
        raise AttributeError('Chiave non inserita correttamente')
    # key = sys.argv[1]     commentato per coerenza con l'options_menu.
    #                       Per il solo punto 3 non c'è il parametro di input nella funzione.
    for name, details in rubrica_input.items():
        if key in details:
            return f'- {name}: {details[key]}'
        else:
            return f'Chiave {key} non trovata.'

# 6) Utilizzando argparse visualizzate la stringa al punto 4 SOLO per il nome fornito come opzione al vostro programma
# (esempio: python esercizio_3.py –nome ‘Madoka Ayukawa’ –> esegue punto 4 solo per il nome indicato)
def custom_message_with_argparser():
    parser = argparse.ArgumentParser(description='Invio di un messaggio personalizzato a un componente della rubrica')
    parser.add_argument('-name', type=str, help='Nome del contatto che voglio visualizzare')
    args = parser.parse_args()
    # ho modificato la funzione send_custom_msg aggiungendo un secondo parametro di input 'name=None' con un controllo iniziale
    send_custom_msg(rubrica, name=args.name)

# 7) Utilizzando argparse introducede delle opzioni al vostro programma per eseguire i punti 1, 2, 3, 4, 5 dell’esercizio
# (esempio: python esercizio_3.py –lista_ordinata –> esegue il punto 2 dell’esercizio)
def options_menu():
    parser = argparse.ArgumentParser(description='Serie di comandi per la scelta di che azione si vuole compiere')
    parser.add_argument('-name', type=str, help='Nome del contatto che voglio visualizzare')
    parser.add_argument('--view', action='store_true', help='Visualizza tutti i dati della rubrica')
    parser.add_argument('--list_age', action='store_true', help='Lista età in ordine crescente')
    parser.add_argument('--list_age_desc', action='store_true', help='Lista età in ordine decrescente')
    parser.add_argument('--msg', action='store_true', help='Messaggio a tutti')
    parser.add_argument('--value_from_key', type=str, help='Visualizza valori della chiave richiesta')
    parser.add_argument('--msg_spec', action='store_true', help='Messaggio solo al nome passato con -name')
    args = parser.parse_args()
    if args.view:
        view_dict_content(rubrica)
    elif args.list_age:
        age, names = view_sorted_ages(rubrica)
        print(age, names)
    elif args.list_age_desc:
        invert_list(rubrica)
    elif args.msg:
        send_custom_msg(rubrica)
    elif args.value_from_key:
        view_by_key(rubrica, args.value_by_key)
    elif args.msg_spec:
        if args.name:
            send_custom_msg(rubrica, args.name)
        else:
            print("Errore: usa -name per specificare il contatto")
    else:
        print("Nessuna opzione valida specificata.")


if __name__ == '__main__':
    options_menu()
