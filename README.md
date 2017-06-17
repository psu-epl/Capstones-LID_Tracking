Capstones-LID_Tracking
------

###### This is the top level directory for the Capstone Awesome Usage Monitor project. The following repo directories contain the files used by this project and the developers to specify, design, and implement the project. This directory may be copied whole into any preconfigured Django AUM project instance. See below on how to configure and setup an AUM project instance.

---

* ./SM/ - Files associated with the Station Module. Not used by Django.
* ./aum/ - Django associated python files for the aum project and used by all applications.
* ./aumwi/ - Django associated python files for the web interface application.
* ./static/ - css, js, img, and font files used by Django to render webpages, organized by project
* ./templates/registration/ - Django authentication and password management html files
* ./test/ - Testing software and associated coverage results zip
* ./manage.py - Django management code.

---

The development environment for the Awesome Usage Monitor used an Ubuntu 16.04 server instance with python3.0 installed and running as a virtual environment.  The server was configured with SMTP, a postgreSQL database, Gunicorn application server, and Nginx setup as the webserver and the reverse proxy to Gunicorn.  Django 1.11 was used to develope the project.

---

The test environment was created using pytest and pytest-django for python3, for detailed instructions on how to create additional tests or verify the functionality of your production instance of the Awesome Usage Monitor please visit this [Pytest-Django Tutorial](http://pytest-django.readthedocs.io/en/latest/tutorial.html)

---

For detailed instructions on how to create a production environment similar to the development environment please visit this [DigitalOcean Tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04).

---

For detailed documentation on any Django function used within the project, please refer to the [Django 1.11 Documentation](https://docs.djangoproject.com/en/1.11/) or the [Django source code](https://github.com/django/django), both of which are extensive and extremely helpful.
