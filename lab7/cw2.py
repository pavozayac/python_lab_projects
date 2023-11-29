class Osoba:
    def __init__(self, imię, nazwisko):
        self.imię = imię
        self.nazwisko = nazwisko

    def przedstaw_się(self):
        print(f'Nazywam się {self.imię} {self.nazwisko}')
    
    def __repr__(self) -> str:
        return f'\b\b\b{self.imię} {self.nazwisko}'

os = Osoba('Ambroży', 'Kleks')

print(f'{os=}')

print(f'{os=}' == 'Ambroży Kleks')