# Projecte Lliga Django -- Gestió Esportiva

Aquest projecte és una aplicació web desenvolupada amb Django 5.2 per a
la gestió d'equips de futbol i dels seus jugadors. Implementa una
arquitectura MTV (Model-Template-View) i utilitza una base de dades
relacional per administrar la informació de la lliga de manera eficient
i estructurada.

------------------------------------------------------------------------

## Descripció del projecte

L'aplicació permet gestionar equips i jugadors mitjançant una interfície
web pública i un panell d'administració segur. Està orientada a
l'aprenentatge i la pràctica del desenvolupament backend amb Django,
aplicant bones pràctiques d'organització del codi i separació de
responsabilitats.

------------------------------------------------------------------------

## Característiques principals

-   Gestió de dades relacionals mitjançant una relació `ForeignKey`
    entre els models Equip i Jugador.
-   Panell administratiu personalitzat amb funcionalitats CRUD completes
    (crear, llegir, actualitzar i eliminar).
-   Arquitectura MTV amb separació clara entre models, vistes i
    plantilles.
-   Entorn virtualitzat amb `venv` per garantir la portabilitat del
    projecte.
-   Integració amb sistema de control de versions mitjançant Git i
    GitHub.

------------------------------------------------------------------------

## Tecnologies utilitzades

-   Backend: Python 3.10 i Django 5.2\
-   Base de dades: SQLite3 (entorn de desenvolupament)\
-   Frontend: HTML5 i Django Template Language (DTL)\
-   Control de versions: Git i GitHub

------------------------------------------------------------------------

## Estructura del projecte

    projecte_liga/
    ├── config/             # Configuració central del projecte (settings, urls)
    ├── liga/               # Aplicació principal
    │   ├── migrations/     # Historial de migracions de la base de dades
    │   ├── models.py       # Definició dels models Equip i Jugador
    │   ├── views.py        # Lògica de les peticions HTTP
    │   ├── urls.py         # Sistema d’enrutament de l’aplicació
    │   └── templates/      # Plantilles HTML amb DTL
    ├── manage.py           # Eina de gestió de Django
    └── requirements.txt    # Dependències del projecte

------------------------------------------------------------------------

## Instal·lació i configuració

### 1. Clonar el repositori

    git clone https://github.com/yousseffouad12/projecte_liga.git
    cd projecte_liga

### 2. Crear i activar l'entorn virtual

    python3 -m venv env
    source env/bin/activate

En Windows:

    env\Scripts\activate

### 3. Instal·lar les dependències

    pip install -r requirements.txt

### 4. Aplicar les migracions i iniciar el servidor

    python3 manage.py migrate
    python3 manage.py runserver

Accedeix a l'aplicació des del navegador a:

    http://127.0.0.1:8000/

------------------------------------------------------------------------

## Funcionament

### Vista pública

Mostra el llistat dinàmic d'equips i els seus jugadors associats,
obtenint la informació directament de la base de dades.

### Panell d'administració

Interfície segura per a administradors que permet gestionar tots els
registres de la lliga de manera visual i eficient.

Per accedir-hi:

    http://127.0.0.1:8000/admin/

------------------------------------------------------------------------

## Autor

Youssef\
Desenvolupament i configuració\
GitHub: https://github.com/yousseffouad12
