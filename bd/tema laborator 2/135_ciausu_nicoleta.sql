--1
select COUNT(*) from employees where last_name like 'K%';

--2
select first_name, last_name, employee_id, salary from employees where salary = (select min(salary) from employees);

--3
select distinct employee_id, last_name, department_id from employees where department_id = 30
order by last_name;

--4
select employee_id, first_name, last_name, (select count(1) from employees where manager_id = e.employee_id) as "nr subalterni" from employees e;

--5
select employee_id, first_name, last_name from employees e where
(select count(1) from employees where last_name = e.last_name) = 2;

--6
select department_id, department_name from departments d where
(select COUNT(distinct job_id) from employees where department_id = d.department_id) >=2;

--7
select qty, prod_id from orders_tbl o where 
(select count(1) from products_tbl where prod_desc) >=1;


--8

select cust_name, 'client' from customer_tbl
union
select last_name || ' ' || first_name, 'angajat'
from employee_tbl;

--9
select distinct prod_desc from products_tbl p, orders_tbl o
where p.prod_id = o.prod_id
and exists (select * from orders_tbl oo
where sales_rep = o.sales_rep and 
(select lower(prod_desc) from products_tbl
where prod_id = oo.prod_id) like '% p%');

--10
select cust_name
from customer_tbl c
where exists 
(select 1 from orders_tbl where cust_id = c.cust_id
and TO_CHAR(ord_date, 'dd') = 17);

--11
select last_name, first_name, bonus from employee_pay_tbl p, employee_tbl e
where e.emp_id = p.emp_id and salary < 32000 and bonus * 17 < 32000;

--12
select first_name, last_name, nvl(sum(o.qty),0)
from employee_tbl e left join orders_tbl o on e.emp_id = o.sales_rep
group by e.emp_id, e.first_name, e.last_name
having sum(o.qty) > 50 or nvl(sum(o.qty),0)=0;

--13
select last_name, salary, MAX(ord_date) from (employee_tbl e1
join employee_pay_tbl e2 on e1.emp_id = e2.emp_id)
join orders_tbl o on e1.emp_id = o.sales_rep
group by last_name, salary, o.sales_rep;

--14
select prod_desc from products_tbl
where cost > (select avg(cost) from products_tbl);

--15
select last_name, first_name, salary, bonus, (select sum(salary) from employee_pay_tbl),
(select sum(bonus) from employee_pay_tbl)
from employee_tbl e join employee_pay_tbl p on e.emp_id = p.emp_id
group by last_name, first_name, salary, bonus;

--16
select unique city from employee_tbl e
where (select count(1) from orders_tbl o
where sales_rep = e.emp_id) >=
(select max(count(1)) from orders_tbl 
group by sales_rep);

--17
select emp_id, last_name, 
count(decode( to_char(ord_date, 'mm'), 9, 1)) "Septembrie",
count(decode( to_char(ord_date, 'mm'), 10, 1)) "Octombrie"
from employee_tbl e left join orders_tbl o
on emp_id = sales_rep
group by emp_id, last_name;

--18
select cust_name, cust_city from customer_tbl
where regexp_like(cust_address, '^[0-9]')
and cust_id not in (select cust_id from orders_tbl);

--19
select distinct e.emp_id, e.last_name, e.city, c.cust_id, c.cust_name, c.cust_city 
from employee_tbl e, customer_tbl c
where exists(select 1 from orders_tbl where sales_rep = e.emp_id and cust_id = c.cust_id)
and city != cust_city;

--20
select avg(nvl(salary,0)) from employee_pay_tbl;

--21
-- a. da
-- b. nu. employee_id nu e un tabel. ar trebui employee_pay_tbl acolo

--22
select last_name, pay_rate from employee_tbl e, employee_pay_tbl p
where e.emp_id = p.emp_id
and pay_rate > (select max(pay_rate) from employee_tbl e2, employee_pay_tbl p2
where e2.emp_id = p2.emp_id and upper(last_name) like '%LL%');


