from flask import Flask, render_template, redirect 
from flask_pymongo import pymongo
import scrape_mars

# scrape_mars_cerberus, scrape_mars_shiaparelli, scrape_mars_syrtris, scrape_mars_valles_marineris
app = Flask(__name__)

# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

conn = "mongodb://localhost:27017/mars_data"
client =  pymongo.MongoClient(conn)

mars_doc= scrape_mars.scrape()
mars_data = client.mars_data
mars_data.mission_to_mars.drop()
mars_data.mission_to_mars.insert_one(mars_doc)

@app.route("/")
def index():
    mars_doc = client.mars_data.mission_to_mars.find_one()
    return render_template("index.html", mars_data = mars_doc)

@app.route("/scrape")
def mars_scrape():
    mars_doc = scrape_mars.scrape()
    mars_data = client.mars_data
    mars_data.mission_to_mars.drop()
    mars_data.mission_to_mars.insert_one(mars_doc)


    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)