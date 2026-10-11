select *
from {{ source('bronze', 'employees') }}