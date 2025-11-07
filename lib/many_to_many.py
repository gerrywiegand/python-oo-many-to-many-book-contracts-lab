class Author:
    all = []

    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name must be a string")
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        if isinstance(title, str):
            self.title = title
        else:
            raise TypeError("Title must be a string")
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, (int, float)):
            raise TypeError("royalties must be a number")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an instance of Author")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise TypeError("book must be an instance of Book")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("royalties must be a number")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
