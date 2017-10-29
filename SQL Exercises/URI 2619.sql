select products.name, providers.name, products.price from products
inner join categories on (categories.id = products.id_categories)
inner join providers on (products.id_providers = providers.id)
where products.price > 1000 and categories.name = 'Super Luxury'