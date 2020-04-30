--1
select cust_id, cust_name from customer_tbl
where cust_state in ('IN', 'OH','MI','IL')
and lower(cust_name) like 'a%' 
or lower(cust_name) like 'b%';

--2 a)
select prod_id, prod_desc, cost from products_tbl
where cost>1 and cost<12.50;

--2 b)
select prod_id, prod_desc, cost from products_tbl
where not(cost>1 and cost<12.50);

--3
select * from employee_tbl;
select lower(first_name) || '.' || lower(last_name) || '@ittech.com' from employee_tbl;

--4
select 'NAME = ' ||last_name||', '||first_name || chr(13) || chr(10) ||
'EMP_ID = ' || substr(emp_id,1,3) ||'-'|| substr(emp_id,4,2) ||'-'||substr(emp_id,6,5) ||chr(13) || chr(10) ||
'PHONE = ('||substr(phone,1,3) ||')'||substr(phone,4,3)||'-'||substr(phone,7,4) || chr(13) || chr(10) ||chr(13) || chr(10)  "Data"
from employee_tbl;

--5
select emp_id, to_char(date_hire,'YYYY') from employee_pay_tbl;

--6
select emp_id, last_name, first_name, salary,bonus from employee_tbl natural join employee_pay_tbl;

--7
select cust_name, ord_num, ord_date from customer_tbl c 
join orders_tbl o on c.cust_id = o.cust_id 
where c.cust_state like 'I%';

--8
select o.ord_num, o.qty, e.last_name, e.first_name, e.city
from orders_tbl o join employee_tbl e
on o.sales_rep = e.emp_id;

--9
select o.ord_num, o.qty, e.last_name, e.first_name, e.city
from orders_tbl o right join employee_tbl e
on o.sales_rep = e.emp_id;

--10
select emp_id from employee_tbl where middle_name is null;

--11
select emp_id, nvl(salary,pay_rate*8*5*52) + nvl(bonus,0) from employee_pay_tbl;

--12
--varianta 1
select e1.last_name "Nume" , e2.salary "Salariu", e2.position "Pozitie", 
decode(lower(e2.position),'marketing',e2.salary*1.10,'salesman', e2.salary*1.15, e2.salary) "Salariu modificat" 
from employee_tbl e1 natural join employee_pay_tbl e2;
--varianta 2
select e1.last_name "Nume", e2.salary "Salariu", e2.position "Pozitie",
case lower(e2.position)
when 'marketing' then e2.salary*1.10
when 'salesman' then e2.salary*1.15
else e2.salary end as "Salariu modificat"
from employee_tbl e1 join employee_pay_tbl e2 
on e1.emp_id = e2.emp_id;
