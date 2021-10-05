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


select a.name, year_of_release, count(s.id) id_q
from album a join song s
on a.id=s.id
where a.year_of_release != '2020'
group by a.name, a.year_of_release order by id_q desc;


select c.name, a.name
from collection c join song_and_collection sac on c.id=sac.id_collection
join song s on sac.id_song=s.id
join album al on s.id_of_album=al.id
join album_and_artist aaa on al.id=aaa.id_of_album
join artist a on aaa.id_of_arist=a.id
where a.name = 'Jennie'
group by c.name, a.name;



# here is where i have a problem it is number 6... i dont know what i is wrong here.

select a.name, a2.name, g.name
from album a join album_and_artist aaa  on a.id=aaa.id
join artist a2 on aaa.id_of_arist=a2.id
join genre_and_artist gaa on a2.id=gaa.id_artist
join genres g on gaa.id_genres=g.id
group by a.name, g.name having count(distinct g.name) < 1;


select s.id, sac.id_song
from song s join song_and_collection sac on s.id=sac.id_song
where s.id != sac.id_song;



select a.name, s.duration
from album a join song s on a.id=s.id_of_album
where s.duration <= 2
group by a.name, s.duration;


### another problem i have is a problem 9... not sure what i am doing wrong....

  select a.name, s.id
from album a join song s on a.id=s.id_of_album
where s.id = (select limit count(s.id) from song);