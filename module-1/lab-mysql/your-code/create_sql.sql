/*CREATE DATABASE lab_mysql;*/
USE lab_mysql;
/*CREATE TABLE cars
(
ID INT,
VIN VARCHAR(100),
Manufacturer TEXT,
año INT,
color TEXT
);*/

/*CREATE TABLE customers
(
ID INT,
customer_ID VARCHAR(100),
nombre TEXT,
phone VARCHAR(100),
email VARCHAR(100),
address TEXT,
city VARCHAR(100)
);*/

/*CREATE TABLE salespersons
(
ID INT,
staff_ID VARCHAR(100),
nombre TEXT,
store TEXT
);*/

CREATE TABLE invoices
(
ID INT,
invoice_number BIGINT,
fecha DATE,
car INT,
customer INT,
sales_person INT
);
