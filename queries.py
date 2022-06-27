from db_connection import DBConnector


def get_rooms():
    with DBConnector() as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM rooms"
        cursor.execute(query)
        return cursor.fetchall()


def get_unavailable():
    with DBConnector() as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM unavailable"
        cursor.execute(query)
        return cursor.fetchall()


def get_booking_time():
    with DBConnector() as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM booking_time"
        cursor.execute(query)
        return cursor.fetchall()


def get_booking():
    with DBConnector() as connection:
        cursor = connection.cursor()
        query = f"SELECT * FROM booking"
        cursor.execute(query)
        return cursor.fetchall()


def get_booking_by_room(id_room, day):
    with DBConnector() as connection:
        cursor = connection.cursor()
        query = f"SELECT * FROM booking WHERE " \
                f"id_room = {id_room}, " \
                f"day = {day}"
        cursor.execute(query)
        return cursor.fetchall()


def get_booking_by_employee(id_emp, day):
    with DBConnector() as connection:
        cursor = connection.cursor()
        query = f"SELECT * FROM booking WHERE " \
                f"id_emp = {id_emp}, " \
                f"day = {day}"
        cursor.execute(query)
        return cursor.fetchall()



def add_booking(id_emp, id_room, day, id_start, id_end):
    with DBConnector() as connection:
        cursor = connection.cursor()
        query = "INSERT INTO booking (id_emp, id_room, day, id_start, id_end) VALUES (" \
                "{}, " \
                "{}, " \
                "{}, " \
                "{}, " \
                "{})".format(id_emp, id_room, day, id_start, id_end)
        cursor.execute(query)


def add_unavailable(id_room, day):
    with DBConnector() as connection:
        cursor = connection.cursor()
        query = "INSERT INTO booking (id_room, day) VALUES (" \
                "{}, " \
                "{})".format(id_room, day)
        cursor.execute(query)