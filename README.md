1- `docker compose up -d`

2- Miditra ao amin bashn'lay docker aveo `docker compose exec web bash`

3- Manao migration pour base de données `python manage.py makemigrations main_user main_etablissement main_post`

4- Aveo manao migrate pour création des tables dans postgres `python manage.py migrate`

5- Dia mi-créer superuser aveo `python manage.py createsuperuser`

6- Fenoina : 'Matricule' puis entrer, dia mampiditra 'mot de passe' dia entrer hatrany

7- Manokatra postman ohatra dia afaka mi-test an'ireto lien ireto :

a/ Application pour Authentification

    - Enregistrement d'un nouvel utilisateur : 
        * Lien : `localhost:8000/api/auth/register/` en method POST
        * Data : exemple = { "matricule": "123456", "password":"password" }
    - Login :
        * Lien : `localhost:8000/api/auth/login/` en method POST
        * Data : exemple = { "matricule": "123456", "password":"password" }
    - Logout :
        * Lien : `localhost:8000/api/auth/logout/` en methode POST
        * pas de data
        
b/ Application pour les Etablissements (CHU pour l'instant)
    
    Lien pour obtenir la liste des CHU : `localhost:8000/api/etablissement/` en mode GET
    Data exemple obtenu : 
        ==> {
                "count": 1,
                "next": null,
                "previous": null,
                "results": [
                    {
                        "id": "a40b1555cccc4954a716099df32fc7f3",
                        "name": "HJRA",
                        "categorie": "CHU",
                        "adresse": "Ampefiloha Antananarivo",
                        "logo": "http://localhost:8000/media/logo_a40b1555-cccc-4954-a716-099df32fc7f3/logo.jpeg",
                        "descriptions": [
                            {
                                "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce euismod sem eu metus scelerisque, id fringilla tortor congue. Vestibulum bibendum, lacus quis euismod fermentum, felis elit tincidunt tellus, nec ultricies mauris dui vel justo. Aliquam erat volutpat. Integer ac metus at augue lacinia faucibus. Vivamus ac lacus non quam posuere imperdiet. In hac habitasse platea dictumst. Pellentesque sit amet tristique sapien. Nunc auctor nisl vitae tellus varius, vitae blandit nisl volutpat.",
                                "updated": "2023-12-11T07:16:46.452377Z"
                            }
                        ],
                        "services": [
                            {
                                "name": "Chirurgie pédiatrique"
                            },
                            {
                                "name": "Chirurgie vasculaire"
                            }
                        ],
                        "directeur": {
                            "nom": "Rakoto",
                            "prenom": "Jean",
                            "categorie": "DE",
                            "matricule": "123456",
                            "photo": "/media/photo_DE/leba.png"
                        },
                        "contacts": [
                            {
                                "contact_accueil": "0331122233",
                                "contact_urgence": "0341122233",
                                "contact_ambulance": "0321122233",
                                "contact_de": "0332233344",
                                "contact_dat": "0342233344",
                                "contact_daf": "0322233344"
                            }
                        ]
                    }
                ]
            }  
    
    Lien pour obtenir un Etablissement avec l'id : "a40b1555cccc4954a716099df32fc7f3"
    Data obtenu : 
    ==> {
            "id": "a40b1555cccc4954a716099df32fc7f3",
            "name": "HJRA",
            "categorie": "CHU",
            "adresse": "Ampefiloha Antananarivo",
            "logo": "http://localhost:8000/media/logo_a40b1555-cccc-4954-a716-099df32fc7f3/logo.jpeg",
            "descriptions": [
                {
                    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce euismod sem eu metus scelerisque, id fringilla tortor congue. Vestibulum bibendum, lacus quis euismod fermentum, felis elit tincidunt tellus, nec ultricies mauris dui vel justo. Aliquam erat volutpat. Integer ac metus at augue lacinia faucibus. Vivamus ac lacus non quam posuere imperdiet. In hac habitasse platea dictumst. Pellentesque sit amet tristique sapien. Nunc auctor nisl vitae tellus varius, vitae blandit nisl volutpat.",
                    "updated": "2023-12-11T07:16:46.452377Z"
                }
            ],
            "services": [
                {
                    "name": "Chirurgie pédiatrique"
                },
                {
                    "name": "Chirurgie vasculaire"
                }
            ],
            "directeur": {
                "nom": "Rakoto",
                "prenom": "Jean",
                "categorie": "DE",
                "matricule": "123456",
                "photo": "/media/photo_DE/leba.png"
            },
            "contacts": [
                {
                    "contact_accueil": "0331122233",
                    "contact_urgence": "0341122233",
                    "contact_ambulance": "0321122233",
                    "contact_de": "0332233344",
                    "contact_dat": "0342233344",
                    "contact_daf": "0322233344"
                }
            ]
        }
        
c/ Application pour les Actualités Posts :
    
    Lien pour obtenir la liste des Actualités : `localhost:8000/api/post/` en mode GET
    Data obtenu :
        ==> {
                "count": 1,
                "next": null,
                "previous": null,
                "results": [
                    {
                        "id": "5f072b72f7fa4420be7c500d2e9d4754",
                        "created": "2023-12-11T08:09:44.508977Z",
                        "updated": "2023-12-11T08:09:44.508992Z",
                        "tags": [
                            "caravane"
                        ],
                        "author": {
                            "last_name": "",
                            "first_name": ""
                        },
                        "public_id": "5f072b72-f7fa-4420-be7c-500d2e9d4754",
                        "title": "Caravane Médical",
                        "summary": "Lorem ipsum dolor met kea",
                        "slug": "caravane-medical",
                        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce euismod sem eu metus scelerisque, id fringilla tortor congue. Vestibulum bibendum, lacus quis euismod fermentum, felis elit tincidunt tellus, nec ultricies mauris dui vel justo. Aliquam erat volutpat. Integer ac metus at augue lacinia faucibus. Vivamus ac lacus non quam posuere imperdiet. In hac habitasse platea dictumst. Pellentesque sit amet tristique sapien. Nunc auctor nisl vitae tellus varius, vitae blandit nisl volutpat.\r\n\r\nQuisque vitae consectetur urna. Integer vel sem at lacus gravida egestas. Duis sed dolor ac ex hendrerit accumsan. Aenean vel justo ut tortor tristique tincidunt nec in mauris. Curabitur nec libero vitae elit tristique imperdiet. Phasellus interdum augue vel est venenatis, vel pharetra orci fermentum. Nullam nec tincidunt orci. Nam interdum sagittis lectus, vitae feugiat leo facilisis sit amet. Suspendisse potenti. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam erat volutpat. Vivamus tincidunt consequat metus, ac posuere urna facilisis eget.\r\n\r\nPellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In hac habitasse platea dictumst. Sed ac arcu ac elit blandit tincidunt nec sit amet purus. Ut vel ultrices nisi. Sed ac dapibus augue. Vivamus vestibulum tristique mi nec dictum. Praesent sagittis justo at dui cursus cursus. Sed ultrices, nulla a euismod scelerisque, tellus augue fermentum purus, nec efficitur elit felis vitae arcu. Sed vel orci et tellus consequat hendrerit id in libero. In at nisl nec justo finibus sagittis. Phasellus id fermentum mauris. Vivamus vitae vestibulum enim.\r\n\r\nQuisque malesuada, nunc vel imperdiet vulputate, velit quam consectetur dui, id suscipit sem orci id tortor. Vestibulum bibendum arcu vitae neque ultricies, eu tempus odio volutpat. Suspendisse nec eros eu felis dapibus malesuada nec eu justo. Duis sit amet libero at purus aliquam auctor non ac augue. Ut in tincidunt arcu, id condimentum libero. Maecenas id magna purus. Pellentesque non justo vitae libero fringilla ultricies. Sed gravida, justo ut iaculis lacinia, velit nisl sollicitudin odio, eu tempus est lacus id enim. Suspendisse potenti.\r\n\r\nFusce aliquam euismod felis, in laoreet odio facilisis non. Proin hendrerit lacus non velit fringilla feugiat. Maecenas facilisis augue ut ullamcorper iaculis. Aliquam vel felis in urna bibendum suscipit a ac enim. Duis ut turpis sit amet justo ullamcorper pellentesque. Nulla facilisi. Nunc laoreet risus id massa feugiat, vel malesuada nulla tristique. Integer vitae tortor vel lacus sollicitudin pellentesque in ut est.",
                        "publish": "2023-12-11T07:57:59Z",
                        "status": "PB",
                        "image": "http://localhost:8000/media/post_5f072b72-f7fa-4420-be7c-500d2e9d4754/dgfs.png"
                    }
                ]
            }
            
    Lien pour obtenir une Actualité avec l'id : "5f072b72f7fa4420be7c500d2e9d4754"
    Data obtenu : {
                        "id": "5f072b72f7fa4420be7c500d2e9d4754",
                        "created": "2023-12-11T08:09:44.508977Z",
                        "updated": "2023-12-11T08:09:44.508992Z",
                        "tags": [
                            "caravane"
                        ],
                        "author": {
                            "last_name": "",
                            "first_name": ""
                        },
                        "public_id": "5f072b72-f7fa-4420-be7c-500d2e9d4754",
                        "title": "Caravane Médical",
                        "summary": "Lorem ipsum dolor met kea",
                        "slug": "caravane-medical",
                        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce euismod sem eu metus scelerisque, id fringilla tortor congue. Vestibulum bibendum, lacus quis euismod fermentum, felis elit tincidunt tellus, nec ultricies mauris dui vel justo. Aliquam erat volutpat. Integer ac metus at augue lacinia faucibus. Vivamus ac lacus non quam posuere imperdiet. In hac habitasse platea dictumst. Pellentesque sit amet tristique sapien. Nunc auctor nisl vitae tellus varius, vitae blandit nisl volutpat.\r\n\r\nQuisque vitae consectetur urna. Integer vel sem at lacus gravida egestas. Duis sed dolor ac ex hendrerit accumsan. Aenean vel justo ut tortor tristique tincidunt nec in mauris. Curabitur nec libero vitae elit tristique imperdiet. Phasellus interdum augue vel est venenatis, vel pharetra orci fermentum. Nullam nec tincidunt orci. Nam interdum sagittis lectus, vitae feugiat leo facilisis sit amet. Suspendisse potenti. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam erat volutpat. Vivamus tincidunt consequat metus, ac posuere urna facilisis eget.\r\n\r\nPellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In hac habitasse platea dictumst. Sed ac arcu ac elit blandit tincidunt nec sit amet purus. Ut vel ultrices nisi. Sed ac dapibus augue. Vivamus vestibulum tristique mi nec dictum. Praesent sagittis justo at dui cursus cursus. Sed ultrices, nulla a euismod scelerisque, tellus augue fermentum purus, nec efficitur elit felis vitae arcu. Sed vel orci et tellus consequat hendrerit id in libero. In at nisl nec justo finibus sagittis. Phasellus id fermentum mauris. Vivamus vitae vestibulum enim.\r\n\r\nQuisque malesuada, nunc vel imperdiet vulputate, velit quam consectetur dui, id suscipit sem orci id tortor. Vestibulum bibendum arcu vitae neque ultricies, eu tempus odio volutpat. Suspendisse nec eros eu felis dapibus malesuada nec eu justo. Duis sit amet libero at purus aliquam auctor non ac augue. Ut in tincidunt arcu, id condimentum libero. Maecenas id magna purus. Pellentesque non justo vitae libero fringilla ultricies. Sed gravida, justo ut iaculis lacinia, velit nisl sollicitudin odio, eu tempus est lacus id enim. Suspendisse potenti.\r\n\r\nFusce aliquam euismod felis, in laoreet odio facilisis non. Proin hendrerit lacus non velit fringilla feugiat. Maecenas facilisis augue ut ullamcorper iaculis. Aliquam vel felis in urna bibendum suscipit a ac enim. Duis ut turpis sit amet justo ullamcorper pellentesque. Nulla facilisi. Nunc laoreet risus id massa feugiat, vel malesuada nulla tristique. Integer vitae tortor vel lacus sollicitudin pellentesque in ut est.",
                        "publish": "2023-12-11T07:57:59Z",
                        "status": "PB",
                        "image": "http://localhost:8000/media/post_5f072b72-f7fa-4420-be7c-500d2e9d4754/dgfs.png"
                    }