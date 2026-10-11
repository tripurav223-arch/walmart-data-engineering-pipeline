{{ config(materialized='ephemeral') }}

SELECT *
FROM {{ ref('stg_orders') }}