## Introduction

The code in this repository generates synthetic data for the task in which the tables are: transactions, customers, and salesmen and orders. The generated data is then analyzed using SQL queries executed with the DuckDB database.


The table  has attributes such as orderId, Date, Amount, CustomerId, SalesId, Name, Province, and Age.

The Queries performed are on the following tasks:

1. Calculating average, minimum, and maximum ages of salesmen by province.
SQL Query:"select province, avg(age) as AverageAge,min(age) as MinAge ,max(age) as MaxAge from sales group by province"

2. Summarizing total sales amounts by year and month.
a)SQL Query for year:"select date_part('year',Date) as Years, round(sum(amount),2) from transaction group by Years"
b)SQL Query for month: "select date_part('month', Date) as Month, round(sum(amount),2) as TotalSum from transaction group by Month"

3. Aggregating sales amounts and customer counts by province.
SQL Query: "select Province, round(sum(amount),2) as TotalAmount, round(avg(amount),2) as AvgAmount, count(c.customerid) as TotalCustomers from transaction t join orders as o on t.orderid=o.orderid join customers as c on c.customerid=o.customerid group by Province order by TotalAmount,AvgAmount,Province ")



4. Identifying Top 10 salespersons with maximum sales by Amount
   SQL Query: "select s.salesid, sum(t.amount) as TotalSales  from transaction t join orders as o on t.orderid=o.orderid join sales as s on s.salesid=s.salesid group by s.salesid order by TotalSales desc limit 10 "

5. Analyzing sales amounts and customer counts by age groups.
   a) SQL Query sales amounts: "select sum(case when c.age <=25 then 1 else 0 end) as Age_0to25, sum(case when c.age >25 and c.age<=50 then 1 else 0 end) as Age_26to50, sum(case when c.age >50 then 1 else 0 end) as Age_51to100 from transaction t join orders o on t.orderid=o.orderid join customers c on o.customerid=c.customerid"
   b) SQL Query customers amount: "select round(sum(case when c.age <=25 then t.amount else 0 end),2) as Amt_0to25, round(sum(case when c.age >25 and c.age<=50 then t.amount else 0 end),2) as Amt_26to50, round(sum(case when c.age >50 then t.amount else 0 end),2) as Amt_51to100 from transaction t join orders o on t.orderid=o.orderid join customers c on o.customerid=c.customerid"

