select products.name from products
inner join providers on (providers.id = products.id_providers)
where products.amount < 20 and products.amount > 10 and providers.name like 'P%'