import pandas as pd
import pyodbc

# from airflow.operators.python import PythonOperator
# from airflow.operators.python import BranchPythonOperator
# from airflow import DAG

# import os

from datetime import datetime
#Create the operation

def insert_hotel():
    df = pd.read_excel(io= r'C:\Users\MTC\Desktop\Data Dalat.xlsx',sheet_name='hotel', converters={'ID': str})
    print(df)
    server = 'QUANGHUY\SQLEXPRESS' 
    database = 'Dalat' 
    username = 'sa' 
    password = 'hoanghuy123' 
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)
    cursor = cnxn.cursor()
    # Insert Dataframe into SQL Server:
    for index, row in df.iterrows():
        print(type(row.ID))
        #ID = row.ID.replace("s", "")
        cursor.execute("INSERT INTO Hotel (ID,name,address) values(?,?,?)", row.ID, row.namee, row.address)
        print(row.namee)
        with open("insert_data.txt","w",encoding= "utf8") as file:
            file.write("INSERT INTO Hotel (ID,name,address) values("+row.ID +"," + "N'"+row.namee+"'" + "," + "N'" +row.address+ "'" + ")\n")    
    cnxn.commit()
    cursor.close()

def insert_staff():
    df = pd.read_excel(r'C:\Users\MTC\Desktop\Data Dalat.xlsx',sheet_name='staff', converters={'ID': str, 'hotel_id': str, 'manager_id': str, 'birthday': str, 'level': str})
    print(df)
    server = 'QUANGHUY\SQLEXPRESS' 
    database = 'Dalat' 
    username = 'sa' 
    password = 'hoanghuy123' 
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)
    cursor = cnxn.cursor()
    # Insert Dataframe into SQL Server:
    for index, row in df.iterrows():
        print(type(row.level))
        cursor.execute("set dateformat DMY;")
        cursor.execute("INSERT INTO staff (ID,hotel_id, [level], first_name, last_name, birthday, manager_id) values(?,?,?,?,?,?,?)", row.ID, row.hotel_id, row.level, row.first_name, row.last_name, row.birthday, row.manager_id)
        print(row.birthday)
        with open("insert_data.txt","a",encoding= "utf8") as file:
            file.write(" INSERT INTO staff (ID,hotel_id, [level], first_name, last_name, birthday, manager_id) values("+str(row.ID) +"," +str(row.hotel_id)+ "," + str(row.level)+ "," +"N'"+ row.first_name +"'" + "," + "N'" +row.last_name + "','"+ str(row.birthday)+ "',"+ row.manager_id + ")\n") 
    cnxn.commit()
    cursor.close()

def insert_room_type():
    df = pd.read_excel(r'C:\Users\MTC\Desktop\Data Dalat.xlsx',sheet_name='room_type', converters={'ID': str, "max_capacity": str })
    print(df)
    server = 'QUANGHUY\SQLEXPRESS' 
    database = 'Dalat' 
    username = 'sa' 
    password = 'hoanghuy123' 
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)
    cursor = cnxn.cursor()
    # Insert Dataframe into SQL Server:
    for index, row in df.iterrows():
        cursor.execute("set dateformat DMY;")
        cursor.execute("INSERT INTO room_type (ID, description, max_capacity) values(?,?,?)", row.ID, row.description, row.max_capacity)
        with open("insert_data.txt","a",encoding= "utf8") as file:
            file.write("INSERT INTO room_type (ID, description, max_capacity) values(" + row.ID +",'" + row.description + "','" + row.max_capacity + "')\n")   
    cnxn.commit()
    cursor.close()
    #ID	description	max_capacity

def insert_room():
    df = pd.read_excel(r'C:\Users\MTC\Desktop\Data Dalat.xlsx',sheet_name='room', converters={'ID': str, 'hotel_id': str, 'room_type_id': str})
    print(df)
    server = 'QUANGHUY\SQLEXPRESS' 
    database = 'Dalat' 
    username = 'sa' 
    password = 'hoanghuy123' 
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)
    cursor = cnxn.cursor()
    # Insert Dataframe into SQL Server:
    for index, row in df.iterrows():
        cursor.execute("set dateformat DMY;")
        cursor.execute("INSERT INTO room (ID,hotel_id, smoke, status, room_type_id) values(?,?,?,?,?)", row.ID, row.hotel_id, row.smoke, row.status, row.room_type_id)
        with open("insert_data.txt","a",encoding= "utf8") as file:
            file.write("INSERT INTO room (ID,hotel_id, smoke, status, room_type_id) values(" +row.ID + "," + row.hotel_id +",'" + row.smoke + "','" + row.status + "'," + row.room_type_id +")\n")   
    cnxn.commit()
    cursor.close()

def insert_guest():
    df = pd.read_excel(r'C:\Users\MTC\Desktop\Data Dalat.xlsx',sheet_name='guest', converters={'ID': str, 'phone_number': str})
    print(df)
    server = 'QUANGHUY\SQLEXPRESS' 
    database = 'Dalat' 
    username = 'sa' 
    password = 'hoanghuy123' 
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)
    cursor = cnxn.cursor()
    # Insert Dataframe into SQL Server:
    for index, row in df.iterrows():
        cursor.execute("set dateformat DMY;")
        cursor.execute("INSERT INTO guest (ID, first_name, last_name, phone_number) values(?,?,?,?)", row.ID, row.first_name, row.last_name, row.phone_number)
        with open("insert_data.txt","a",encoding= "utf8") as file:
            file.write("INSERT INTO guest (ID, first_name, last_name, phone_number) values(" +row.ID+ ",N'" +row.first_name+ "',N'" +row.last_name+ "','" +row.phone_number+ "')\n")
    cnxn.commit()
    cursor.close()
    # ID	first_name	last_name	phone_number

def insert_reservation():
    df = pd.read_excel(r'C:\Users\MTC\Desktop\Data Dalat.xlsx',sheet_name='reservation', converters={'ID': str, 'date_in': str, 'date_out': str, 'guest_id': str, "deposit": str})
    print(df)
    server = 'QUANGHUY\SQLEXPRESS' 
    database = 'Dalat' 
    username = 'sa' 
    password = 'hoanghuy123' 
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)
    cursor = cnxn.cursor()
    # Insert Dataframe into SQL Server:
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO reservation (ID, date_in, date_out, guest_id, deposit) values(?,?,?,?,?)", row.ID, row.date_in, row.date_out, row.guest_id, row.deposit)
        with open("insert_data.txt","a",encoding= "utf8") as file:
            file.write(" INSERT INTO reservation (ID, date_in, date_out, guest_id, deposit) values(" +row.ID+ ",'" +row.date_in+ "','" +row.date_out+ "'," +row.guest_id+ ",'" +row.deposit+"')\n")   
    cnxn.commit()
    cursor.close()
    #ID	date_in	date_out	guest_id	deposit


def insert_reserved_room():
    df = pd.read_excel(r'C:\Users\MTC\Desktop\Data Dalat.xlsx',sheet_name='reserved_room', converters={'ID': str, 'room_type_id': str, 'reservation_id': str, "number_of_room": str})
    print(df)
    server = 'QUANGHUY\SQLEXPRESS' 
    database = 'Dalat' 
    username = 'sa' 
    password = 'hoanghuy123' 
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)
    cursor = cnxn.cursor()
    # Insert Dataframe into SQL Server:
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO reserved_room (ID, number_of_rooms, room_type_id, reservation_id) values(?,?,?,?)", row.ID, row.number_of_room, row.room_type_id, row.reservation_id)
        with open("insert_data.txt","a",encoding= "utf8") as file:
            file.write("INSERT INTO reserved_room (ID, number_of_rooms, room_type_id, reservation_id) values(" +row.ID+ "," +row.number_of_room+ "," +row.room_type_id+ "," +row.reservation_id+ ")\n")
    cnxn.commit()
    cursor.close()
    #ID	number_of_room	room_type_id	reservation_id	status

def insert_occupied_room():
    df = pd.read_excel(r'C:\Users\MTC\Desktop\Data Dalat.xlsx',sheet_name='occupied_room', converters={'ID': str, 'reservation_id': str, 'room_id': str})
    print(df)
    server = 'QUANGHUY\SQLEXPRESS' 
    database = 'Dalat' 
    username = 'sa' 
    password = 'hoanghuy123' 
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)
    cursor = cnxn.cursor()
    # Insert Dataframe into SQL Server:
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO occupied_room (ID, check_in, check_out, room_id, reservation_id) values(?,?,?,?,?)", row.ID, row.check_in, row.check_out, row.room_id, row.reservation_id)
    cnxn.commit()
    cursor.close()
    #ID	check_in	check_out	room_id	reservation_id

def insert_occupied_room2():
    df = pd.read_excel(r'C:\Users\MTC\Desktop\Data Dalat.xlsx',sheet_name='occupied_room', converters={'ID': str, 'reservation_id': str, 'room_id': str, 'check_in': str, 'check_out': str})
    for index, row in df.iterrows():
        with open("insert_data.txt","a",encoding= "utf8") as file:
           file.write("INSERT INTO occupied_room (ID, check_in, check_out, room_id, reservation_id) values(" +row.ID+ ",'" +row.check_in+ "','" +row.check_out+ "'," +row.room_id+ "," +row.reservation_id+")\n")

def insert_hosted_at():
    df = pd.read_excel(r'C:\Users\MTC\Desktop\Data Dalat.xlsx',sheet_name='hosted_at', converters={'ID': str, 'guest_id': str, 'occupied_room_id': str})
    print(df)
    server = 'QUANGHUY\SQLEXPRESS' 
    database = 'Dalat' 
    username = 'sa' 
    password = 'hoanghuy123' 
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)
    cursor = cnxn.cursor()
    # Insert Dataframe into SQL Server:
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO hosted_at (ID, guest_id, occupied_room_id) values(?,?,?)", row.ID, row.guest_id, row.occupied_room_id)
        with open("insert_data.txt","a",encoding= "utf8") as file:
            file.write("INSERT INTO hosted_at (ID, guest_id, occupied_room_id) values(" +row.ID+ "," +row.guest_id+ "," +row.occupied_room_id+ ")\n")   
    cnxn.commit()
    cursor.close()
    #ID	guest_id	occupied_room_id

def main():
    insert_hotel()
    with open("insert_data.txt","a",encoding= "utf8") as file:
            file.write("set dateformat DMY;\n")
    insert_staff()
    insert_room_type()
    insert_room()
    with open("insert_data.txt","a",encoding= "utf8") as file:
            file.write("set dateformat YMD;\n")
    insert_guest()
    insert_reservation()
    insert_reserved_room()
    insert_occupied_room()
    insert_occupied_room2()
    insert_hosted_at()
if __name__ == '__main__':
    main()

# with DAG("load_to_dalat_database2", start_date = datetime(2021,10,24),
#     schedule_interval = None, catchup=False) as dag:

#         _insert_hotel = PythonOperator(
#             task_id="insert_hotel",
#             python_callable=insert_hotel
#         )

#         _insert_staff = PythonOperator(
#             task_id="insert_staff",
#             python_callable=insert_staff
#         )

#         _insert_room_type = PythonOperator(
#             task_id="insert_room_type",
#             python_callable=insert_room_type
#         )

#         _insert_room = PythonOperator(
#             task_id="insert_room",
#             python_callable=insert_room
#         )

#         _insert_guest = PythonOperator(
#             task_id="insert_guest",
#             python_callable=insert_guest
#         )

#         _insert_reservation = PythonOperator(
#             task_id="insert_reservation",
#             python_callable=insert_reservation
#         )

#         _insert_reserved_room = PythonOperator(
#             task_id="insert_reserved_room",
#             python_callable=insert_reserved_room
#         )

#         _insert_occupied_room = PythonOperator(
#             task_id="insert_occupied_room",
#             python_callable=insert_occupied_room
#         )

#         _insert_hosted_at = PythonOperator(
#             task_id="insert_hosted_at",
#             python_callable=insert_hosted_at
#         )

#         _insert_hotel >> _insert_staff >> _insert_room_type >> _insert_room >> _insert_guest >> _insert_reservation >> _insert_reserved_room >> _insert_occupied_room >> _insert_hosted_at 

