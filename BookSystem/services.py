from django.contrib.auth.models import User

from BookSystem.models import Category, Author, Publisher, Book, Reader


class CategoryService:

    @staticmethod
    def getAll():
        return Category.objects.all()

    @staticmethod
    def getById(id):
        return Category.objects.get(pk=id)

    @staticmethod
    def add(name):
        c = Category(name=name)
        c.save()


class AuthorService:

    @staticmethod
    def getAll():
        return Author.objects.all()

    @staticmethod
    def getById(id):
        return Author.objects.get(id)

    @staticmethod
    def add(first_name, last_name, type):
        a = Author(first_name=first_name, last_name=last_name, type=type)
        a.save()


class PublisherService:

    @staticmethod
    def getAll():
        return Publisher.objects.all()

    @staticmethod
    def getById(id):
        return Publisher.objects.get(id)

    @staticmethod
    def add(name, country):
        a = Publisher(name=name, country=country)
        a.save()


class BookService:

    @staticmethod
    def getAll():
        return Book.objects.all().filter(isApproved=True)


    @staticmethod
    def add(title, description, publication_date, categoryId, publisherId, authorsIds, isApproved):
        category = Category.objects.get(pk = categoryId)
        publisher = Publisher.objects.get(pk = publisherId)
        authors = Author.objects.filter(pk__in = authorsIds)

        b = Book(title=title, description=description, publication_date=publication_date,
                 category=category, publisher=publisher, isApproved = isApproved)
        b.save()
        b.authors.add(*authors)

    @staticmethod
    def getBooksInCategory(id):
        return Book.objects.filter(category__id=id)

    @staticmethod
    def addReadBook(book_id, user_id):
        reader = Reader.objects.get(pk=user_id)
        reader.books.add(Book.objects.get(id=book_id))

    @staticmethod
    def getReadBooksForUser(user_id):
        return User.objects.all().get(pk = user_id).reader.books.all()

    @staticmethod
    def getBooksForApproval():
        return Book.objects.all().filter(isApproved=False)

    @staticmethod
    def approveBook(id):
        book  = Book.objects.filter(pk=id)
        if book is None:
            return False
        book.update(isApproved = True)
        return True

    @staticmethod
    def getBook(id):
        return Book.objects.get(pk=id)

    @staticmethod
    def editBook(id, title,  description, publication_date, categoryId, publisherId, authorsIds):
      book = BookService.getBook(id)
      if book is None:
          return False

      book.title = title
      book.description = description
      book.publication_date = publication_date
      book.category_id = categoryId
      book.publisher_id = publisherId

      authors = Author.objects.filter(pk__in=authorsIds)
      book.authors.add(*authors)

      book.save()

      return True

    @staticmethod
    def deleteBook(id):
        book = BookService.getBook(id)
        if book is None:
            return False

        Book.objects.all().filter(pk=id).delete()
        return True

    @staticmethod
    def getBookAuthors(id):
        authors = Book.objects.get(pk = id).authors.all()
        return authors


class UserService:

    @staticmethod
    def add_user(first_name, last_name, email, country, username, password):
        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        reader = Reader(country = country, user = user)
        reader.save()




