# projet-docker

# Lancer le projet 
###  Se mettre à la racine du projet : là où se trouve le fichier docker-compose.yml
docker-compose up 

# Lancer MySQL
docker exec -it projet-docker_db_1 bash
mysql -uroot -proot


.
├── app
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── db
│   └── init.sql
├── docker-compose.yml
├── README.md
└── tests
    └── test.py


