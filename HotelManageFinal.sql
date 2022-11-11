--create database Dalat
-- drop database Dalat
-- use master
use Dalat
-- Create table
create table Hotel 
(
ID nvarchar(11),
name nvarchar(40),
address nvarchar(100),
primary key (ID)
)

create table room_type
(
ID nvarchar(10),
description nvarchar(80),
max_capacity int,
primary key(ID)
)

create table room
(
ID nvarchar(10),
hotel_id nvarchar(11),
status nvarchar(40),
smoke nvarchar(5),
room_type_id nvarchar(10),
primary key (ID)
)

create table occupied_room
(
ID nvarchar(10), 
check_in datetime,
check_out datetime,
room_id nvarchar(10) not null, 
reservation_id nvarchar(10) not null,
primary key (ID)
)

create table hosted_at
(
ID nvarchar(10), 
guest_id nvarchar(10),
occupied_room_id nvarchar(10),
primary key (ID)
)

create table guest
(
ID nvarchar(10),
first_name nvarchar(80),
last_name nvarchar(80),
phone_number nvarchar(10),
primary key (ID)
)

create table reservation
(
ID nvarchar(10),
date_in datetime,
date_out datetime,
guest_id nvarchar(10),
deposit int,
primary key (ID)
)

create table staff
(
ID nvarchar(10),
hotel_id nvarchar(11),
level int,
first_name nvarchar(10),
last_name nvarchar(20),
birthday datetime,
manager_id nvarchar(10),
primary key (ID, hotel_id)
)


create table reserved_room
(
ID nvarchar(10), 
number_of_rooms int,
room_type_id nvarchar(10), 
reservation_id nvarchar(10) not null,
primary key (ID)
)

-- Add constraint
ALTER TABLE reserved_room
add  constraint fk_1 foreign key(reservation_id)
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

ALTER TABLE staff
add constraint fk_11 foreign key(manager_id, hotel_id)
references staff(ID,hotel_id);

set dateformat DMY;
select * from Hotel
-- Create trigger

-- Insert data

-- User permision (Phân quyền)

-- Backup Database 
