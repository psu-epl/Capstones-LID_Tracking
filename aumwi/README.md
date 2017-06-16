Awesome Usage Monitor Web Interface

* ./templates/ - Application specific html templates
* ./__init__.py - Python file to designate the directory as an importable package. May be empty or contain package initialization instructions.
* ./admin.py - Application override functions for Django model administration
* ./apps.py - Application configuration class definitions and settings
* ./forms.py - Model form definitions
* ./managers.py - Application override classes for model "managers". Django managers perform admin functions on the database models. 
* ./models.py - Application definitions for database models.
* ./test.py - Application specific testing definitions. None currently. 
* ./urls.py - Appliation specific url patterns for resolving http requests. Associates a url pattern with a function to be run by the application.
* ./views.py - Application specific class and function definitions. A "view" defines the backend rendering and processing logic for a url
