import mariadb


database = {
    "user": "yura_admin",
    "password": "Metallica24+",
    "host": "172.18.4.58",
    "port": 3306,
    "database": "sobrante",
}


def createDatabase(db):
    con = mariadb.connect(**db)
    cur = con.cursor()
    cur.execute("CREATE DATABASE sobrante")


def createTables(**db):
    con = mariadb.connect(**db)
    cur = con.cursor()
    cur.execute(
        """
		CREATE TABLE IF NOT EXISTS sobrante_m1 (
		id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        lote VARCHAR(12),
		num_parte VARCHAR(30),
		circuito VARCHAR(30) NOT NULL,
		cable VARCHAR(10),
		terminal_l VARCHAR(14),
		terminal_r VARCHAR(14),
        sello_l VARCHAR(14),
        sello_r VARCHAR(14),
        longitud INT,
        cantidad INT,
        fecha DEFAULT CURRENT_TIMESTAMP,
        restante INT,
        actualizado ON UPDATE CURRENT_TIMESTAMP
		);"""
    )
    # """
    #     CREATE TABLE sobrante_m1 (
    #         id INT AUTO_INCREMENT PRIMARY KEY,
    #         codigo VARCHAR,
    #         num_parte VARCHAR,
    #             circuito VARCHAR,
    #             cable VARCHAR,
    #             terminal_l VARCHAR,
    #             terminal_r VARCHAR,
    #             sello_l VARCHAR,
    #             sello_r VARCHAR,
    #             longitud VARCHAR,
    #             cantidad INT,
    #             fecha DEFAULT CURRENT_TIMESTAMP,
    #             restante INT,
    #             actualizado ON UPDATE CURRENT_TIMESTAMP
    #         );
    #     """
    # )
    # cur.execute(
    #     """
    #         CREATE TABLE sobrante_m2 (
    #             id INT AUTO_INCREMENT PRIMARY KEY,
    #             codigo VARCHAR,
    #             num_parte VARCHAR,
    #             circuito VARCHAR,
    #             cable VARCHAR,
    #             terminal_l VARCHAR,
    #             terminal_r VARCHAR,
    #             sello_l VARCHAR,
    #             sello_r VARCHAR,
    #             longitud VARCHAR,
    #             cantidad INT,
    #             fecha DEFAULT CURRENT_TIMESTAMP,
    #             restante INT,
    #             actualizado ON UPDATE CURRENT_TIMESTAMP
    #         );
    #     """
    # )
    # cur.execute(
    #     """
    #         CREATE TABLE movimientos_m1 (
    #             id INT AUTO_INCREMENT PRIMARY KEY,
    #             ref INT,
    #             np VARCHAR,
    #             circuito VARCHAR,
    #             fecha DEFAULT CURRENT_TIMESTAMP
    #             );
    #     """
    # )
    # cur.execute(
    #     """
    #         CREATE TABLE movimientos_m1 (
    #             id INT AUTO_INCREMENT PRIMARY KEY,
    #             ref INT,
    #             np VARCHAR,
    #             circuito VARCHAR,
    #             fecha DEFAULT CURRENT_TIMESTAMP
    #             );
    #     """
    # )


if __name__ == "__main__":
    createTables(**database)
