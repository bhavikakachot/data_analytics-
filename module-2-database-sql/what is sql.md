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

![alt text](image-5.png)

or 

![alt text](image-6.png)   

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


or

create table tbl_feedback(
id int AUTO_INCREMENT primary key,
name varchar(100),
email varchar(255),
phone bigint,
rating enum('*','**','***','****','*****'),
comment text    
);

```

# alter ....

1. alter is used to add | update | modify new column in tables 
2. alter is also  used to add unique key of any column name 

**query or commands are**

```
alter table tbl_feedback add added_date_time datetime;
or
alter table customers add address text;
or
alter table customers add photo varchar(255) after name;
or
alter table tbl_feedback change added_date_time adddatetime datetime;

```

# add unique key via alter 

1. unique key is provides in table stored unique values 
2. unique is never stored dublicate values 


**add unique key via SQL**


```
alter table tbl_feedback add UNIQUE(`email`)

```

# change 

- change is used with alter 
- change is used to update any column name used with alter 

```
alter table tbl_feedback change adddatetime added_date datetime;
```


# rename :

- rename any table name 
- rename is use to update or rename to created tables 

```
rename table customers to tbl_customers;
```

# drop : 

**drop a database**

1. drop will used to delete database and its structured 
2. after drop we will never rollback any structured and data 

**syntax**

```
drop database databasename;
or
drop database data_analytics_4pm;

```

**drop a table**

1. drop will used to delete table and its data also 
2. after drop we will never rollback any structured or  data of tables

**syntax**

```
drop table tablename;
or
drop table tbl_customers;
or
drop table tbl_feedback;

```


# truncate : 

1. truncate is used to empty tables data 
2. truncate removed all data from tables 
3. truncate never rollback data 
4. truncate only delete data not delete structures 


**difference b/ primary key and unique key**

**primary key**
1. A pk is provides one times in table 
2. A pk key should always auto_increment
3. A pk never return a null values
4. A pk stored a unique values 

|   id(pk)     |  name     |  age  |   address |
|--------------|-------------------|-----------|
|   1          | brijesh   | 36    | rjt       |

**unique key**
1. A uk is provides more than one times in table 
3. A uk return one times a null values
4. A uk never return dublicate data 


|   id(pk)     |  name     |  age  |   address |  mobile   |    email   |
|--------------|-------------------|-----------|-----------|------------|
|   1          | brijesh   | 36    | rjt       |9121212    | a@gmail.com|


```
truncate table tablename
or
truncate table tbl_feedback 

``` 

# difference b/w truncate | drop | delete 

**truncate**

1. truncate is empty all data from tables 
2. after truncate we never rollback any data data from tables 
3. truncate deleted  only rows or data 


**drop**
1. drop is used to drop database or table with structured and data 
2. drop never rollback any data 

**drop database**

````
drop database data_analytics_430;
````

**drop  table**

````
drop table tbl_feedback;
````

**delete**

1. delete is used to delete all data from table
2. delete is used to delete particular data from tables 
3. delete is used to a range of data from tables 
4. delete is used to delete alternate   data from table

**delete data**

1. delete from tbl_country;
2. delete from tbl_country where cid=2;
3. delete from tbl_country where name='pakistan';
4. delete from tbl_country where cid between 6 and 50;
5. delete from tbl_country where cid in (2,5,7);

**note: after delete we rollback data using transanctional query**


# DML (data manipulation language)

1. DML is used to insert | delete | update data 

```
examples : insert | delete | update 

```

2. How to **insert data** ...

**syntax**

```
insert into tbl_customers(name,photo,password,firstname,lastname,gender,mobile,address) values('brijesh','brijesh.jpg','brij123','brij','pandey','male',912236151546,'rajkot')

or

insert into tbl_customers(name,photo,password,firstname,lastname,gender,mobile,address) values('dhruv','dhruv.jpg','d123','shruv','patel','male',912236151546,'rajkot'),('bhavika','bhavika.jpg','bh123','bhavika','sharma','female',9122361,'rajkot'),('kalpit','kalpit.jpg','kalpit','kalpit','patel','male',912236,'rajkot')

or

insert into tbl_customers values(null,'om','om.jpg','d123','shruv','patel','male',912236151546,'rajkot'),(null,'jainish','jainish.jpg','bh123','bhavika','sharma','female',9122361,'rajkot'),(null,'kumar','kumar.jpg','kalpit','kalpit','patel','male',912236,'rajkot')

```

3. How to **update data or rows**... 

**syntax**
```
update tablename set columnname='values' where id=1;
or 
update  tbl_customers set name='naimish',photo='naimish.png',password='naimish123',firstname='naimish',lastname='vaja',mobile=6356421656,address='150 feet ring road ahemdabad' where id=7; 
```


4. how to **delete data or **rows**..

- delete from tbl_country;
- delete from tbl_country where cid=2;
- delete from tbl_country where name='pakistan';
- delete from tbl_country where cid between 6 and 50;
- delete from tbl_country where cid in (2,5,7);

**note**
- after delete we can rollback data via rollback transactional query 


## DQL  : stands for data query language

**query in DQL**

```
select 

1. select all data from tables

select * from tbl_customers

2. select particular one data from tables 

select * from tbl_customers where id=3;

3. select particular one data from tables 

select * from tbl_customers where name='kalpit';


4. select particular columns of data

select name,photo,mobile,address from tbl_customers;


5. select and create alias(change nick name of column) of any column name

select cid,cname as countryname from tbl_country

6. select alternative of data from tables 

select * from tbl_customers where id in(4,6,7);

7. select range of data from tables 

select * from tbl_customers where id between 1 and 6;

8. select data using limit 

select * from tbl_customers where id limit 0,1;
or
select * from tbl_customers where id limit 3,2;
or
select * from tbl_customers where id limit 5,3;

9. select is used in searching data using like operator and its wildcard

a) select customers name who's name start with 'a' character

select * from tbl_customers where name like  'a%';
or
select * from tbl_customers where name like  'b%';



b) select customers name who's name end with 'h' character

select * from tbl_customers where name like  '%h';
or
select * from tbl_customers where name like  '%t';


c) select customers name who's name found a anywhere  'a' character

select * from tbl_customers where name like  '%a%';
or
select * from tbl_customers where name like  '%sh%';

```
# difference b/w order by and group by 

## order by : 

- order by is used to filter data from tables in ASC or DESC order 

``` 
select * from tbl_employee order by name asc;
or
select * from tbl_employee order by name DESC;
or
select * from tbl_employee order by name;

```

- w.a.q to filter from tables to find second highest salary

```
select * from tbl_employee order by salary desc limit 1,1;

```    
- w.a.q to filter from tables to find highest  salary

```

select * from tbl_employee order by salary desc limit 0,1;

```

# w.a.q to find second highest salary using subquery 

# what is subquery ? 

1. query within another query i.e called subquery 

```
select max(salary) as second_highest_salary from tbl_employee where salary < (select max(salary) from tbl_employee); 

```

# group by :

- group by filter data on group of columns in tables 

- w.a.q to sum of salary of departments

```
select sum(salary) as sumof_salary,department  from tbl_employee group by department;
```

# distinct :  

- distinct a keyword used in sql to find a different and unique values from tables there we used distinct 

```
select DISTINCT(salary) from tbl_employee 
``` 


# sql function ? 

- SQL provides some inbuilt function that can be used to completed any task  
- There are two types of sql inbuilt function 

1. aggrigate function

- sum()
- avg()
- count()
- max()
- min()

2. scalar function 

- first()
- last()
- ucase()
- lcase()
- now()
- timestamp()

**examples of all sql function**


1.  select sum(salary) as sumof_salary from tbl_employee
2.  select avg(salary) as averageof_salary from tbl_employee
3.  select COUNT(empid) as total_numbers_employee from tbl_employee
4.  select max(salary) as max_salary from tbl_employee
6.  select min(salary) as min_salary from tbl_employee
7.  select first(empid) from tbl_employee
8.  select last(empid) from tbl_employee
9.  select ucase(name) from tbl_employee
10. select lcase(name) from tbl_employee
11. select now(added_date_time) from tbl_employee
12. select timestamp(added_date_time) from tbl_employee


# TCL : transactional control language

query : commit | rollback 


# TCL have some query 

1. commit : commit is used to save data after delete 

**query**

```
START TRANSACTION;
delete from tbl_employee where empid=4;
commit; 

```


2. rollback : rollback  is used to return data   after delete from tables  

**query**

```
START TRANSACTION;
delete from tbl_employee where empid=8;
select * from tbl_employee where empid=8;
rollback;
select * from tbl_employee where empid=8;

```


# SQL windows function ....

1. SQL windows function is used to applied calculations and add unique rows to current rows in a table.

2. SQL windows function are used to add or set a rows related to the current row without grouping the result into a single row.

# types of windows function 


1. ROW_NUmber()
2. Rank()
3. Dense_RANK()
4. NTILE()
5. LAG()
6. LEAD()
7. FIRST_VALUE()
8. LAST_VALUE()
9. SUM() OVER()
10. AVG() OVER()
11. MIN() OVER()
12. MAX() OVER()
13. COUNT() OVER()

**examples of windows function**

1. select name ,salary,ROW_NUMBER() over(order by salary desc) from tbl_employee;
2. select name ,salary,Rank() over(order by salary desc) from tbl_employee;
3. select name ,salary,Dense_Rank() over(order by salary desc) from tbl_employee;
4. select name ,salary,NTILE(3) over(order by salary desc) from tbl_employee;
5. select name ,salary,LAG(salary,1) over(order by salary desc) from tbl_employee;
6. select name ,salary,LEAD(salary,1) over(order by salary desc) from tbl_employee;
7. select name ,salary,first_value(salary) over(order by salary desc) from tbl_employee;
8. select name ,salary,sum(salary) over(order by salary desc) from tbl_employee;
9. select name ,salary,avg(salary) over(order by salary desc) from tbl_employee;
10. select name ,salary,max(salary) over(order by salary desc) from tbl_employee;
11. select name ,salary,min(salary) over(order by salary desc) from tbl_employee;
12. select name ,salary,count(salary) over(order by salary desc) from tbl_employee;
13. select name ,salary,Last_values(salary) over(order by salary desc) from tbl_employee;



# what is SQL index or indexer or SQL query optimizations ? 

1. SQL index or indexer create for optimized a speed of SQL tables 
2. SQL index used to optimized speed of tables 
3. index or indexer is fast lookup data from table
4. indexer is used to one column of table of multiples columns of tables 

**two types of indexer**

1. single indexer 

```
create index indexname on tablename  (columnname);
or 
create index index_emplid on tbl_employee  (empid);  

```
2. composite indexer 

```
create index index_emplid on tbl_employee  (empid,name,salary);

``` 


# What is SQL view ? 

1. SQL view is used to create an dublicate table of virtual tables of main table
2. SQL view create a clone of main tables 
3. SQL view create to clone of main tables to hide some data from some users there we create view 

# how to create view  ?

**query**

```
create view view_employee_data as select * from tbl_employee

```

# note : when we create any query inside of virtual tables or view its performed in our main tables 

```
insert in view 
delete in view 
update in view 
change in view   

```

**case based questions and solutions of faculty based database**

1. create a database named "university"

2. create a table named "faculty" with the following columns: faculty_id (primary key), faculty_name, department, and country_id (foreign key referencing the country table) and 
provides email as unique key in faculty tables.

3. insert at least 5 records into the faculty table.

4. create a table named "courses" with the following columns: course_id (primary key), course_name, and faculty_id (foreign key referencing the faculty table).

5. insert at least 3 records into the courses table.  

6. create a table named "students" with the following columns: student_id (primary key), student_name, age, and country_id (foreign key referencing the country table).

7. insert at least 5 records into the students table.

8. create a table named "enrollments" with the following columns: enrollment_id (primary key), student_id (foreign key referencing the students table), course_id (foreign key referencing the courses table), and enrollment_date.


9. insert at least 5 records into the enrollments table.

10. write a query to select all enrollments along with student names and course names.

11. write a query to find the total number of students enrolled in each course.

12. write a query to find the faculty member teaching the most courses.

13. write a query to update the department of a faculty member with a specific faculty_id.

14. write a query to delete a student with a specific student_id.

**Note: after creating database and tables you will insert some data in that tables then you will apply all the queries on that data to understand better**

**solutions of students tables** 

```

CREATE TABLE tbl_student
(
student_id INT AUTO_INCREMENT PRIMARY KEY,
studentname VARCHAR(255),
studentage INT,
phone BIGINT,
address TEXT,
grade VARCHAR(255),

faculty_id INT,
department_id INT,
country_id INT,

CONSTRAINT faculty_id
FOREIGN KEY (faculty_id)
REFERENCES tbl_faculty(faculty_id)
ON DELETE CASCADE,

CONSTRAINT department_id
FOREIGN KEY (department_id)
REFERENCES tbl_department(department_id)
ON DELETE CASCADE,

CONSTRAINT country_id
FOREIGN KEY (country_id)
REFERENCES tbl_country(country_id)
ON DELETE CASCADE
);


create table tbl_country
(

country_id int AUTO_INCREMENT primary key,
country_name varchar(255)

)

create table tbl_department
(

department_id int AUTO_INCREMENT primary key,
dep_name varchar(255)

)
create table tbl_faculty
(

faculty_id int AUTO_INCREMENT primary key,
faculty_name varchar(255),
department varchar(255),
country_id INT,
CONSTRAINT tbl_country
FOREIGN KEY (country_id)
REFERENCES tbl_country(country_id)
ON DELETE CASCADE


)


create table tbl_courses
(

course_id int AUTO_INCREMENT primary key,
course_name varchar(255),
faculty_id INT,
CONSTRAINT tbl_faculty
FOREIGN KEY (faculty_id)
REFERENCES tbl_faculty(faculty_id)
ON DELETE CASCADE


)



create table tbl_enrollment
(

enrollment_id int AUTO_INCREMENT primary key,
course_id INT,
CONSTRAINT tbl_course
FOREIGN KEY (course_id)
REFERENCES tbl_course(course_id)
ON DELETE CASCADE,

student_id INT,
CONSTRAINT tbl_student
FOREIGN KEY (student_id)
REFERENCES tbl_student(student_id)
ON DELETE CASCADE,

enrollment_date date


)

```


**foreign key** : 

1. A fk is used to provides relationship b/w one tables to another tables 
2. A fk is used to provides more than one times 
3. A fk is create a for relationship with common field


```

1) select student with there countryname

select tbl_student .*, countryname from tbl_student join tbl_country on tbl_student.country_id=tbl_country.country_id;

or

select student_id,studentname,address,grade, countryname from tbl_student join tbl_country on tbl_student.country_id=tbl_country.country_id

2) select avg(studentage) as average_student_age from tbl_student

3) select avg(studentage) as average_student_age, studentage from tbl_student group by grade

4) select COUNT(student_id) as total_student from tbl_student group by country_id;

5) select COUNT(student_id) as total_student,country_name from tbl_student  join tbl_country on tbl_student.country_id=tbl_country.country_id group by country_name;

6) select studentname from tbl_student  where grade='A'

7) update tbl_student set grade='A' where student_id=4;

8) delete from tbl_student where student_id=4;


```


## Home work

**students based database**

1. create a database named "school"

2. create a table named "students" with the following columns: id (primary key), name, age, grade, and country_id (foreign key referencing the country table).

3. insert at least 5 records into the students table.

4. create a table named "country" with the following columns: country_id (primary key) and country_name.

5. insert at least 3 records into the country table.

6. write a query to select all students along with their country names.

7. write a query to find the average age of students in each grade.

8. write a query to find the total number of students in each country.

9. write a query to find the student with the highest grade.

10. write a query to update the grade of a student with a specific id.

11. write a query to delete a student with a specific id.



**add to cart based database**

1. create a database named "ecommerce_app"

2. create a table named "products" with the following columns: product_id (primary key), product_name, price, and stock.

3. insert at least 5 records into the products table.

4. create a table named "customers" with the following columns: customer_id (primary key), customer_name, email, and country_id (foreign key referencing the country table).

5. insert at least 3 records into the customers table.   

6. create a table named "orders" with the following columns: order_id (primary key), customer_id (foreign key referencing the customers table), product_id (foreign key referencing the products table), quantity, and order_date.

7. insert at least 5 records into the orders table.   

8. write a query to select all orders along with customer names and product names.

9. write a query to find the total revenue generated from all orders.

10. write a query to find the most popular product based on the quantity ordered.

11. write a query to update the stock of a product after an order is placed.

12. write a query to delete an order with a specific order_id.


# normailization in SQL ?

1. normalization is used to normalised any tables and provides relationship b/w them.

2. normalization is some types  ....

## types of normalization ?

1. 1-NF 
2. 2-NF
3. 3-NF
4. 4-NF

**1-NF***
```
1-NF form is just information about any tables with primary key 

```
**2-NF***

```
2-NF form is just information about any tables with primary key and provides UK for not return a dublicate data  

```
**2-NF***

```
3-NF form is just information about any tables with primary key and provides UK for not return a dublicate data and also provides a fk for relationship b/w one tables to another tables i.e 3-NF  

```

# SQL key constraints ? 

1. SQL key constraints provides limit on tables using pk | uk | fk 
2. SQL keu constaints also provides relationship b/w tables with common field with fk 

## types of key contarints 

1. pk
```
A pk is never return null values
A pk is stored unique data 
A pk only defines one times in a tables 
A pk is always auto_increments
```

2. uk
```
A uk is return once times  null values
A uk is stored unique data 
A uk defines more than one times in a tables 
A uk is never return dublicate data

```  
3. fk
```
A fk is never return null values
A fk is stored dublicate  data 
A fk  defines more than one times in a tables 
A fk provides relationship b/w one tables to another tables with common field 
```


## scenario using pk | uk | fk 

1. create a table of tbl_department
2. create a table of tbl_college
3. create a table tbl_students

```
create table tbl_department
(
depid int AUTO_INCREMENT primary KEY,
depname varchar(255)    
)

or

create table tbl_college
(
collegeid int AUTO_INCREMENT primary KEY,
collegename varchar(255)    
)

or

create table tbl_students
(
studentid int AUTO_INCREMENT primary KEY,
collegeid INT,
CONSTRAINT tbl_college
FOREIGN KEY (collegeid)
REFERENCES tbl_college(collegeid)
ON DELETE CASCADE,

depid INT,
CONSTRAINT tbl_department
FOREIGN KEY (depid)
REFERENCES tbl_department(depid)
ON DELETE CASCADE,

name varchar(255),
age int, 
adress text,
mobile bigint       
)

```
# sql join ? 

1. SQL join is used to match data from 1st table to second table if data are matched join all data otherwise return null values

## types of join ? 

1. join 
2. inner join 
3. outer join 
- left join 
- right join 
- full join (not support in mysql) 
4. cross join  
5. self join

**join**

SQL join is used to match data from 1st table to second table if data are matched join all data otherwise return null values

**syntax**

```
select 1sttablename.*, columname from 1sttablename join 2ndtablename on 1sttablename.commonfield=2nstablename.commonfield;
or
select tbl_students.*, depname from tbl_students join tbl_department on tbl_students.depid=tbl_department.depid;
or

select tbl_students.*, depname, collegename from tbl_students join tbl_department on tbl_students.depid=tbl_department.depid join tbl_college on tbl_students.collegeid=tbl_college.collegeid

or

select studentid,name,age,adress,mobile, depname, collegename from tbl_students join tbl_department on tbl_students.depid=tbl_department.depid join tbl_college on tbl_students.collegeid=tbl_college.collegeid
```

**inner join :**


SQL inner join is used to match data from 1st table to second table if data are matched join all data otherwise return null values

**syntax**

```
select 1sttablename.*, columname from 1sttablename inner join 2ndtablename on 1sttablename.commonfield=2nstablename.commonfield;
or
select tbl_students.*, depname from tbl_students inner join tbl_department on tbl_students.depid=tbl_department.depid;
or

select tbl_students.*, depname, collegename from tbl_students inner join tbl_department on tbl_students.depid=tbl_department.depid inner join tbl_college on tbl_students.collegeid=tbl_college.collegeid

or

select studentid,name,age,adress,mobile, depname, collegename from tbl_students inner join tbl_department on tbl_students.depid=tbl_department.depid inner join tbl_college on tbl_students.collegeid=tbl_college.collegeid
```


## outer join

**left join**


SQL left  join is used to match data from 1st table of left rows to second table of left rows  if data are matched join all data otherwise return null values

**syntax**

```
select 1sttablename.*, columname from 1sttablename left join 2ndtablename on 1sttablename.commonfield=2nstablename.commonfield;
or
select tbl_students.*, depname from tbl_students left join tbl_department on tbl_students.depid=tbl_department.depid;
or

select tbl_students.*, depname, collegename from tbl_students left join tbl_department on tbl_students.depid=tbl_department.depid left join tbl_college on tbl_students.collegeid=tbl_college.collegeid

or

select studentid,name,age,adress,mobile, depname, collegename from tbl_students left join tbl_department on tbl_students.depid=tbl_department.depid left join tbl_college on tbl_students.collegeid=tbl_college.collegeid
```

**right join**

SQL right  join is used to match data from 2nd table of right rows to 1st  table of right rows  if data are matched join all data otherwise return null values

**syntax**

```
select 1sttablename.*, columname from 1sttablename right join 2ndtablename on 1sttablename.commonfield=2nstablename.commonfield;
or
select tbl_students.*, depname from tbl_students right join tbl_department on tbl_students.depid=tbl_department.depid;
or

select tbl_students.*, depname, collegename from tbl_students right join tbl_department on tbl_students.depid=tbl_department.depid right join tbl_college on tbl_students.collegeid=tbl_college.collegeid

or

select studentid,name,age,adress,mobile, depname, collegename from tbl_students right join tbl_department on tbl_students.depid=tbl_department.depid right join tbl_college on tbl_students.collegeid=tbl_college.collegeid

```

**cross join**

cross join either data matched or not its return a multiplication of total rows from second tables of total rows and join tables and also return a multiple dublicates values.

```
select * from tbl_students cross join tbl_college;

```


**query based task**


1. get a collegename and departmentname inside of students table

**solution**

```
select studentid,name,age,adress,mobile, depname, collegename from tbl_students join tbl_department on tbl_students.depid=tbl_department.depid join tbl_college on tbl_students.collegeid=tbl_college.collegeid
```

2. get students with depname , collegename only of 2 students

```
select studentid,name,age,adress,mobile, depname, collegename from tbl_students join tbl_department on tbl_students.depid=tbl_department.depid join tbl_college on tbl_students.collegeid=tbl_college.collegeid where studentid in(2,3);

or

select studentid,name,age,adress,mobile, depname, collegename from tbl_students join tbl_department on tbl_students.depid=tbl_department.depid join tbl_college on tbl_students.collegeid=tbl_college.collegeid where studentid between 5 and 100;

```

## self join ?

1. self join isused to join a table to itself and return data from same table with matched columns and field of tables there we used self join.

# create a scenario for self join 

```
select e.empid, e.name as employee_name , m.name as manager_name from tbl_employee e inner join tbl_employee m on e.manager_id=m.empid;

```