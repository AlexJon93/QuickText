from sys import argv
from models import member

def generate_message(member):
    print('Hey there', member.firstname)

def parse_text(file):
    

if __name__ == '__main__':
    new_dude = member.Member('Phoebe', 'Sawyer', 's132156', '0412828374', 'test@test.com')
    generate_message(new_dude)