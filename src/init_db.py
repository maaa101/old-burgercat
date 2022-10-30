# creates a burger database

# IF THERE IS ALREADY A DATABASE.DB FILE, THE DATABASE WILL BE CLEARED AND ALL BURGERS WILL BE REMOVED

import sqlite3

connection = sqlite3.connect("database.db")

with open("schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

# add posts

#cur.execute("INSERT INTO posts (title, imgurl) VALUES (?, ?)",
#            ('the burger the burger is ready', 'https://tenor.com/view/yummy-burger-monch-cat-eat-gif-22806539')
#            )

#cur.execute("INSERT INTO posts (title, imgurl) VALUES (?, ?)",
#            ('the burger revolution is here', 'https://media.discordapp.net/attachments/563966858462625822/1035545221536170096/ABA24D6F-E6E7-4718-B7CE-8B5A208AB1FE.gif')
#            )

connection.commit()
connection.close()