select products.name, providers.name, categories.name from products
inner join categories on (categories.id = products.id_categories)
inner join providers on (products.id_providers = providers.id)
where providers.name = 'Sansul SA' and categories.name = 'Imported'