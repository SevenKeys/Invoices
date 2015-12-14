#Wysely

Wysely is an web application to manage, create and send invoices for companies and freelancers, making much easier this process and with a very practical UI to generate invoices easily.

Wysely is developed with django 1.8 and python 3.4.

##Overview
This project includes the following:
* Basic user login, registration, and forgot password screens & logic.
* A general 500 error page and 404 page are wired up.  The 404 page can easily be customized to include suggested pages.
* A basic admin area, to help directory/file naming conventions for scripts & stylesheets for areas.

##Git Standards
* Branch for storyWMVP-19 should be called WMVP-19
* Merge branches commit comment:
* Merge $branch_1 -> $branch_2 (edited)
* Merge heads commit comment: merged heads $branch_name
* Branches commit comment: $branch_name implemented; description
* i.e.

  git commit -m "refs WMVP-19, implemented;  some description of the story and what was done in the commit"

  or

  git commit -m "refs WMVP-19, fixes;  some description of the story and what was done in the commit"

  and so on

##How to make it run in your local machine:
* Install python3.4 and pip
* Download and install Git and any source control app you like and download the code
* Download and install any application to edit the files (We are using PyCharm)
* Download and install Node.js
* Download and install PostgreSQL
* Create database 'wysely'
* Run 'npm install'
* Run 'npm install -g bower'
* Run 'bower install'
* Run 'pip install -r requirements.txt'
* Start the application with 'python manage.py runserver' under the root project

