# what is SQL  ?

1. SQL stands for structured query language 
2. SQL is a case insenstive language 
3. SQL is not conditional 
4. SQL create a structured of database and tables 
5. SQL is execute query or command 

# what is query or command in SQL ?

1. query is a single line 
2. query and command both are same 
3. via SQL query its create and database and tables structured 

# types of SQL query ?

- THere are 4 types of SQL query 

- **DDL** (data definition language)

- **DML** (data manipulation language)

- **DQL** (data query language)

- **TCL** (transactional control language)


- **DDL** (data definition language) : 

1. DDL create an structured 
2. DDL create an database and tables structured 
3. DDL used to change column name is table
4. DDL used to change table name is table
5. DDL used to drop database and table structured


**DDL query are ..**

1. create 
2. alter 
3. truncate 
4. drop 
5. rename 
6. change 


## how to create database ? 

**syntax**

``` 
create database databasename;
or 
create database data_analytics_4pm;

```

![alt text](MysqlWorkbench-2.png)

or 

![alt text](xampp.png)   

## how to create table in database  ? 

## chart of create table for its columnname or fieldname 

|   column name    |   data types     |    size           |
|------------------|------------------|-------------------|
|id                | int              | default size(11)  |
|name, email ,pass | char , varchar   | (0-255)           |
|mobile            | int, bigInt      | default size(20)  |
|decimal, salary   | decimal(10,2)    | (10,2)            |       
|address , message | text             | 65365 character   | 
|date , datetime   | date , datetime  |                   | 
|photo , image     | varchar , blob   |                   |
|salary            | float            |                   |
|multiple choice   | enum()           |                   |
|default timezone  | timestamp        |                   |
|true, false       | boolean          |                   |   


**syntax**

```
create table tablename
(
columnname datatype(size) primary key auto_increment,
.
.
.
.
.
column datatype(size)

)

or

create table customers(
id int AUTO_INCREMENT primary key,
name varchar(200),
password varchar(255),
firstname varchar(255),
lastname varchar(255),
gender varchar(255),
mobile bigint
)

```
