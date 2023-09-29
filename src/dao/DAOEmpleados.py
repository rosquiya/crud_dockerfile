import pymysql

class DAOEmpleados:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="db_poo" )

    def read(self,id):
        con =DAOEmpleados.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM empleados order by nombre asc")
            else:
                cursor.execute("SELECT * FROM empleados where id = %s order by nombre asc", (id,))
            return cursor.fetchall()
        
        except:
            return ()
        finally:
            con.close()

    def insert(self,data_empleados):
        con = DAOEmpleados.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO empleados(nombre,telefono,email,area,puesto,edad) VALUES(%s, %s, %s,%s,%s, %s)", (data_empleados['nombre'],data_empleados['telefono'],data_empleados['email'],data_empleados['area'],data_empleados['puesto'],data_empleados['edad'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data_empleados):
        con = DAOEmpleados.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE empleados set nombre = %s, telefono = %s, email = %s,area =  %s, puesto= %s,edad = %s where id = %s", (data_empleados['nombre'],data_empleados['telefono'],data_empleados['email'],data_empleados['area'],data_empleados['puesto'],data_empleados['edad'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def delete(self, id):
        con = DAOEmpleados.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM empleados where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
