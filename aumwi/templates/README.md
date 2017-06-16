Awesome Usage Monitor Web Interface HTTP Templates
------

* ./site_template.html - Top level render instructions for the User Interface of the AUM webframework
* ./index.html - Required html page. This page should not be hit under normal UI usage.
* ./Error.html - Required html page. This page should not be hit under normal UI usage.

---
###### All other files specify the render instructions for a specific User Interface page.  They are templatized and refer to site_template.html for the majority of their render instructions.  Django renders the html using context from views.py

* ./Add*.html - Adds an entry to the specific database table.
* ./Del*.html - Asks to confirm the deletion of the specified station or user.
* ./Del*Conf.html - Confirms the station or user was deleted.
* ./Edit*.html - Edits an entry from the specified database table.
* ./Find*.html - Searches for the station or user from the supplied information.
* ./Find*List.html - Displays the results of the search in a list format.
* ./Find*Result.html - Displays the result of the search in a table format.
* ./ReportsBase.html - Top level report generation configuration page.
* ./RptUseBy*.html - Displays the result of the report generation based on the configuration parameters. 

---
###### Functionality not implemented in the User Interface
* ./DatabaseAdmin.html - Allows for database configuration and administration from the UI.
* ./DatabaseBackup.html - Sends a copy of the database to the specified local or remote directory.
* ./DatabaseRestore.html - Deletes the current database and restores a previous version from the specified local or remote directory.
