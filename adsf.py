#!/bin/python3
import models
import db as pdb
import api as papi
import isbnlib
import argparse

def inventory(api):
    while True:
        try:
            raw_isbn = input('isbn: ')
        except:
            print()
            break
        isbn = isbnlib.clean(raw_isbn)
        book = api.book_by_isbn(isbn)
        if book:
            print(f"already scanned '{book.title}'")
            continue

        if isbnlib.notisbn(isbn):
            print("invalid isbn")
            continue
        meta = isbnlib.meta(isbn)
        title = meta['Title']
        desc = isbnlib.desc(isbn)
        book_id = api.book_create(isbn=isbn, title=title, description=desc)
        print(f"created '{title}' with id {book_id}")


def init(db):
    db.create_db()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ADSF book tracker thing')
    parser.add_argument('mode', help='the mode to run the tool ing', choices=['init', 'inventory', 'report'])
    args = parser.parse_args()

    db = pdb.DB()
    api = papi.Api(db)

    if args.mode == 'inventory':
        inventory(api)
    elif args.mode == 'init':
        init(db)
