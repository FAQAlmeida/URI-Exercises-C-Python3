SELECT
    products.name,
    providers.name,
    categories.name
FROM
    products
    INNER JOIN categories ON (categories.id = products.id_categories)
    INNER JOIN providers ON (products.id_providers = providers.id)
WHERE
    providers.name = 'Sansul SA'
    AND categories.name = 'Imported'
