select * from products;

select id, name from products
where is_sale = true;

select name ,price from products
where name = 'Pankaj';

select * from  products where price >= 200 and is_sale ='true';


select name,created_at from products
where id >=1 and id <=3;


select name from products where id IN(1,2,3);


select name from products 
where name Like '%mouse wi%'


select 








