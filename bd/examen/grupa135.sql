describe jobs;

select e.job_id,j.job_title from employees e, jobs j where e.department_id = 30 and e.job_id = j.job_id;

select e.last_name, d.department_name, l.city from employees e, departments d, locations l where e.department_id = d.department_id and d.location_id = l.location_id;
select e.last_name, d.department_name, l.city from employees e join departments d on (e.department_id = d.department_id) join locations l using (location_id);

select e1.last_name, e1.hire_date, e2.last_name, e2.hire_date from employees e1 join employees e2 on (e1.manager_id = e2.employee_id) where e1.hire_date < e2.hire_date;


select e1.last_name, to_char(e1.hire_date, 'MONTH YYYY') from employees e1 join employees e2 
on (e1.department_id = e2.department_id)
where e1.last_name like '%a%'
and e1.last_name != 'Gates' 
and e2.last_name = 'Gates';

select distinct e1.employee_id, e1.last_name, d.department_id, d.department_name
from employees e1 join employees e2 on e1.department_id = e2.department_id
join departments d on e1.department_id = d.department_id
where lower(e2.last_name) like '%t%'
order by e1.last_name;


select e1.last_name, e1.salary, j.job_title, l.city, c.country_name
from employees e1 
join employees m on (e1.manager_id = m.employee_id)
join jobs j on (e1.job_id = j.job_id)
left join departments d on (e1.department_id = d.department_id)
left join locations l on (d.location_id = l.location_id)
left join countries c on (l.country_id = c.country_id)
where m.last_name = 'King';

select d.department_id, d.department_name, e1.last_name, j.job_title, to_char(e1.salary, '$99,999.00')
from employees e1 join departments d on (e1.department_id = d.department_id)
join jobs j on (e1.job_id = j.job_id)
where d.department_name like '%ti%'
order by d.department_name, e1.last_name;

select e.last_name, e.department_id, d.department_name, l.city, j.job_title
from employees e join departments d on (e.department_id = d.department_id)
join locations l on (d.location_id = l.location_id)
join jobs j on (e.job_id = j.job_id)
where l.city='Oxford';

select e.last_name, d.department_name
from employees e full outer join departments d
on (e.department_id = d.department_id);

select d.department_name from departments d where d.department_name like '%re%'
union 
select d.department_name from departments d join employees e on (e.department_id = d.department_id)
where e.job_id = 'SA_REP';

select department_id from departments
where department_id not in
(
    select d.department_id from departments d
    join employees e on d.department_id = e.department_id
);

SELECT d.department_id
FROM departments d
WHERE LOWER(d.department_name) LIKE '%re%'
INTERSECT
SELECT e.department_id
FROM employees e
WHERE e.job_id = 'HR_REP';

select e.employee_id, e.job_id, e.last_name from employees e
where salary > 3000
union
select e.employee_id, e.job_id, e.last_name from employees e
join jobs j on (e.job_id = j.job_id)
where e.salary = (j.min_salary + j.max_salary)/2;

select 'Departamentul ' || d.department_name || ' este condus de ' || nvl(m.last_name, 'nimeni')
|| ' si ' from departments d left join employees m on m.employee_id = d.manager_id;




select e.last_name, e.hire_date from employees e
where e.hire_date > (select hire_date from employees where last_name='Gates');

select last_name, salary
from employees
where department_id in ( select department_id from employees where last_name = 'Gates')
and last_name != 'Gates';

select last_name, salary from employees
where manager_id = (select employee_id from employees where manager_id is null);

select last_name, department_id, salary from employees
where (department_id, salary) in (select department_id, salary from employees
where commission_pct is not null);


select e.employee_id, e.last_name, e.salary from employees e
where e.salary >
(
    select (j.min_salary+j.max_salary)/2 from jobs j
    where e.job_id = j.job_id
)
and e.job_id in
(
    select m.job_id from employees m
    where e.job_id = m.job_id
    and lower(m.last_name) like '%t%'
);

select e.last_name from employees e
where e.salary > all (
    select e2.salary from employees e2 
    where e2.job_id like '%CLERK%'
);

select e.last_name, d.department_name, e.salary 
from employees e join departments d on(e.department_id = d.department_id)
where e.commission_pct is null
and (select commission_pct from employees m where e.manager_id = m.employee_id) is not null;


select e.last_name,(select department_name from departments d where e.department_id = d.department_id), e.salary, (select j.job_title from jobs j where e.job_id = j.job_id)
from employees e
where (e.salary,e.commission_pct) in
(
    select e2.salary, e2.commission_pct from employees e2
    where e2.department_id in
        (
        select department_id from departments
        where location_id in
        (
            select location_id from locations
            where city = 'Oxford'
        )
        )
);

select e.last_name NUME,
    (select department_name from departments where department_id = e.department_id) DEPARTAMENT,
    nvl(e.salary, 0) SALARIU,
    (select job_title from jobs where job_id = e.job_id) JOB
from employees e
where (nvl(e.salary, 0), nvl(e.commission_pct, 0)) in 
        (select nvl(salary, 0), nvl(commission_pct, 0)
            from employees
            where department_id in 
                    (select department_id
                        from departments
                        where location_id in
                                (select location_id
                                    from locations
                                    where city = 'Oxford')));



