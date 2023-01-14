drop table if exists places;

create table `places` (
  `id` int not null auto_increment,
  `city` varchar(85) not null,
  `county` varchar(80) not null,
  `country` varchar(56) not null,
  primary key (`id`),
  UNIQUE KEY (city, county, country)
);

drop table if exists people;

create table `people` (
  `id` int not null auto_increment,
  `given_name` varchar(80) not null,
  `family_name` varchar(80) not null,
  `date_of_birth` date not null,
  `place_of_birth` varchar(56) not null,
  primary key (`id`),
  FOREIGN KEY (place_of_birth) REFERENCES places(city)
);