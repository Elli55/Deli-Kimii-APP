import sys
from pathlib import Path
import csv
import datetime
import uuid
from . import doing

 

# # data_dir = base_dir / 'datas'
EXPENSE_DIR = doing.DATA_DIR/ 'expenses.csv'
INCOME_DIR = doing.DATA_DIR / 'income.csv'
DEBIT_DIR = doing.DATA_DIR/ 'debt.csv'

def set_data_dir_fi(new_base):
    global EXPENSE_DIR, INCOME_DIR, DEBIT_DIR

    doing.DATA_DIR = Path(new_base)
    EXPENSE_DIR = doing.DATA_DIR/ 'expenses.csv'
    INCOME_DIR = doing.DATA_DIR / 'income.csv'
    DEBIT_DIR = doing.DATA_DIR/ 'debt.csv'
    

_name = 'Ad'
_date = 'Tarix'
_amount = 'Məbləğ'
_live_time = 'YazılmaVaxtı'
_category = 'Kateqoriya'
_id = 'ID'
_deadline = 'SonÖdəməTarixi'
_source = 'Mənbə'




def created_time_and_uniq_id(group=''):

    # 2 dəyişən verir,1cisi həminki anı,2ci unikal 8 xanalı bir İD. 
    # CSVləri yazarkən istifadə üçün əlavə edirəm
    
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f'{group}{uuid.uuid4().hex[:8]}'
    

    

def write_expenses(Name, Date, Amount, Category): 
    doing.DATA_DIR.mkdir(exist_ok=True)
    if  not EXPENSE_DIR.exists():
        

        with open(EXPENSE_DIR, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([_id,_name, _date, _amount, _category, _live_time])
    created_time, uniq_id   = created_time_and_uniq_id(group='XRC-')
   
    with open(EXPENSE_DIR, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([uniq_id,Name , Date,Amount, Category, created_time])


def write_income(Name, Date, Amount, Source ):
    doing.DATA_DIR.mkdir(exist_ok=True)
    if not INCOME_DIR.exists():
        
        with open(INCOME_DIR, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([_id,_name, _date, _amount,  _source, _live_time])
    creeated_time, uniq_id =created_time_and_uniq_id('INC-')
    with open(INCOME_DIR, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([ uniq_id ,Name, Date, Amount, Source, creeated_time])

def write_debit(Name, Amount, Category, Deadline):
    doing.DATA_DIR.mkdir(exist_ok=True)
 
    if not DEBIT_DIR.exists():

        with open(DEBIT_DIR, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([_id, _name, _amount, _category, _deadline, _live_time])
    created_time, uniq_id = created_time_and_uniq_id('DBT-')
    with open(DEBIT_DIR, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([uniq_id,Name, Amount, Category, Deadline, created_time])

def pay_debit(name, category): 
    if not DEBIT_DIR.exists():
        return
    removed_debit = None
    debits = []
    with open(DEBIT_DIR, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header:
            debits.append(header)
        
        for line in reader:
            if line and line[1] != name:  
                debits.append(line)
            else:
                removed_debit = line
    created_time, uniq_id = created_time_and_uniq_id('EXP-')            
    if removed_debit:
        with open(EXPENSE_DIR, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([  uniq_id, removed_debit[1],datetime.date.today().isoformat(), removed_debit[2], category, created_time])     

    with open(DEBIT_DIR, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f) 
        writer.writerows(debits)
    



def get_debits_list():
    #borc adları siyahılanır silmək üçün conboboxda 
    if not DEBIT_DIR.exists():
        return []
    names = []

    with open(DEBIT_DIR, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            if line:
                names.append(line[1])
    return names



def calculate_wallet():
    income = 0
    expenses = 0
    if INCOME_DIR.exists():
        with open(INCOME_DIR, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for line in reader:
                if line:
                    income += float(line[3])

    if EXPENSE_DIR.exists():
        with open(EXPENSE_DIR, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for line in reader:
                if line:
                    expenses += float(line[3])

    return income - expenses

def calculate_total_debits():

    total_debit = 0
    if EXPENSE_DIR.exists():
        with open(EXPENSE_DIR, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for line in reader:
                total_debit += float(line.get(_amount))

    return total_debit        

