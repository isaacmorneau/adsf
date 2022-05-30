from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models


class DB:
    def __init__(self, echo=False):
        self.engine = create_engine(
            f"sqlite:///adsf.db", echo=echo
        )

    def session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

