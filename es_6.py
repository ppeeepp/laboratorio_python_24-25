import json
import os
#Riscrivete l’esercizio 3 della rubrica sotto forma di “classe”:
# 1) in un file separato, create una classe rubrica
class Rubrica:
    """
    la classe rubrica deve fare 5 azioni:
    1 aprire una rubrica leggendola da un file (JSON oppure testo) - APRI
    2 aggiungere un elemento alla rubrica - AGGIUNGI
    3 rimuovere un elemento dalla rubrica (dato il nome) - RIMUOVI
    4 salvare la rubrica su un file (JSON o testo) - SALVA
    5 stampare tutte le informazioni di un contatto (data il nome), come nell’eserczio 3 - STAMPA
    la classe rubrica deve inizializzarsi con un dizionario (come nell’esercizio 3)
    """
    def __init__(self, contacts=None):
        self.contacts = contacts if contacts else {}
        self.open = bool(contacts)
    # la classe rubrica deve avere un classmethod per inizializzarla con un file JSON
    @classmethod
    def open_json(cls, filepath):
        with open(filepath, 'r') as jsonfile:
            contacts = json.load(jsonfile)
            return cls(contacts)
    # la classe rubrica deve avere un classmethod per inizializzarla con un file testo
    @classmethod
    def open_txt(cls, filepath):
        contacts = {}
        with open(filepath, 'r') as f:
            for line_num, line in enumerate(f, start=1):
                parts = line.strip().split(', ')
                if len(parts) != 7:
                    print(f'Riga malformattata alla linea {line_num}: "{line.strip()}"')
                    continue
                nome, giorno, mese, anno, eta, sesso, mail = parts
                try:
                    contacts[nome] = {
                        'giorno': int(giorno),
                        'mese': mese,
                        'anno': int(anno),
                        'età': int(eta),
                        'sesso': sesso,
                        'mail': mail
                    }
                except ValueError as e:
                    print(f'Errore nei dati numerici alla linea {line_num}: {e}')
            return cls(contacts)
    # Per “aggiungere un elemento”, bisogna aver prima aperto una rubrica, altrimenti si ottine un messaggio di errore “Prima apri una rubrica”
    def add(self, name, data):
        if not self.open:
            print('Prima apri una rubrica')
            return
        self.contacts[name] = data
        print(f"Contatto '{name}' aggiunto.")
    # Per “rimuovere un elemento”, deve esserci almeno un elemento nella rubrica altrimenti si ottine un messaggio di errore “La rubrica è vuota”.
    # Se l’elemento da rimuovere non esiste, il messaggio di errore sarà “Il contatto NOME non esiste in rubrica”
    def remove(self, name):
        if not self.contacts:
            print('La rubrica è vuota')
            return
        if name not in self.contacts:
            print(f'{name} non esiste in rubrica')
            return
        del self.contacts[name]
        print(f'{name} rimosso.')
    # Per “stampare le informazioni”, deve esserci almeno un elemento nella rubrica altrimenti si ottine un messaggio di errore “La rubrica è vuota”.
    # Se l’elemento da rimuovere non esiste, il messaggio di errore sarà “Il contatto NOME non esiste in rubrica”
    def stampa(self, nome):
        if not self.contacts:
            print('La rubrica è vuota')
            return
        if nome not in self.contacts:
            print(f'{nome} non esiste in rubrica')
            return
        contact = self.contacts[nome]
        print(f'Nome: {nome}')
        print(f'Giorno: {contact['giorno']}')
        print(f'Mese: {contact['mese']}')
        print(f'Anno: {contact['anno']}')
        print(f'Età: {contact['età']}')
        print(f'Sesso: {contact['sesso']}')
        print(f'Email: {contact['mail']}')
    # Per salvare la rubrica su file (JSON o txt deciso dall’estensione del nome del file), la rubrica non deve essere vuota,
    # altrimenti si ottine un messaggio di errore “La rubrica è vuota”
    def save(self, filepath):
        if not self.contacts:
            print('La rubrica è vuota')
            return
        ext = os.path.splitext(filepath)[-1].lower()
        try:
            with open(filepath, 'w') as file:
                if ext == '.json':
                    json.dump(self.contacts, file, indent=2)
                else:
                    for nome, data in self.contacts.items():
                        file.write(f'{nome}: {data}')
            print(f'Rubrica salvata in {filepath}')
        except Exception as e:
            print(f'Errore: {e}')

def main():
    # 1 - apertura da file JSON
    try:
        rubrica_json = Rubrica.open_json('Lezioni/rubrica.json')
        print('Rubrica da JSON aperta correttamente')
    except Exception as e:
        print(f'Errore: {e}')
        rubrica_json = Rubrica()
    # 2 - aggiunta di un nuovo contatto
    new = {
        'giorno': 15,
        'mese': 'Giugno',
        'anno': 1990,
        'età': 34,
        'sesso': 'M',
        'mail': 'javier.zanetti@inter.it'
    }
    rubrica_json.add('Javier Zanetti', new)
    # 3 - stampa contatto esistente
    rubrica_json.stampa('Javier Zanetti')
    # 4 - stampa contatto non esistente
    rubrica_json.stampa('Juventino Onesto')
    # 5 - rimozione contatto esistente
    rubrica_json.remove('Javier Zanetti')
    # 6 - rimozione contatto non esistente
    rubrica_json.remove('Juventino Onesto')
    # 7 - salvataggio rubrica JSON
    rubrica_json.save('rubrica_new.json')
    # 8 - apertura da file TXT
    try:
        rubrica_txt = Rubrica.open_txt('rubrica_new.txt')
        print('Rubrica da txt aperta correttamente')
    except Exception as e:
        print(f'Errore: {e}')
        rubrica_txt = Rubrica()
    # 9 - salvataggio rubrica TXT
    rubrica_txt.save('rubrica_new.txt')
    # 10 - operazioni su rubrica vuota
    rubrica_empty = Rubrica()
    rubrica_empty.add('Test', new)
    rubrica_empty.remove('Test')
    rubrica_empty.stampa('Test')
    rubrica_empty.save('empty.txt')

main()
