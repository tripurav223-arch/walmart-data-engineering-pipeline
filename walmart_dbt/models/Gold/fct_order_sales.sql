{{ config(materialized='table', schema='gold') }}

SELECT
    o.order_id,
    o.customer_id,
    c.customer_name,
    c.city,
    o.order_date,
    o.order_status,
    i.order_item_id,
    i.product_id,
    i.quantity,
    i.unit_price,
    i.quantity * i.unit_price AS item_total

FROM {{ ref('stg_orders') }} o

LEFT JOIN {{ ref('stg_customers') }} c
    ON o.customer_id = c.customer_id

LEFT JOIN {{ ref('stg_order_items') }} i
    ON o.order_id = i.order_id