import models
import sqlalchemy as sqa
from sqlalchemy import func


class Api:
    def __init__(self, db):
        self.db = db
        self.engine = self.db.engine
        self.session = db.session()

    def commit(self):
        self.session.commit()

    def book_by_isbn(self, isbn):
        sel = models.book.select().where(models.book.c.isbn == isbn)
        res = self.session.execute(sel).first()
        if res:
            return res
        return None

    def book_create(self, commit=True, **properties):
        ins = models.book.insert().values(**properties)
        res = self.session.execute(ins)
        if commit:
            self.session.commit()
        return res.inserted_primary_key[0]
