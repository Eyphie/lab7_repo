import pymysql as MySQLdb


db = MySQLdb.connect(user='dbuser', password='123', host='127.0.0.1', database='cook')
c = db.cursor(MySQLdb.cursors.DictCursor)

c.execute("TRUNCATE TABLE category_test")
db.commit()

c.execute('INSERT INTO category_test (name, description) values (%s,%s), (%s,%s)',\
          ('New recipies', 'Cook something new', 'All recipies', "Choose what you want to do"))
db.commit()

c.execute("SELECT * FROM category_test")
categories=c.fetchall()
for category in categories:
   print("{}:{}".format(category['name'], category['description']))

c.execute("DELETE FROM category_test where id=1;")
db.commit()

c.execute ("SELECT * FROM category_test;")
print("After DELETE")
categories=c.fetchall()
for category in categories:
   print("{}:{}".format(category['name'], category['description']))

c.close()
db.close()