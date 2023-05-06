create or replace  procedure data_project.sp_airlines()
language plpgsql
as $$
begin 
truncate table data_project.airlines;
insert into  data_project.airlines
(
	id,
	name,
	country,
	logo, 
    slogan,
    head_quaters,
    website,
    established
) 
select id::bigint,
       name,
       country,
       logo, 
       slogan,
       head_quaters,
       website,
       established
from data_project.stg_airlines;
end
$$;

