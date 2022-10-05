use lqn
declare @col NVARCHAR(MAX);
declare @col2 NVARCHAR(MAX) = '';
declare @query NVARCHAR(MAX);
declare @query2 NVARCHAR(MAX);

--We have 3 way to make the quotename string agg of the column to pivot table
--Way1: Using string_agg() function
set @col =
(select string_agg(quote,', ') within group (order by quote asc)
from
(select distinct quotename(order_priority) as quote
from orders
) t)

--Way2: Using the recursion of cursor
select @col2 += QUOTENAME(order_priority) + ', ' 
from 
(select distinct order_priority
from orders) pd
set @col2 = LEFT(@col2, len(@col2) - 1)

--Way3: using the loops of cusor and combine with coalesce() function
declare @col3 NVARCHAR(MAX);
select @col3 = coalesce(@col3 + ',','') +  QUOTENAME(order_priority)
from (select distinct [order_priority] from orders) tab


-- Dynamic Query
SET @query2 = 
'select province, '+@col+'
from
(select
	od1.province,
	od1.order_priority,
	profit
from orders od1
) od2
pivot
(sum(profit)
for order_priority in ('+@col+') 
) as pivottable
order by province asc'

execute sp_executesql @query2
