import pymysql as MySQLdb


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self.__connection= None

    @property
    def connection(self):
        return self.__connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self.__connection:
            self.__connection = MySQLdb.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                db = self.db
            )

    def disconnect(self):
        if self.__connection:
            self.__connection.close()


class Category:
    def __init__(self, db_connection, name, description, id=None,):
        self.db_connection = db_connection.connection
        self.name = name
        self.description = description
        self.__id = id

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO category_test (name, description) values (%s, %s);", (self.name, self.description))
        self.__id = self.db_connection.insert_id()
        self.db_connection.commit()
        c.close()

    def select_all(self):
        c = self.db_connection.cursor()
        c.execute("SELECT * from category_test")
        items = c.fetchall()
        c.close()
        return items

    def truncate_table(self):
        c = self.db_connection.cursor()
        c.execute("TRUNCATE table category_test")
        self.db_connection.commit()
        c.close()


con = Connection('dbuser', '123', 'cook')

with con:
    category = Category(con, 'New recipies', 'Cook something new')
    category.save()
    category = Category(con, 'All recipies', 'Choose what you want to do')
    category.save()
    categories = list(category.select_all())
    print(categories)
    category.truncate_table()
    categories = list(category.select_all())
    print(categories)







