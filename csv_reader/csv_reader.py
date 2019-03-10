from models import member
import csv
import re

def csv_parse(csvfile):
    csv_reader = csv.DictReader(csvfile)
    mem_list = []
    for row in csv_reader:
        try:
            if(csv_validate_items(row)):
                first_name = row['name'].split()[0]
                surname = ''.join(row['name'].split()[1:])
                mem_list.append(member.Member(first_name, surname, row['student number'], row['phone number'], row['email']))
        except KeyError:
            print('Given csv file does not contain one of the following fields: name, student number, phone number, or email')
            return 
    return mem_list

def csv_validate_items(member):
    if csv_validate_call(member['tocall']):
        return (
            csv_validate_name(member['name']) and
            csv_validate_student_number(member['student number']) and
            csv_validate_phone(member['phone number']) and
            csv_validate_email(member['email'])
        )
    return False

def csv_validate_name(name):
    name = name.replace(' ', '')
    return name.isalpha()

def csv_validate_phone(number):
    number = number.replace(' ', '')
    return number.isdigit() and number[0:2] == '04' and len(number) == 10

def csv_validate_student_number(number):
    number = number.replace(' ', '')
    return ((number[0] == 's' or number[0] == 'S') and number[1:].isdigit()) or (number.isdigit())

def csv_validate_email(email):
    return re.match(r'[^@]+@[^@]+\.[^@]+', email)

def csv_validate_call(call):
    return call.lower() == 'yes' or call.lower() == 'y' or call == '1'