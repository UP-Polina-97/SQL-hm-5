select name, count(id_artist) artist_q
from genres g join genre_and_artist a
on g.id=a.id_artist
group by g.name
order by artist_q desc;

select a.name, year_of_release, count(s.id) id_q
from album a join song s
on a.id=s.id
where a.year_of_release between 2019 and 2020
group by a.name, a.year_of_release order by id_q desc;

select a.name, avg(s.duration) duration_q
from album a join song s
on a.id=s.id group by a."name" order by duration_q desc;

select a.name, year_of_release, s.id
from album a join song s
on a.id=s.id
where a.year_of_release != '2020'
group by a.name, a.year_of_release, s.id order by s.id desc;


select distinct c.name, a.name
from collection c join song_and_collection sac on c.id=sac.id_collection
join song s on sac.id_song=s.id
join album al on s.id_of_album=al.id
join album_and_artist aaa on al.id=aaa.id_of_album
join artist a on aaa.id_of_arist=a.id
where a.name = 'Jennie';


select a.name
from album a join album_and_artist aaa  on a.id=aaa.id
join artist a2 on aaa.id_of_arist=a2.id
join genre_and_artist gaa on a2.id=gaa.id_artist
join genres g on gaa.id_genres=g.id
group by a.name having count(distinct g.name) > 1;


select s.name, sac.id_song
from song s left join song_and_collection sac on s.id=sac.id_song
where sac.id_song is null;

select ar.name, s.name, s.duration
from artist ar join album_and_artist aaa  on ar.id = aaa.id_of_arist
join album a on aaa.id_of_album = a.id
join song s on a.id = s.id_of_album
where s.duration = (select min(duration) from song);

select a.name
from album a join song s on a.id=s.id_of_album
group by a.name, s.id
having s.id = (select count(id) from song group by a.name order by s.id limit 1);