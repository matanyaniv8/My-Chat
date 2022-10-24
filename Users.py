import sqlite3


class UsersDatabase:
    def __init__(self):
        self.con = sqlite3.connect("databases/Users.db")
        self.cur = self.con.cursor()
        self.validate_all()

    def validate_all(self):
        """
        The function checks all the SQl parameters are correct built.
        :return:
        None
        """
        self.cur.execute("CREATE TABLE IF NOT EXISTS Users(id number (10) primary key, password, chat_list [])")
        self.cur.execute("CREATE TABLE IF NOT EXISTS ContactCard(name, age integer, phone number (10) primary key)")
        self.con.commit()

    def new_user(self, phone, password):
        self.cur.execute("INSERT INTO Users values(?, ?)", (phone, password))
        self.con.commit()

    def new_contact(self, name, age, phone):
        self.cur.execute("INSERT INTO ContactCard values(?, ?, ?)", (name, age, phone))
        self.con.commit()

    def check_phone(self, phone):
        result = self.cur.execute("SELECT * FROM ContactCard WHERE phone = %s" % phone)
        return result.fetchone() is None

    def finish(self):
        self.cur.close()
        self.con.close()


if __name__ == "__main__":
    userDatabase = UsersDatabase()

    print(userDatabase.check_phone("1234567890"))

    userDatabase.new_contact('roy', 22, '0544234555')

    userDatabase.new_user('0544234555', '052384')

    userDatabase.finish()


# TODO: encrypt password (hash, one way)
# TODO: new users register
# TODO: connect
# TODO: connect chats to the user 'chat_list'
