create or replace  procedure data_project.sp_airlines()
language plpgsql
as $$
begin 
-----------------Truncating data_project.airlines table ----------------
truncate table data_project.airlines;
-----------------Inserting staging data into data_project.airlines-------
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

