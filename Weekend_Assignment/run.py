from flask_routes.routes import app
from models.listing import SneakerListing

SneakerListing.dbpath = "data/listings.db"

app.run()