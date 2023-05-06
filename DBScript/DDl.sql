
create table data_project.stg_airlines
( 
	id varchar primary key,
    name varchar,
    country varchar, 
    logo varchar, 
    slogan varchar,
    head_quaters  varchar,
    website varchar,
    established varchar
);
  
create table data_project.airlines
(
	id bigint, 
	name varchar,
	country varchar, 
	logo varchar,
	slogan varchar,
    head_quaters  varchar, 
    website varchar,
    established varchar
);
                                        
                                   