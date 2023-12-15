from abc import ABC, abstractmethod
from json import dump, load

class Item(ABC):
    def __init__(self, title, creator, year) -> None:
        self.title = title
        self.creator = creator
        self.year = year
    
    @abstractmethod
    def display_info(self) -> str:
        return f'Title: {self.title} \nCreator: {self.creator}\nYear: {self.year}\n'
    
    
class Book(Item):
    def __init__(self, title, creator, year, genre, isbn):
        super().__init__(title, creator, year)
        self.genre = genre
        self.isbn = isbn
    
    def display_info(self) -> str:
        return super().display_info() + f'Genre: {self.genre}\nISBN: {self.isbn}'
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, self.__class__):
            return False
        
        return self.title == __value.title and self.creator == __value.creator \
            and self.year == __value.year and self.genre == __value.genre \
            and self.isbn == __value.isbn

class Movie(Item):
    def __init__(self, title, creator, year, genre, duration):
        super().__init__(title, creator, year)
        self.genre = genre
        self.duration = duration
    
    def display_info(self) -> str:
        return super().display_info() + f'Genre: {self.genre}\nDuration: {self.duration}'

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, self.__class__):
            return False
        
        return self.title == __value.title and self.creator == __value.creator \
            and self.year == __value.year and self.genre == __value.genre \
            and self.duration == __value.duration
    
class Library:
    def __init__(self) -> None:
        self.items: list[Item] = []

    def add_item(self, item: Item):
        self.items.append(item)
    
    def display_items(self):
        for item in self.items:
            print(item.display_info(), end='\n\n')

    def save_to_file(self, fname: str):
        with open(fname, 'w') as jsonfile:
            dump(list(map(lambda i: i.__dict__ | {'kind': i.__class__.__name__}, self.items)), jsonfile)
            
    def load_from_file(self, fname: str):
        with open(fname, 'r') as jsonfile:
            items_list = load(jsonfile)
            
            for item in items_list:
                if item['kind'] == Movie.__name__:
                    self.items.append(Movie(item['title'], item['creator'], item['year'], item['genre'], item['duration']))
        
                if item['kind'] == Book.__name__:
                    self.items.append(Book(item['title'], item['creator'], item['year'], item['genre'], item['isbn']))
    
    def recommend(self, item: Item) -> Item | None:
        recommendation = None
        
        for i in self.items:
            if i.__class__ == item.__class__ and i.genre == item.genre and not (i == item):
                recommendation = i
            
        return recommendation
        
    
if __name__ == '__main__':
    library = Library()

    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", "978-3-16-148410-0")
    movie = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi", 148)

    library.add_item(book)
    library.add_item(movie)


    # Wyświetl informacje o przedmiotach w bibliotece
    library.display_items()

    library.save_to_file("library_data.json")

    new_library = Library()
    new_library.load_from_file("library_data.json")

    # # Wyświetl informacje o przedmiotach w nowej bibliotece
    new_library.display_items()

    movie2 = Movie("Interstellar", "Christopher Nolan", 2014, "Sci-Fi", 169)
    movie3 = Movie("Shutter Island", "Martin Scorsese", 2010, "Mystery", 138)

    new_library.add_item(movie2)
    new_library.add_item(movie3)

    print('Recommendation: \n' + new_library.recommend(movie).display_info())


