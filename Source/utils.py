import mysql.connector as m
import hashlib
from cryptography.fernet import Fernet

KEY = b'7KMQYjugbgHfata2Guwztm7mpPeBbdlAaBv460iStn0='

class Crypto():
    def __init__(self, KEY):
        self.KEY = KEY
        self.fernet = Fernet(self.KEY)
    def encrypt(self, data):
        return self.fernet.encrypt(data)
    def decrypt(self, data):
        return self.fernet.decrypt(data)

class DB():
    def __init__(self):
        self.HOST = "localhost"
        self.PORT = 3306
        self.USER = "root"
        self.PASSWORD = "root"
        self.DATABASE = "srmtrichy"
        self.conn = None
        self.cur = None
    def makeConnection(self):
        self.conn = m.connect(host = self.HOST, port = self.PORT, user = self.USER, passwd = self.PASSWORD, database = self.DATABASE)
        self.cur = self.conn.cursor()
    def setupDatabase(self):
        self.makeConnection()
        self.cur.execute("CREATE TABLE IF NOT EXISTS students (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL, number VARCHAR(10) NOT NULL, password VARCHAR(256) NOT NULL, address VARCHAR(1000) NOT NULL)")
        self.conn.commit()
    def loginWithCred(self, email, password) -> bool:
        password = hashlib.sha256(password.encode()).hexdigest()
        self.cur.execute("select  * from students where email = %s && password = %s", (email, password))
        data = self.cur.fetchall()
        if data == []: return False
        return data[0][2] == email
    def generateEncodedString(self, email, password):
        crypt = Crypto(KEY)
        res = email + "\n\t" + password
        return crypt.encrypt(res.encode()).decode()
    def loginWithEncodedString(self, encodedString):
        crypt = Crypto(KEY)
        try:
            decoded = crypt.decrypt(encodedString.encode()).decode().split('\n\t')
            email = decoded[0]
            password = decoded[1]
            return (True, self.loginWithCred(email, password), email)
        except:
            return (False,)
    def getStudentDetails(self, email):
        try:
            self.cur.execute("select * from students where email = %s", (email,))
            data = self.cur.fetchall()
            return data
        except:
            return [["Not found", "Not found", "Not found", "Not found", "Not found", "Not found"]]
    def registerNewStudent(self, name, email, number, addr, password) -> bool:
        self.cur.execute("select * from students where email = %s", (email,))
        data = self.cur.fetchall()
        if data == []:
            try:
                password = hashlib.sha256(password.encode()).hexdigest()
                self.cur.execute("insert into students(name, email, number, password, address) values (%s, %s, %s, %s, %s)", (name, email, str(number), password, addr))
                self.conn.commit()
                return True
            except:
                return False
        else:
            return False

