{{ config(materialized='ephemeral') }}

SELECT *
FROM {{ ref('stg_employees') }}