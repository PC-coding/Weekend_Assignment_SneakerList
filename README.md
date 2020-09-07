# Weekend_Assignment_SneakerList
Create the following in a NEW Github repository, adding me (username greg-smith1) as a collaborator.

Sneaker Seller
In modern times, the third-party sneaker market has exploded- as of summer 2019, the global retail sneaker market was worth about $58 billion. This has led to a secondary market where consumers exchange limited-release or limited-edition sneakers in a peer-to-peer manner, using sites like StockX to create a multi-billion dollar resale industry.

To capitalize on that market, we're going to start building an application (called Sneaker Seller, until we can find some PR people who will work for free) to allow users to post sneakers they'd like to sell.

We will need to create:

A sqlite3 database that will store data about listed sneakers, including:
Sneaker name
Year released
Version number
Sports personality or style icon that created it (or empty string if it doesn't exist)
Original price
Current price (listing price on our app)
Company that manufactures it (e.g. Nike, Adidas)
Contact phone number
Contact email
Once the database exists, we will need Python object-oriented models and a Flask RESTful backend that will allow us to:
Add a new sneaker
Update a sneaker
Delete a sneaker listing
View all sneakers listed by a given person (think how you might identify the person)
View sneakers below a given price
View sneakers by company
Bonus: View sneakers that are sold at 50% or less of their original sale value
Once this all works, make an additional class and table to represent a User, each User being a person who will be adding items to our app. You don't need to worry about any Flask functionality for now, but having the class lets us integrate it i the future.
