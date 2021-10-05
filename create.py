create table Artist (
    Id serial primary key,
    Name varchar(50) not null,
    Stage_name varchar(50) not null,
    Birthday date
);

create table Album (
    Id serial primary key,
    Name varchar(50) not null,
    Year_of_release integer
);

create table Song (
    Id serial primary key,
    Name varchar(50) not null,
    Duration integer,
    Id_of_album integer references Album(Id)
);

create table Genres (
    Id serial primary key,
    Name varchar(50) not null
);

create table Collection (
    Id serial primary key,
    Name varchar(50) not null,
    Year_of_release integer
);

create table if not exists Album_and_Artist(
    Id serial primary key,
    id_of_arist integer not null references Artist(Id),
    id_of_album integer not null references Album(Id)
);

create table if not exists Genre_and_Artist(
    Id serial primary key,
    id_artist integer not null references Artist(Id),
    id_genres integer not null references Genres(Id)
);