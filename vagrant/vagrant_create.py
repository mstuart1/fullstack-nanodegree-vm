from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# lets our program know what database we want to communicate with
engine = create_engine('sqlite:///restaurantmenu.db') 

# bind the engine to the base class, makes connections to tables
Base.metadata.bind = engine

# establishes link of communication between code executions and engine for CRUD
DBSession = sessionmaker(bind = engine)

# CRUD sends to the database on commit, DBSession is staging zone
session = DBSession()

# add new data
myFirstRestaurant = Restaurant(name = "Pizza Palace")
# adds to staging zone
session.add(myFirstRestaurant)
# commits to database
session.commit()

# check that it worked
session.query(Restaurant).all()

#add another item
cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzeralla", course = "Entree")