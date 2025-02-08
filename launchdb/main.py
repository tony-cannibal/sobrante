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
    cur.execute(
        """
		CREATE TABLE IF NOT EXISTS sobrante_m2 (
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
        cantidad INT NOT NULL,
        fecha DEFAULT CURRENT_TIMESTAMP,
        restante INT,
        actualizado ON UPDATE CURRENT_TIMESTAMP
		);"""
    )
    cur.execute(
        """
        CREATE TABLE movimientos_m1 (
            id INT AUTO_INCREMENT PRIMARY KEY,
            sobrante_m1_id INT NOT NULL,
            num_parte VARCHAR(),
            circuito VARCHAR(6),
            fecha DEFAULT CURRENT_TIMESTAMP,  
            accion VARCHAR(20)
            );
    """
    )
    cur.execute(
        """
        CREATE TABLE movimientos_m1 (
            id INT AUTO_INCREMENT PRIMARY KEY,
            sobrante_m1_id INT NOT NULL,
            num_parte VARCHAR(),
            circuito VARCHAR(6),
            fecha DEFAULT CURRENT_TIMESTAMP,  
            accion VARCHAR(20)
            );
    """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS num_parte (
            id VARCHAR(20) NOT NULL PRYMARY KEY,
            circuito VARCHAR(10),
            terminal_l VARCHAR(12),
            terminal_r VARCHAR(12),
            sello_l VARCHAR(12),
            sello_r VARCHAR(12),
            cable VARCHAR(12),
            longitud INT
            );
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS carga_m1 (
            id VARCHAR(20) NOT NULL PRYMARY KEY,
            circuito VARCHAR(6),
            maquina VARCHAR(6),
            terminal_l VARCHAR(12),
            terminal_r VARCHAR(12),
            sello_l VARCHAR(12),
            sello_r VARCHAR(12),
            cable VARCHAR(12),
            longitud INT
            );
                """
    )


if __name__ == "__main__":
    createTables(**database)
