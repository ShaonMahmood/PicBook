PicBook Documentation
=====================
Welcome to Picbook. PicBook is a simple photo uploading website where users can upload, delete and view photos of other users.

Project Development requirements
--------------------------------
#) A linux machine, For example: Ubuntu 16.04 or 18.04 LTS

#) Python 3.5 or above, Linux distributions have it already

#) PostgreSQL setup, Follow Link: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04

#) Redis server setup, Follow Link: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis

#) Install git, Follow Link: https://www.liquidweb.com/kb/install-git-ubuntu-16-04-lts/

#) Setup a Virtual environment, Instructions: https://linoxide.com/linux-how-to/setup-python-virtual-environment-ubuntu/

#) Setup ngrok, Follow Instruction: https://ngrok.com/download

Project SetUp
-------------
* Clone the project directory to your local machine using git clone command::

    git clone https://github.com/ShaonMahmood/PicBook.git
* Create a virtual environment::

    python3 -m venv picbook_env
    source picbook_env/bin/activate
* Install requirements::

    cd <your_cloned directory>/
    pip install -r requirements/local.txt
* Create a local_settings.py file inside your picbook directory::

    touch picbook/local_settings.py
* A typical local_settings.py may contains the following settings::

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    THUMBNAIL_DEBUG = True
    DEBUG = True
    DATABASE = {}
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'your_account@gmail.com'
    EMAIL_HOST_PASSWORD = 'your_password'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
* Migrate all the database files using migrate command::

    python manage.py migrate
* Run the project::

    python manage.py runserver 8000

Project specific task
---------------------
A User can bookmark an image or can upload it locally. while uploading through
bookmarklet some modifications should be done in local development,such as:

* Run ngrok at the port 8000 keeping the project running::

    ./ngrok http 8000
* copy the https address and replace it with following lines::

    src = "<https://592f3f52.ngrok.io>" # in templates/bookmarklet_launcher.js
    site_url = '<https://592f3f52.ngrok.io/>' # in static/images/js/bookmarklet.js
* visit the running project with that https address,for example::

    https://592f3f52.ngrok.io/user-account
