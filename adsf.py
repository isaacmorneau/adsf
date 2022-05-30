#!/bin/python3
import models
import db as pdb
import api as papi
import isbnlib
import argparse

def link(api):
    container_code = input('container code: ').strip()
    location = api.location_by_barcode(container_code)
    if not location:
        location = models.LocationModel()
        location.barcode = container_code
        api.location_create(location)
    while True:
        try:
            raw_isbn = input('isbn: ')
        except:
            print()
            break

        isbn = isbnlib.clean(raw_isbn)
        book = api.book_by_isbn(isbn)

        if not book:
            if isbnlib.notisbn(isbn):
                print("invalid isbn")
                continue
            meta = isbnlib.meta(isbn)
            title = meta['Title']
            desc = isbnlib.desc(isbn)
            book = models.BookModel()
            book.isbn = isbn
            book.title = title
            book.description = desc
            book.location = location
            api.book_create(book)
            print(f"created book '{book.title}'")
        else:
            book.location = location
            api.book_update(book)
            print(f"linked book '{book.title}'")
def findloc(api):
    book_title = input('book title: ').strip()
    if '%' not in book_title:
        book_title = f"%{book_title}%"
    location = api.find_container_by_book(book_title)
    if location:
        if location.description:
            print(f"book in {location.barcode} - {location.description}")
        else:
            print(f"book in {location.barcode}")
    else:
        print("book not found")

def init(api):
    api.create_db()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ADSF book tracker thing')
    parser.add_argument('mode', help='the mode to run the tool in', choices=['init', 'link', 'findloc'])
    args = parser.parse_args()

    db = pdb.DB()
    api = papi.Api(db)

    if args.mode == 'init':
        init(api)
    elif args.mode == 'link':
        link(api)
    elif args.mode == 'findloc':
        findloc(api)
