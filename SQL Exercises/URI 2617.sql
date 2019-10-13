SELECT
    products1.name,
    providers.NAME
FROM
    products1
    INNER JOIN providers ON (providers.id = products1.id_providers)
WHERE
    providers.name = 'Ajax SA'
