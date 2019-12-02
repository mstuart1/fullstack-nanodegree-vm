import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base() # instance of function

#### class names are camel case, table names are lowercase with underscores


#### Class code
# create the python classes that we want to be tables in our database

class Restaurant(Base):
### table definition
	__tablename__ = 'restaurant'

	id = Column(Integer, primary_key = True)

	name = Column(String(250), nullable = False)

	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
		'name': self.name,
		'id': self.id,
		}


class MenuItem(Base):
	__tablename__ = 'menu_item'

### mapper code - creates columns
	name = Column(String(80), nullable = False)

	id = Column(Integer, primary_key = True)

	course = Column(String(250))

	description = Column(String(250))

	price = Column(String(8))

	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

	restaurant = relationship(Restaurant)

# decorator to send JSON objects in a serializable format
	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
		'name': self.name,
		'description': self.description,
		'id': self.id,
		'price': self.price,
		'course': self.course,
		}

### begin footer

engine = create_engine('sqlite:///restaurantmenu.db') # creates new file

Base.metadata.create_all(engine) # adds classes we will create as new tables in database

