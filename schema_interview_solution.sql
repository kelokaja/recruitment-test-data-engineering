drop table if exists people;
drop table if exists places;

create table people (
  id int not null auto_increment,
  given_name varchar(80) default null,
  family_name varchar(80) default null,
  date_of_birth varchar(10) default null,
  place_of_birth varchar(128) not null,
  primary key (id),
  FOREIGN KEY (place_of_birth) REFERENCES places(city)
);

create table places (
  city varchar(128) not null,
  county varchar(128) default null,
  country varchar(128) default null,
  primary key (city)
);