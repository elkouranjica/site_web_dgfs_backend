1- `docker compose up -d`

2- Miditra ao amin bashn'lay docker aveo `docker compose exec web bash`

3- Manao migration pour base de données `python manage.py makemigrations main_user main_etablissement main_post main_institution main_message`

4- Aveo manao migrate pour création des tables dans postgres python manage.py migrate

5- Dia mi-créer superuser aveo `python manage.py createsuperuser`

6- Fenoina : 'Matricule' puis entrer, dia mampiditra 'mot de passe' dia entrer hatrany

7- Manokatra postman ohatra dia afaka mi-test an'ireto lien ireto :

/* DEPLOYMENT */

01 - Dump data from the Localhost into /fixtures/dump.json

02 - Push the dumped data to git
 
03 - commit/pull change

04 - Connect to the Ssh on the server

05 - pull data from git

06 - python manage.py 