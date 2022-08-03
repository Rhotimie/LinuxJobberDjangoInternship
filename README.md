Django Tutorials for Beginners
================================

Look into the websites for tips on how to setup a django project

--http://realdjango.herokuapp.com/

                               Setting up of Django projects from the command window
                               =====================================================
--pip install django
--pip install virtualenv
--django-admin startproject Linuxjobber                     (This is used to create a django project)
Navigate inside the folder created and run the following command below
--virtualenv venv              (run this to set up a virtual environment)
--cd env
--cd scripts
--activate
To deactivate use
--deactivate
while the virtual environment is still activated
--pip install django
--pip install mysqlclient
--pip install psycopg2
--python manage.py migrate
--python manage.py createsuperuser
-- python manage.py runserver
-- python manage.py runserver 8000              (use this to change from default port 8000)

                                           EXPLAINING EACH FILES IN A PROJECT
                                           ==================================
1. __init__.py
    The _init_py file tells the python interpreter that the project directory should be considered as a python package
2. settings.py
    settings.py contains the configuration settings for your project
3. urls.py
    urls.py handles url declarations for your website. You can see it as a table of contents for your site.
4. wsgi.py
    wsgi.py serves as an entry point for wsgi applications.
    It stands for web server gateway interface
    Wsgi is a specification that describes how web servers communicate with web applications.
5. manage.py
    manage.py allows you run certain commands such as one to start a new application,
    perform a database migration or run the the lightweight django server to run your project

An Application is not the same thing as a project. An application performs a particular function while
a project is a collection of all the configurations and applications for a particular website

                                            EXPLAINING EACH FILES IN AN APP
                                            ===============================
1. admin.py
    admin.py which handles the administrative tasks of your app
2. apps.py
    apps.py essentially contains the settings and configurations for your application
3. models.py
    models.py is where your Apps database information and meta data will be described
4. tests.py
    test.py is where you can write test code that automatically tests your application to see if everything works fine
5. views.py
    views.py is where the logic of you application can be specified.
    It is just a design of the information displayed on the website, displays how data handled by the model looks
App is a web application that does specific functions
Projects is a collection of apps and configuration for a website

                                                   Version control
                                                   ===============
--git init
--touch .gitignore
--Add the following into it
        .Python
        env
        bin
        lib
        include
        .DS_Store
        .pyc
--git add .
--git commit -m "initial commit"
--pip install setuptools --upgrade

                                                  DJANGO VERSION
                                                  ==============
--import django
--django.get_version()

                                        SQLITE(DEFAULT DJANGO DATABASE SYSTEM)
                                        ======================================
This is the default database that comes with python django
--python manage.py migrate             (This is used to synchronize your code with the database)

                                                    MySQL
                                                    =====
--pip install mysqlclient
Create another console
--mysqld                                                (helps to start sql)
--mysql -u root
--show databases;
--CREATE DATABASE django_db;
--USE django_db;
--SHOW tables;
--quit


                                                    Database settings
                                                    =================
--pip install mysqlclient                                (if you are using mysql)
--pip install psycopg2                                   (if you are using postgresql)
--DO you database configuration
--python manage.py migrate                               (after activating the virtual environment)


                                    while inside the project directory
                                    =================================

--python manage.py runserver                                        (after activating the virtual environment)
----pip freeze > requirements.txt       (it is used to create a record of the installed libraries:)

                                                       SOUTH
                                                       =====

South is used for managing changes to your database tables. As your application grows, and you need to add a field to
a specific table, for example, you can simply make changes to the database via data migrations with South.
It makes life so much easier.

Install South and then commit your new changes to git.
--pip install south

Update the INSTALLED_APPS in your settings.py file with:
 'south',

                                                 CREATING DJANGO SUPERUSER
                                                 =========================
Admin interface is essentially to control the content of the website or database
--python manage.py createsuperuser
For you to access your Article models from your admin, set up ur admin.py
Use the url below to navigate to the superuser page
--http://127.0.0.1:8000/admin/

                                         How to create a superuser in MySQL?
                                         ===================================
1. First, you have to log in with the root user, which has the CREATE USER privilege
    --CREATE USER 'rhotimie'@'localhost' IDENTIFIED BY 'abraham';
2. Make it a superuser
    --GRANT ALL PRIVILEGES ON *.* TO 'rhotimie'@'localhost' WITH GRANT OPTION;
    --FLUSH PRIVILEGES;
3. To GRANT ALL privileges to a user, allowing that user full control over a specific database, use the syntax below:
    --GRANT ALL PRIVILEGES ON django_db.* TO 'rhotimie'@'localhost';
    --FLUSH PRIVILEGES;
4. To view all users in the MySQL database server, you use the following SELECT statement:
    --SELECT user, host FROM mysql.user;
5. To delete a specific user, type the following command from the mysql
    --DELETE FROM mysql.user WHERE user = 'rhotimie';
    --FLUSH PRIVILEGES;
6. How to show user's privileges in MySQL?
    --SHOW GRANTS FOR 'admin'@'localhost';


                                         How to create a superuser in Django?
                                         ====================================
1. Note: Django provides an admin interface that you can use to manage your applications for example managing the
   database and making desired changes to the application. This interface can be accessed through 127.0.0.1:8000/admin
   Only a superuser is allowed access to this interface. A superuser account has all privileges granted to it.
   A superuser account can be created with the command `python manage.py create superuser`
   --python manage.py createsuperuser

                                        Making your Django Apps reusable for other Projects
                                        ===================================================
1. In order to package your application for use in other projects, you need a tool called setuptools to do this for you
    --pip install setuptools
    --pip install setuptools --upgrade
2. Naming your Package
    Note: Copying your application folder into a new folder which is different from your project folder can help you
    prevent naming conflict between other modules. It is good practice to append `django-` to the name of the folder
    you intend copying the application you wish to package to, as this makes it easy for other developers to identify
    your module as django specific.
3. Usually other people that may want to use your application in their project will need a sort of guide on how to
    get your application to work in their project.
    Note: A README.rst file is traditionally used here to give a description of what your application does and steps
    intending users need to follow to successfully integrate your application within their project
4. To use the setuptools you will need to configure it and this configuration is usually implemented in a
   setup.py file.
   Note: The setup.py file basically manipulates files within your operating system by changing or finding directories
    and specifies information about your application.
5. Code released publicly without a license is useless. License determines who is able to use your code but
    understanding how to create a License is beyond the scope of this tutorial.
6. Building your package
    Note: Running the command `python setup.py sdist` within django-yourusernamescrumy in your command line terminal
    will create a directory called dist and build your new package into a tar.gzz file. You can also specify the
    format you want your package to be built to with the command `python setup.py sdist --format=zip`.
    --python setup.py sdist --format=zip


                                       Creating Django views
                                       =====================
1. Understanding django's most basic (function based view)
    Note: In Django, web pages and other contents are delivered by views. A view is basically a python function which
    is usually defined in the views.py file. It takes a request and sends back an HTTP response. The response sent by
    a view can be rendered on a template. For example, in a web application you might have a ‘Contactpage view’
    which may display your contact details on a page or a ‘Homepage view’ which may display your sites homepage.

                                       Working with Django Models
                                       ==========================
1. A model is the single definitive source of information about your data. It contains the essential fields and
   behavior of the data you are storing.
   Generally each model represents a single database table and is specified as a python class usually written inside
   the models.py file. The model class specified is required to extend the models.model class which can be imported
   from django.db.

2. Each attribute of a model represents a database field. For example a model with attribute “name” will have a field
   called name on the database. Field properties are defined by assigning models.Field type with or without widgets
   to the field name. For example, Age=models.Integerfield (default=18) will create a table field named Age and format
   the field to accept integers with 18 as the default value If no value is set.

3. In an earlier lab you gained knowledge about a superuser and created a superuser.
   Django has a predefined model called User which can be imported into your project from django.contrib.auth.models.
   this user has some primary attribute such as username, password, e-mail, first_name and last name. Instead of going
   through the stress of creating a custom user model for our project, we can use the predefined user model.
   But in a real world project it is recommended to use a custom user model.
   --from django.contrib.auth.models import User
4. Relationship such as one-to-one,one-to-many and many-to-many can exist between objects in different tables,this
   relationship can be established using foreign keys.
   When a record is added to a table, django automatically adds an ID field to the table and this field is
   automatically made a primary key. Relationships that exist between two tables are expressed with the use of foreign
   keys which is basically just a primary key from another table.
   When defining a foreign key field, the on_delete value specifies what action to be taken on a child table if an
   attempt is made to delete data from a parent table.
   Setting on_delete = model.CASCADE deletes data from a child table when data is deleted from the parent table.
   On_delete=models.PROTECT will prevent data from being deleted. Another argument that can be passed to a
   foreign key field is a related_name argument. This argument specifies the name of the reverse relationship that
   exists between a model and the model with the foreign key definition.
   This argument is really important when multiple applications in a project share a common relationship with another
    model, django uses this name to uniquely identify the reverse relationship between the models. The value “+” is
    used when you don't need an existence of a reverse relationship.

                                            Working with Django Models
                                            ==========================
1. Using django templates.
   Note :
   A template is simply a text file. It can generate any text-based format such as HTML, XML, CSV etc.
   A template can contain variables, which get replaced with values when the template is evaluated, and tags which
   control logics in the template.
   Django usually locates a template by searching through the path templates/nameofapplication/.
   Hence your applications templates should lie in that path so django can easily locate them.

2. How you can use a template in a view.
   Note :
   When working with templates, the render function plays significant role. It combines a given template with a given
   context dictionary and returns an HttpResponse object with that rendered text. request and the name of the template
   are required arguments to be passed to this function.
   A context is an optional argument, which is simply a dictionary of values to add to the templates context.
   By default, this is an empty dictionary. If a value in the dictionary is callable, the view will call it just before
   rendering the template.

3. Working with template tags.
   Note :
   In HTML, you can’t really write Python code, because browsers don’t understand it. They know only HTML. HTML is
   static while python is much more dynamic. Django template tags allow us to transfer python-like things into HTML,
   so you can build dynamic websites faster.
   Different template tags exists for different purpose for example there are tags for specifying conditional
   operations, for specifying variables, to load files etc.
   The values of the dictionary variable you passed as a context to the render function for rendering on the home.html
   template can be evaluated within the template. When the template engine encounters a variable, it evaluates that
   variable and replaces it with the result. Variables are represented like this {{ variable }} in templates. If you
   use a variable that doesn’t exist, the template system will insert the value of the TEMPLATE_STRING_IF_INVALID
   setting, which is set to empty by default.

                                                Set up your Django app
                                                ======================
Create an app which is used to separate concerns or functionality in a project:
--python manage.py startapp simple
--pip install django-markdown
--pip freeze > requirements.txt

Update the INSTALLED_APPS in your settings.py file with:
 'simple',
 'django_markdown',

CREATE a templates folder inside the project directory add to TEMPLATES > DIR, like blow
'DIRS': ['/c/Users/Rotimi/PycharmProjects/Linuxjobber/templates'],


Open models.py that is inside simple and add your models
Proceed to make migrations from the console with
--python manage.py makemigrations
--python manage.py migrate                                           (This will migrate the table to the database)

                                                     Views and URLs
                                                     ==============
We will be following the Model-View-Controller (MVC) architecture structure. Django projects are logically
organized around this architecture. However, Django's architecture is slightly different in that the views act
as the controllers. So, projects are actually organized in a Model-Template-Views architecture
(MTV). Yes, this is confusing.

                                                        Views
                                                        =====
Add the following code to the views.py file:

from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('index.html')
This function takes a parameter, request, which is an object that has information about the user requesting the
page from the browser. The function's response is to simply render the index.html template.

                                                        URLs
                                                        ====
Next, we need to add a new pattern to the urls.py file:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('$', 'simple.views.index')
]

                                                      Templates
                                                      =========
Finally, we need to create the "index.html" template. Create a new file called index.html within the templates
directory, and add the code found here.

Fire up the server. How does that look? Let's add some styles.

Replace the previous code with code here.

Better?