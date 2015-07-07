# adding components (autonomous views displayed in pages):

     component has it's own:

     .html - template
     .css
     .js
     .py - View class

     for a component named banana, this is to be added:
     1) template: components/banana.html

     2) styles: create new file under static/css/banana.css
        add style to the 'common_styles' in wysely/settings.py

     3) add js file, in which following template should be use for post load inits:

         wysely.component.banana = {
             initialize: function() {
                /// this function gets called on page load
             }
         }

         add the js file to the 'common_scripts' in wysely/settings.py

     4) create a file under wysely/common/components (i.e. banana.py)

         add content:
            from common.component import ViewComponent

            class BananaView(ViewComponent):
                ...

         be sure to inherit from ViewComponent, it will make things easier

     5) add alias to your component:
         # this is not necessary if you include views and don't reload them with ajax (?)
         edit wysely/urls.py, add your view:
            i) import your view class
            ii) add linking to url dict:
                 url(r'^bananaurl/', BananaView.as_view(), name='name of banana component')

 Adding a component to your page:
  https://djangosnippets.org/snippets/1568/
 {% view view_or_url arg[ arg2] k=v [k2=v2...] %}

 # dumping data from DB to fixture for reusing
    ./manage.py dumpdata --format=json > ./fixtures/initial_data.json

 # loading data from dumped DB
     ./manage.py loaddata fixtures/initial_data.json


