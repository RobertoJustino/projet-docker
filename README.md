# projet-docker

# Lancer le projet 
###  Se mettre à la racine du projet : là où se trouve le fichier docker-compose.yml
docker-compose up 

# Lancer MySQL

  docker exec -it projet-docker_db_1 bash  
  mysql -uroot -proot


```
.
├── app
│   ├── app.py
│   ├── Dockerfile
│   ├── __pycache__
│   │   └── app.cpython-39.pyc
│   ├── requirements.txt
│   ├── static
│   │   └── css
│   │       └── w3.css
│   └── templates
│       ├── index.html
│       ├── manga_form.html
│       ├── manga.html
│       └── mangas.html
├── db
│   └── init.sql
├── docker-compose.yml
├── README.md
└── tests
    └── test.py


```


![image](Modèle_BDD.png)