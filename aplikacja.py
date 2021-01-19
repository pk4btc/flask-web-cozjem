from flask import Flask, render_template
from contentfromweb import content_foods,content_breakfast
from pymongo import MongoClient
import json








def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://qweqweqwe123:qweqweqwe123@cozjem.rpgvf.mongodb.net/test")
    app.db = client.cozjem

    @app.route('/')
    def index():
            return render_template('index.html')

    @app.route('/sniadanie')
    def sniadanie():


        # sniadanie= content_breakfast.tabSniadanie['sniadanie'][1]
        # sniadanieImg= content_breakfast.tabSniadanieImg['sniadanieImg'][1]

        lista =[e for e in app.db.sniadanie.find({})]
        x1=lista[0]['sniadanie'][1]
        z2=lista[1]['sniadanieImg'][1]

        return render_template('sniadanie.html',sniadanieHtml=x1,sniadanieImgHtml=z2)


    @app.route('/obiadek')
    def obiadek():

        lista =[e for e in app.db.obiad.find({})]
        x=lista[0]['obiadek'][1]
        z=lista[1]['obiadekImg'][1]

        return render_template('obiadek.html',obrazy=z,nazwa=x)

    @app.route('/kolacja')
    def kolacja():
        lista =[e for e in app.db.kolacja.find({})]
        kolacja=lista[0]['kolacja'][1]
        kolacjaImg=lista[1]['kolacjaImg'][1]

        return render_template('kolacja.html',kolacja=kolacja,kolacjaImg=kolacjaImg)




    # obiadki = content_foods.tabObiadek
    # obrazki = content_foods.tabObiadekImg

    class KolacjaKlasa:
        def __init__(self,a,b,c,d):
            self.aa=a
            self.bb=b
            self.cc=c
            self.dd=d


    return app

content_breakfast()