class Member:
    def __init__(self, firstname, surname, student_number, phone, email):
        self.firstname = firstname
        self.surname = surname
        self.student_number = student_number
        self.phone = phone
        self.email = email

    def __repr__(self):
        return ','.join([self.firstname, self.surname, self.student_number, self.phone, self.email])

    def valList(self):
        return [self.firstname, self.surname, self.student_number, self.phone, self.email]