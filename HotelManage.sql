create database Dalat
use Dalat

-- Create table
create table Hotel 
(
ID int,
name nvarchar(40),
address nvarchar(100),
manager_id int not null,
primary key (ID)
)

create table room_type
(
ID int,
description nvarchar(80),
max_capacity int,
primary key(ID)
)

create table room
(
ID int,
hotel_id int,
number varchar(10),
name nvarchar(40),
status nvarchar(40),
smoke nvarchar(5),
room_type_id int,
primary key (ID)
)

create table occupied_room
(
ID int, 
check_in datetime,
check_out datetime,
room_id int not null, 
reservation_id int not null,
primary key (ID)
)

create table hosted_at
(
ID int, 
guest_id int,
occupied_room_id int,
primary key (ID)
)

create table guest
(
ID int,
first_name nvarchar(80),
last_name nvarchar(80),
phone_number int,
primary key (ID)
)

create table reservation
(
ID int,
date_in datetime,
date_out datetime,
guest_id int,
deposit int,
primary key (ID)
)

create table staff
(
ID int,
hotel_id int,
level int,
first_name nvarchar(10),
last_name nvarchar(20),
birthday date,
manager_id int,
salary int,
primary key (ID, hotel_id)
)

create table reserved_room
(
ID int, 
number_of_rooms int,
room_type_id int, 
reservation_id int not null,
status nvarchar(20),
primary key (ID)
)
-- Add constraint
ALTER TABLE reserved_room
add  constraint fk_rs_rsr foreign key(reservation_id)
references reservation(ID);

ALTER TABLE reserved_room
add  constraint fk_2 foreign key(room_type_id)
references room_type(ID);

ALTER TABLE room
add  constraint fk_3 foreign key(room_type_id)
references room_type(ID);

ALTER TABLE occupied_room
add  constraint fk_4 foreign key(room_id)
references room(ID);

ALTER TABLE hosted_at
add constraint fk_5 foreign key(occupied_room_id)
references occupied_room(id);

ALTER TABLE hosted_at
add constraint fk_6 foreign key(guest_id)
references guest(id);

ALTER TABLE reservation
add constraint fk_7 foreign key(guest_id)
references guest(ID);

ALTER TABLE occupied_room
add constraint fk_8 foreign key(reservation_id)
references reservation(ID);

ALTER TABLE room
add constraint fk_9 foreign key(hotel_id)
references hotel(ID);

ALTER TABLE staff
add constraint fk_10 foreign key(hotel_id)
references hotel(ID);

ALTER TABLE hotel
add constraint fk_11 foreign key(manager_id,ID)
references staff(ID,hotel_id);

ALTER TABLE staff
add constraint fk_12 foreign key(manager_id, hotel_id)
references staff(ID,hotel_id);

