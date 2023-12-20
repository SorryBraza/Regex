from pprint import pprint
import re
import csv
phone_pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
phone_sub = r'+7(\2)-\3-\4-\5 \6\7'


def get_contacts(db_path):
    with open(db_path, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def save_process_contacts(db_path, data):
    with open(db_path, "w", encoding="utf-8", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(data)

def process_fio(data):
    for i in range(len(data)):
        fio = " ".join(data[i][:2]).rstrip().split(" ")
        try:    
            for j in range(3):
                data[i][j] = fio[j]
        except IndexError:
            continue

def process_phone(data):
    contact_list = list()
    for contact in data:
        contact_db = ",".join(contact)
        contact_db = re.sub(phone_pattern, phone_sub, contact_db).rstrip().split(",")
        contact_list.append(contact_db)
    return contact_list

def merge_doubles(contact_one, contact_two):
    contact = list()
    for index in range(len(contact_one)):
        contact.append(contact_one[index]) if contact_one[index] else contact.append(contact_two[index])
    return contact

def process_contact_list(data):
    contact_list = dict()
    for item in data:
        contact_list[" ".join(item[:2])] = merge_doubles(item, contact_list[" ".join(item[:2])]) if " ".join(item[:2]) in contact_list else item
    return list(contact_list.values())