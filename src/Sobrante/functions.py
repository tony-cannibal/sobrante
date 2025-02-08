import mariadb
import configparser
from datetime import date


database = {
    "host": "172.18.4.58",
    "database": "wip_inventory",
    "user": "yura_admin",
    "password": "Metallica24+",
    "port": 3306,
}


def getConfig(path):
    config = configparser.ConfigParser()
    config.read(path + "/conf.ini")
    area = config["config"]["area"]
    station = config["config"]["estacion"]
    return area, station


def getDatabase(path):
    config = configparser.ConfigParser()
    config.read(path + "/conf.ini")
    database = {
        "host": config["database"]["host"],
        "database": config["database"]["database"],
        "user": config["database"]["user"],
        "password": config["database"]["password"],
        "port": int(config["database"]["port"]),
    }
    return database
