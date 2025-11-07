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
