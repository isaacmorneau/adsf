import models
import sqlalchemy as sqa
from sqlalchemy import func


class Api:
    def __init__(self, db):
        self.db = db
        self.engine = self.db.engine
        self.session = db.session()

    def create_db(self):
        models.Base.metadata.create_all(self.engine)

    def commit(self):
        self.session.commit()

    def book_by_isbn(self, isbn):
        res = self.session.query(models.BookModel).where(models.BookModel.isbn == isbn).first()
        if res:
            return res
        return None

    def book_create(self, book, commit=True):
        res = self.session.add(book)
        if commit:
            self.session.commit()
        return book.id

    def book_update(self, book, commit=True):
        res = self.session.add(book)
        if commit:
            self.session.commit()
        return book.id

    def find_container_by_book(self, title):
        book = self.session.query(models.BookModel).where(models.BookModel.title.ilike(title)).first()
        if not book:
            return None
        return book.location

    def location_by_barcode(self, barcode):
        res = self.session.query(models.LocationModel).where(models.LocationModel.barcode == barcode).first()
        if res:
            return res
        return None

    def location_create(self, location, commit=True):
        res = self.session.add(location)
        if commit:
            self.session.commit()
        return location.id
