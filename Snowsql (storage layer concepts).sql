-- These cmds are run from snowsql (in cmd prompt)
--All commands and sample csv file in the video description--
create database SLEEKDATA;

create schema OMS;
create stage MY_STAGE;

create table MY_TABLE (
    ID int,
    Name varchar(100),
    Age int,
    Region varchar(10)
);

-- Run put command in SNOWSQL CLI
-- (transfers the file from local machine to a stage within snowflake)
-- compresses the raw file and uploads to snowflake
put file://D:/mydata.csv @MY_STAGE;

copy into MY_TABLE from @MY_STAGE/mydata.csv.gz;

select * from MY_TABLE;

-- THE DATA FILE
mydata.csv

1,Alice,25,US
2,Bob,30,EU
3,Charlie,28,AP
4,David,35,US
5,Emma,40,EU
6,Frank,32,AP
7,Grace,27,US
8,Henry,45,EU
9,Ivan,50,AP
10,Jasmine,23,US