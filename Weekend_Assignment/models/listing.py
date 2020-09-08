import sqlite3
import os

class SneakerListing:

    tablename = "listings"
    dbpath = ""

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.Name = kwargs.get('Name', '')
        self.Yr_release = kwargs.get('Yr_release', 0)
        self.Version_number = kwargs.get('Version_number', 0)
        self.Creator = kwargs.get('Creator', '')
        self.OP = kwargs.get('OP', 0.0)
        self.CP = kwargs.get('CP', 0.0)
        self.Company = kwargs.get('Company', '')
        self.Contact_number = kwargs.get('Contact_number', 0)
        self.Contact_email = kwargs.get('Contact_email', '')

    def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename} (Name, Yr_release, Version_number, Creator, OP, CP, Company, Contact_number, Contact_email) VALUES (?,?,?,?,?,?,?,?,?) """
            values = (self.Name, self.Yr_release, self.Version_number, self.Creator, self.OP, self.CP, self.Company, self.Contact_number, self.Contact_email)
            cursor.execute(sql, values)
            return True
        return False

    def update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""UPDATE {self.tablename} SET Name =?, Yr_release =?, Version_number =?, Creator =?, OP =?, CP =?, Company =?, Contact_number =?, Contact_email =? WHERE pk =?; """
            values = (self.Name, self.Yr_release, self.Version_number, self.Creator, self.OP, self.CP, self.Company, self.Contact_number, self.Contact_email, self.pk)
            cursor.execute(sql, values)
            return True
        return False

    @classmethod
    def delete(cls, pk):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""DELETE FROM sneakerlistings WHERE pk =?;"""
            values = (pk,)
            cursor.execute(sql, values)
            return True
        return False

    @classmethod
    def select_person(cls, Contact_number, Contact_email):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename} WHERE Contact_number =?, Contact_email =?;"""
            values = (Contact_number, Contact_email,)
            cursor.execute(sql, values)
            return cursor.fetchone()

    @classmethod    
    def select_price(cls, where_clause):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename} {where_clause};"""
            cursor.execute(sql)
            return cursor.fetchone()

    @classmethod   
    def select_company(cls, Company):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename} WHERE Company =?;"""
            values = (Company,)
            cursor.execute(sql, values)
            return cursor.fetchone()


    #bonus
    
    # @classmethod
    # def select_sneaker_sale(cls):

    @classmethod
    def select_all(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename};""" 
            cursor.execute(sql)
            return cursor.fetchall()
        return []