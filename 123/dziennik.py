from datetime import datetime
import os

def check_file_exists(file_path):
    return os.path.exists(file_path)


def read_journal(file_path):
    with open(file_path,'r') as file:
        return file.readlines() 
    

def save_journal(journal):
    with open(file_path,'w') as file:
        for linia in journal:
            file.write(linia)

def display_journal():
    print(read_journal(file_path))

def check_date(date):
    format = "%Y-%m-%d %H:%M:%S"
    try:
        datetime.strptime(date,format)
        return True
    except ValueError:
        print("invalid date")
        return False
    

def add_journal_entry(task_name, task_description, date):
    if check_date(date) == False:
        return False

    journal = read_journal(file_path)
    for line in journal:
        if date in line:
            print("Task is already existing")
            return False
    
    with open(file_path, 'a') as file: 
        file.write(f"{task_name};{task_description}:{date}\n")
        print("Task saved")
        return True
    

def del_journal_entry(date):
    if not check_date(date):
        return False
    try:
        journal = read_journal(file_path)
        to_be_del = None
        for line in journal:
            if date in line:
                to_be_del = line
        if to_be_del != None:
            journal.remove(to_be_del)
            save_journal(journal)
            print("entry has been removed")
        else:
            print("Entry does not exist")
        
    except FileNotFoundError:
        print("File does not exist")
        return False
    


def modify_entry(old_date, new_task_name, new_task_description, new_date):
    if not check_date(old_date):
        return False
    else:
        journal = read_journal(file_path)
        for line in journal:
            if old_date in line:
                journal.remove(line)
                journal.append(f"{new_task_name};{new_task_description};{new_date}\n")
        save_journal(journal)
        print("Tasked change successfully")
    
file_path = "journal.txt"


add_journal_entry("przepis","robienie kotlekow","2023-12-17 11:57:30")
# del_journal_entry("2023-12-17 11:11:30")
# modify_entry("2023-12123-17 11:06:30","Zupa","Zrobic zupe","2023-12-17 11:11:30")
display_journal()