SELECT
    products.name,
    providers.name,
    products.price
FROM
    products
    INNER JOIN categories ON (categories.id = products.id_categories)
    INNER JOIN providers ON (products.id_providers = providers.id)
WHERE
    products.price > 1000
    AND categories.name = 'Super Luxury'
