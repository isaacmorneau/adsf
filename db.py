from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models


class DB:
    def __init__(self, echo=False):
        self.engine = create_engine(
            f"sqlite:///adsf.db", echo=echo
        )
        self.metadata = models.metadata

    def session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    def create_db(self):
        self.metadata.create_all(self.engine)
