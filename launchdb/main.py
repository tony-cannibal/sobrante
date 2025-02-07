import mariadb


database = {
    "host": "172.18.4.58",
    "database": "sobrantes",
    "user": "yura_admin",
    "password": "Metallica24+",
    "port": 3306,
}


def createDatabase(db):
    con = mariadb.connect(**db)
    cur = con.cursor()
    cur.execute("CREATE DATABASE sobrante")


def createTable(db):
    con = mariadb.connect(**db)
    cur = con.cursor()
    cur.execute(
        """
            CREATE TABLE sobrante_m1 (
                id INT AUTO_INCREMENT PRIMARY KEY, 
                codigo VARCHAR,
                num_parte VARCHAR,
                circuito VARCHAR,
                cable VARCHAR,
                terminal_l VARCHAR,
                terminal_r VARCHAR,
                sello_l VARCHAR,
                sello_r VARCHAR,
                longitud VARCHAR,
                cantidad INT,
                fecha DEFAULT CURRENT_TIMESTAMP,
                restante INT,
                actualizado ON UPDATE CURRENT_TIMESTAMP
            )
        """
    )
    cur.execute(
        """
            CREATE TABLE sobrante_m2 (
                id INT AUTO_INCREMENT PRIMARY KEY, 
                codigo VARCHAR,
                num_parte VARCHAR,
                circuito VARCHAR,
                cable VARCHAR,
                terminal_l VARCHAR,
                terminal_r VARCHAR,
                sello_l VARCHAR,
                sello_r VARCHAR,
                longitud VARCHAR,
                cantidad INT,
                fecha DEFAULT CURRENT_TIMESTAMP,
                restante INT,
                actualizado ON UPDATE CURRENT_TIMESTAMP
            )
        """
    )
    cur.execute(
        """
            CREATE TABLE movimientos_m1 (
                id INT AUTO_INCREMENT PRIMARY KEY,

                np VARCHAR,
                circuito VARCHAR,
                fecha DEFAULT CURRENT_TIMESTAMP
                )
        """
    )
