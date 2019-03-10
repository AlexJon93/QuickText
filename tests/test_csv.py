import pytest
from csv_reader import csv_reader

def test_csv_parse():
    vals = ['Alex', 'Jarvis','s3607170','0406 851347','alex.jon.jarvis@gmail.com']
    try:
        file = open('tests/csv_tests/valid_test_data1.csv')
    except IOError as e:
        print(str(e))
        assert False
    result = csv_reader.csv_parse(file)
    assert result[0].valList() == vals

def test_csv_parse_fail():
    try:
        file = open('tests/csv_tests/invalid_test_data1.csv')
    except IOError as e:
        print(str(e))
        assert  False
    assert csv_reader.csv_parse(file) is None

def test_csv_validate_name():
    assert csv_reader.csv_validate_name('Alex Jarvis')

def test_csv_validate_phone():
    assert csv_reader.csv_validate_phone('0412 345 678')

def test_csv_validate_student_number():
    assert csv_reader.csv_validate_student_number('s3607170')

def test_csv_validate_student_number2():
    assert csv_reader.csv_validate_student_number('3607170')

def test_csv_validate_student_number3():
    assert csv_reader.csv_validate_student_number('S3607170')

def test_csv_validate_email():
    assert csv_reader.csv_validate_email('test@email.com') is not None

def test_csv_validate_email_fail():
    assert csv_reader.csv_validate_email('test@email@fail.com') is None

def test_csv_validate_items():
    member = {
        'name': 'Alex Jarvis',
        'student number': 's3607170',
        'phone number': '0412345678',
        'email': 'test@email.com',
        'tocall': 'y'
    }
    assert csv_reader.csv_validate_items(member)