class Osoba:
    def __init__(self, imię, nazwisko):
        self.imię = imię
        self.nazwisko = nazwisko

    def przedstaw_się(self):
        print(f'Nazywam się {self.imię} {self.nazwisko}')


person1 = Osoba('John', 'Doe')
person1.przedstaw_się()

person2 = Osoba('Mary', 'Poppins')
person2.przedstaw_się()

person3 = Osoba()
person3.przedstaw_się()