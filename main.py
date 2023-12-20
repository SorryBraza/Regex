from application import processing

if __name__ == '__main__':
    db_path = "db/phonebook_raw.csv"
    contact_list = processing.get_contacts(db_path)
    processing.process_fio(contact_list)
    contact_list = processing.process_phone(contact_list)
    contact_list = processing.process_contact_list(contact_list)
    new_db_path = "db/phonebook.csv"
    processing.save_process_contacts(new_db_path, contact_list)