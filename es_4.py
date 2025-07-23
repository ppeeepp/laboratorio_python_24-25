import es_3
from es_3 import rubrica, view_dict_content
import json

# 1) aggiungete una opzione al programma per generare un file di testo rubrica.txt
# contenente tutti gli elmenti della rubrica, uno per linea, con tutte le informazioni separate da virgole.
def export_to_txt(input_dict, filename):
    with open(filename, 'w') as f:
        for name, details in input_dict.items():
            line = f'{name}, {details['giorno']}, {details['mese']}, {details['anno']}, {details['età']}, {details['sesso']}, {details['mail']}'
            f.write(line + '\n')
# 2) Create un file JSON che contiene la rubrica con la stessa struttura del dizionario interno al programma
def export_to_json(input_dict, filename):
    with open(filename, 'w') as f:
        json.dump(input_dict, f, indent=4)

# 3) Leggete la rubrica salvata in un file formato JSON e visualizzate tutto il contenuto
def read_json(filename):
    try:
        with open(filename, 'r') as f:
            print(es_3.view_dict_content(json.load(f)))
    except FileNotFoundError:
        print(f'File {filename} non trovato')
    except json.JSONDecodeError:
        print(f'Il file {filename} non è un JSON valido')

if __name__ == '__main__':
    export_to_txt(rubrica, 'Lezioni/rubrica.txt')
    export_to_json(rubrica, 'Lezioni/rubrica.json')
    read_json('Lezioni/rubrica.json')




