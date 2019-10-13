SELECT
    products.name
FROM
    products
    INNER JOIN providers ON (providers.id = products.id_providers)
WHERE
    products.amount < 20
    AND products.amount > 10
    AND providers.name LIKE 'P%'
