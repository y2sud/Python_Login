import mysql.connector as mysqlc
from .cryp import Cryp


host = 'url or ip for db instance'
db = 'database_name'
user = 'db_user'
pwd = 'encrypted_Db_password'

conn = mysqlc.connect(host = host,
               database=db,
               user = user,
               password = Cryp.decrypt(pwd.encode()) )

cursor = conn.cursor()

class Model:
    @staticmethod
    def get_row(user_n):
        query = "select * from user where username = '%s' "  % (user_n)
        cursor.execute(query)
        row = cursor.fetchone()
        return row

    @staticmethod
    def user_exists(user_n, pwd):
        row = Model.get_row(user_n)
        #print('row ', row, cursor.rowcount)
        #print(cursor.rowcount )
        if cursor.rowcount == 1:
            db_pwd = row[2]
            #print('db pwd ', db_pwd)
            if db_pwd == Cryp.f_hash(pwd):
                return 0
            else:
                return 1
        return 2

    @staticmethod
    def get_fullname(user_n):
        row = Model.get_row(user_n)
        # return fullname
        return row[3]

    #data = cursor.fetchall()
    @staticmethod
    def add_user(*args):
        email_id, user_n, password, fullname = args
        password = Cryp.f_hash(password)
        _ = Model.get_row(user_n)
        # user already exists
        if cursor.rowcount == 1:
            return 1
        # insert user into db
        try:
            query = ("insert into user values ('%s', '%s', '%s', '%s')") % (email_id, user_n, password, fullname)
            cursor.execute(query)
            conn.commit()    
            return 0
        except:
            print('error ')
            return 2

    @staticmethod
    def close_conn():
        conn.close()

    @staticmethod
    def delete_row(user_n):
        try:
            query = ("delete from user where username = '%s' ") % (user_n)
            cursor.execute(query)
            del_row = cursor._rowcount
            print('del count ', del_row)
            conn.commit()
            return True
        except:
            return False

    @staticmethod
    def get_all_rows():
        query = "select * from user"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print('Row: ', row)

if __name__ == "__main__":
    print('user exists ', Model.user_exists('Kane', 'Kane%'))
    #print('db ver ', data)
    print('Deleted? ', Model.delete_row('Kane'))
    Model.get_all_rows()
    Model.close_conn()
