from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
from scrape_mars import scrape_mars_news, scrape_mars_featured, scrape_mars_weather, scrape_mars_facts, scrape_mars_hem as scrape
import os


app = Flask(__name__)


mongo = PyMongo(app, URI="mongodb://localhost:27017")


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape.scrape()
    mars.update(
        {}, mars_data, upsert=True
    )
    # mars_db.update({}, scrape_mars.scrape_mars_featured(), upsert=True)
    # mars_db.update({}, scrape_mars.scrape_mars_weather(), upsert=True)
    # mars_db.update({}, scrape_mars.scrape_mars_facts(), upsert=True)
    # mars_db.update({}, scrape_mars.scrape_mars_hem(), upsert=True)

    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)