create database IF NOT EXISTS goodreads;
use goodreads;
create table IF NOT EXISTS mangas (
     id int NOT NULL AUTO_INCREMENT,
     title varchar(255),
     img_src varchar(255) ,
     author  varchar(255) ,
     description text ,
     year int,
     PRIMARY KEY (id)
);
create table IF NOT EXISTS genres (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    PRIMARY KEY(id)
);
create table IF NOT EXISTS manga_genre(
    id int NOT NULL AUTO_INCREMENT,
    manga_id int NOT NULL,
    genre_id int NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (manga_id) REFERENCES mangas(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);

create table IF NOT EXISTS users (
     id int NOT NULL AUTO_INCREMENT,
     username varchar(255),
     password varchar(255) ,
     email varchar(255) ,
     PRIMARY KEY (id)
);
create table IF NOT EXISTS reviews_manga (
    id int NOT NULL AUTO_INCREMENT,
    user_id int NOT NULL,
    manga_id int NOT NULL,
    review text,
    note int,
	created_at date,
    PRIMARY KEY(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (manga_id) REFERENCES mangas(id)
);
create table IF NOT EXISTS roles (
        id int NOT NULL AUTO_INCREMENT,
        name varchar(255),
        PRIMARY KEY(id)
) ;
create table IF NOT EXISTS user_role (
        id int NOT NULL AUTO_INCREMENT,
        user_id int not null,
        role_id int not null,
        PRIMARY KEY (id) ,
        FOREIGN KEY (user_id) REFERENCES users(id)  ,
        FOREIGN KEY (role_id) REFERENCES roles(id)
) ;

insert mangas values (null, 'Berserk', 'https://media.kitsu.io/manga/8/poster_image/medium-0ec4706293ca8bc09ce9995fcc927afa.jpeg', 'Kentaro Miura', "Guts, known as the Black Swordsman, seeks sanctuary from the demonic forces that pursue him and his woman, and also vengeance against the man who branded him as an unholy sacrifice. Aided only by his titanic strength, skill, and sword, Guts must struggle against his bleak destiny, all the while fighting with a rage that might strip him of his humanity. Berserk is a dark and brooding story of outrageous swordplay and ominous fate, in the theme of Shakespeare's Macbeth. Included one-shot: Volume 14: Berserk: The Prototype", 1989);

insert mangas values (null, 'Monster', 'https://media.kitsu.io/manga/4/poster_image/medium-0cfa11da958137c4f2ce0d363c0af3a9.jpeg', 'Naoki Urasawa', "Dr. Kenzo Tenma is a renowned young brain surgeon of Japanese descent working in Europe. Highly lauded by his peers as one of the great young minds that will revolutionize the field, he is blessed with a beautiful fiancé and is on the cusp of a high promotion in the hospital he works at. However, all of that is about to change with one critical decision that Dr. Tenma faces one night – whether to save the life of a young child or that of the town's mayor. Despite being pressured by his superiors to perform surgery on the mayor, his morals force him to perform the surgery on the young child, saving his life and forfeiting the mayor’s. All of a sudden, Dr. Tenma’s world is turned upside down by his decision leading to the loss of everything he previously had. A doctor is taught to believe that all life is equal; however, when a series of murders occur in the vicinity of Dr. Tenma, all of the evidence pointing to the young child who he saved, Tenma’s beliefs are shaken.\nNaoki Urasawa’s Monster is a tale full of mystery, suspense and intrigue as Dr. Tenma journeys to find out the true identity of the young child. In turn, the fate of the world may depend on it.\n\n(Source: MAL Rewrite)", 1994);

insert genres values (null, 'Action');
insert genres values (null, 'Aventure');
insert genres values (null, 'Comedie');
insert genres values (null, 'Drama');
insert genres values (null, 'Sci-fi');
insert genres values (null, 'Mystere');
insert genres values (null, 'Magie');
insert genres values (null, 'Surnaturelle');
insert genres values (null, 'Police');

insert manga_genre values (null, 1,1);
insert manga_genre values (null, 1,2);
insert manga_genre values (null, 1,4);
insert manga_genre values (null, 1,8);

insert users values (null, 'otaku75', 'password', 'otaku75@gmail.com');

insert reviews_manga values (null, 1,1,'Un manga incroyable !', 5,now());
insert reviews_manga values (null, 1,1,'Excellent', 5,now());
insert reviews_manga values (null, 1,9,"J'aime beaucoup", 4,now());
