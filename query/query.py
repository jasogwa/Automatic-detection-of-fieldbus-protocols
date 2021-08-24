import mysql.connector

class QUERY:

    def __init__(self):
        self.__localhost     = "localhost"
        self.__username      = "root"
        self.__password      = ""
        self.__database_name = "reverse_protocols" 
        self.__table_name 	 = "sequences" 
        self.createConnection()

    def create(self,name,seqA,seqB,score):
        self.createConnection()
        cursor = self.__db.cursor()
        cursor.execute("INSERT INTO sequences (name, seqA, seqB,score) VALUES (%s, %s, %s, %s)", (name,seqA,seqB,score))
        self.__db.commit()

    def createMsa(self,name,consensus_seq):
        self.createConnection()
        cursor = self.__db.cursor()
        cursor.execute("INSERT INTO msa (name, consensus_seq) VALUES (%s, %s)", (name,consensus_seq))
        self.__db.commit()

    def select(self):
        self.createConnection()
        cursor = self.__db.cursor()
        cursor.execute("SELECT * FROM sequences")
        rows = cursor.fetchall()
        return rows

    def selectMsa(self):
        self.createConnection()
        cursor = self.__db.cursor()
        cursor.execute("SELECT * FROM msa")
        rows = cursor.fetchall()
        return rows

    def createConnection(self):
        db = mysql.connector.connect(
            host     = self.__localhost,
            user     = self.__username,
            passwd   = self.__password,
            database = self.__database_name
        )

        self.__db = db