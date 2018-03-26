#!/usr/bin/env python
import os
import jinja2
import webapp2
import gc
import random


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

class Country:
    def __init__(self, name, capital, capital_img_url):
        self.name = name
        self.capital = capital
        self.capital_img_url = capital_img_url

countries_list = []

Spain = Country("Spain", "Madrid", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Gran_V%C3%ADa_%28Madrid%29_1.jpg/1024px-Gran_V%C3%ADa_%28Madrid%29_1.jpg")
Italy = Country("Italy", "Rome", "https://upload.wikimedia.org/wikipedia/commons/c/c0/Rome_Montage_2017.png")
Portugal = Country("Portugal", "Lisbon", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Poster_Lisbon.jpg/800px-Poster_Lisbon.jpg")
France = Country("France", "Paris", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Seine_and_Eiffel_Tower_from_Tour_Saint_Jacques_2013-08.JPG/800px-Seine_and_Eiffel_Tower_from_Tour_Saint_Jacques_2013-08.JPG")
Germany = Country("Germany", "Berlin", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Brandenburger_Tor_Nachts.JPG/1024px-Brandenburger_Tor_Nachts.JPG")
Austria = Country("Austria", "Vienna", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Schloss_Sch%C3%B6nbrunn_Wien_2014_%28Zuschnitt_1%29.jpg/1920px-Schloss_Sch%C3%B6nbrunn_Wien_2014_%28Zuschnitt_1%29.jpg")
Denmark = Country("Denmark","Copenhagen", "https://upload.wikimedia.org/wikipedia/commons/6/68/Copenhagen_Collage2.jpg")
Finland = Country("Finland", "Helsinki", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Helsinki_montage_2015.jpg/800px-Helsinki_montage_2015.jpg")
Norway = Country("Norway", "Oslo", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/NO-oslo-akershus-blick-von-schiff.jpg/1024px-NO-oslo-akershus-blick-von-schiff.jpg")
Sweden = Country("Sweden", "Stockholm", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Stockholm.jpg/800px-Stockholm.jpg")
Switzerland = Country("Switzerland", "Bern", "https://upload.wikimedia.org/wikipedia/commons/f/fe/Bern_2.jpg")
Poland = Country("Poland", "Warsaw", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Pa%C5%82ac_Na_Wyspie_w_Warszawie%2C_widok_na_elewacj%C4%99_po%C5%82udniow%C4%85.jpg/1024px-Pa%C5%82ac_Na_Wyspie_w_Warszawie%2C_widok_na_elewacj%C4%99_po%C5%82udniow%C4%85.jpg")
Hungary = Country("Hungary", "Budapest", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Views_from_Fisherman%27s_Bastion_toward_south._-_Budapest%2C_Hungary._-_62_365%C2%B2_Observador_%288262965486%29.jpg/1024px-Views_from_Fisherman%27s_Bastion_toward_south._-_Budapest%2C_Hungary._-_62_365%C2%B2_Observador_%288262965486%29.jpg")
Czech_Republic = Country("Czech Republic", "Prague", "https://upload.wikimedia.org/wikipedia/commons/f/fb/Prague_Collage_2017.png")
Monaco = Country("Monaco", "Monaco", "https://upload.wikimedia.org/wikipedia/commons/2/2f/Monaco_Monte_Carlo_1.jpg")
Liechtenstein = Country("Liechtenstein", "Vaduz", "https://upload.wikimedia.org/wikipedia/commons/8/8e/Vaduz1.png")

for obj in gc.get_objects():
    if isinstance(obj, Country):
        countries_list.append(obj)

def findCountryByName(name):
    for obj in countries_list:
        if obj.name == name:
            return obj
    return None

class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        global countries_list
        country = random.choice(countries_list)
        if self.request.get("change_country") == True:
            country = random.choice(countries_list)
            print country

        url = country.capital_img_url
        country_name = country.name
        correct = False
        params = { 'url': url, 'correct': correct, 'country': country_name }
        return self.render_template("index.html", params)

    def post(self):
        country = findCountryByName(self.request.get("country"))
        capital = country.capital.lower()

        if capital == self.request.get("answer").lower():
            text = "You are right! The capital is " + country.capital
            correct = True
        else:
            text = "You are wrong! Try again!"
            correct = False

        params = { 'capital': capital, 'text': text, 'country': country.name, 'correct': correct }
        return self.render_template("index.html", params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
