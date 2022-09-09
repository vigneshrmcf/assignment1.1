show databases;
create database assignment ;
use assignment;
create table salespeople(
snum int,
sname varchar(100) unique,
city varchar(100),
comm varchar(100),
primary key (snum)
);
insert into salespeople (snum,sname ,city,comm) values (1011,'peel','london',.12);
select * from salespeople;
update salespeople set snum=1001 where sname ='peel';
select * from salespeople;
insert into salespeople (snum,sname ,city,comm) values (1003,'axelrod','newyork',.10);
select * from salespeople;

create table customers(
cnum int ,
city varchar(100),
cname varchar(100),
snum int,
primary key(cnum),
foreign key (snum) references salespeople(snum)
);

select * from customers;
insert into customers (cnum,city,cname,snum) values (2007,'pereira','rome',1004);
select * from customers;
create table orders(
onum int,
amt int ,
odate varchar(100),
cnum int,
snum int,
primary key(onum),
foreign key(cnum) references customers(cnum),
foreign key(snum) references salespeople (snum)
);

select * from orders;
insert into orders(onum,amt,odate,cnum,snum) values(3011,9891.88,6-10-1990,2006,1001);
select * from orders;

select * from salespeople where sname like 'a%';