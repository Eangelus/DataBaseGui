import re

import mysql.connector


class MyDataBaseBot:

    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = int(port)
        self.username = username
        self.nameDataBase = database
        self.password = password
        self.base = mysql.connector.connect(host=self.host, port=self.port, user=self.username, password=self.password, database=self.nameDataBase)
        print('connect done')
        self.bot_cursor = self.base.cursor()
        self.tablename = ""
        self.spaltenname = ""
        self.vari = ""

        self.id = ""
        self.auswahl = ""

    def use(self, dataBaseName):
        self.bot_cursor.execute("USE " + dataBaseName)

    def create_bases(self, nameDataBase):
        self.bot_cursor.execute("CREATE DATABASES " + nameDataBase)

    def einf(self, tablename, spaltenname, vari):
        self.bot_cursor.execute("INSERT INTO " + tablename + " SET " + spaltenname + " = " + vari)

    def update(self, tablename, spaltenname, vari, id, auswahl):
        self.bot_cursor.execute("UPDATE "+tablename+" SET "+spaltenname+" = "+vari+" WHERE "+id+" = "+auswahl)

    def zeige(self, tablename):
        self.bot_cursor.execute("SELECT * FROM " + tablename)
        r = self.bot_cursor.fetchall()
        return r

    def zeige_base(self):
        self.bot_cursor.execute("SHOW DATABASES")
        resulte = self.bot_cursor.fetchall()
        return resulte

    def zeige_tables(self):
        self.bot_cursor.execute("SHOW TABLES")
        r = self.bot_cursor.fetchall()
        return r

    def zeige_struk(self, tablename):
        self.bot_cursor.execute("Desc " + tablename)
        result = self.bot_cursor.fetchall()
        return result

    def delete_table(self):
        self.bot_cursor.execute()

    def join_left(self):
        self.bot_cursor.execute()

    def con_close(self):
        self.bot_cursor.close()
        self.base.close()

    def enf(self, tablename, auswahl):
        print(tablename, auswahl)
        a = self.zeige(tablename)
        print(a)

        self.bot_cursor.execute("DELETE FROM "+tablename+" WHERE id_eintrag="+auswahl)
        print("löschen erfolgreich")

    #---------------------------------------- geter / setter -------------------------------
    def get_tablename(self):
        return self.tablename

    def set_tablename(self, tablename):
        self.tablename = tablename


    def set_spaltenname(self,spaltenname):
        self.spaltenname = spaltenname
    def get_spaltenname(self, spaltenname):
        return self.spaltenname

