import pymysql

class DAOObservaciones:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="db_poo" )

    def read(self,id):
        con =DAOObservaciones.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM observaciones order by id asc")
            else:
                cursor.execute("SELECT * FROM observaciones where id = %s order by id asc", (id,))
            return cursor.fetchall()
        
        except:
            return ()
        finally:
            con.close()



