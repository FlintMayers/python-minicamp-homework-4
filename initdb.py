import sqlite3

connection = sqlite3.connect('database.db')
print 'Connected'

connection.execute('CREATE TABLE movies (title TEXT, rating INTEGER, genre TEXT)')

print 'Table created'

connection.close()
