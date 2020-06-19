#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 18:02:29 2020

@author: sanantha
"""

import json

with open('books.json', 'r') as f:
    catalog = json.load(f)

# Print all the book identifiers

print('Task 1:  Print all the book identifiers')
for book_id in sorted(catalog):
    print(book_id)


print('Task 2:  Show author and price of bk102')
book = catalog['bk102']
print(book['author'])
print(book['price'])

print('Task 3: Show the title of all the books')
for title in catalog.values():
    print(title['title'])

print('Task 4:  Show author and price of the computer books')
for book_comp in catalog.values():
    if book_comp['genre'] == 'Computer':
        print(book_comp['author'])
        print(book_comp['price'])

print('Task 5:  Show the decription of bk105')
print(catalog['bk105']['description'])

print('Task 6:  Show all metadata for bk104')
book = catalog['bk104']
for tag, value in book.items():
    print(tag.upper())
    print(value)
    print

print('Task 7: Print publishing date for bk106')
print(catalog['bk106']['publish_date'])

print('Task 8: Print the complete catalog')
print(catalog.items())
    