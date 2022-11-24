from conexion import get_mysql_conection
try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (
                ('Persona1', 'apellido1', 'email1@gmail.com'),
                ('Persona2', 'apellido2', 'email2@yahoo.com'),
                ('Persona3', 'apellido3', 'email3@domain.com')
            )
            cursor.executemany(sentencia, valores)
            #conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')

            sentencia2 = 'SELECT nombre FROM personas'
            cursor.execute(sentencia2)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)

            sentencia3 = 'SELECT * FROM personas WHERE email LIKE "%gmail.com%"'
            cursor.execute(sentencia3)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)

            sentencia4 = "UPDATE `personas` SET `email` = " \
                         "CONCAT(left(`personas`.`email`, locate('@', `personas`.`email`) - 1), %s) " \
                         "WHERE `personas`.`email` NOT LIKE %s"
            cursor.execute(sentencia4, ('@gmail.com', 'gmail.com'))
            conexion.commit()
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')