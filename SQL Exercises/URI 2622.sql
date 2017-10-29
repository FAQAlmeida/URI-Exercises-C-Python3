select customers.name from customers
where customers.id in (select id_customers from legal_person)