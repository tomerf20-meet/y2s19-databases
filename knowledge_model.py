from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = "information"
	site_url = Column(String, primary_key=True)
	rating = Column(Integer)
	topic = Column(String)
	title = Column(String)
	def __repr__(self):
		if self.rating>=7:
			return ("If you want to learn about: {}\n"
            	"Go to the wikipedia article called: {} \n"
            	"We gave this article a rating of: {} out of 10 \n"
				"You can visit the article here: {}").format(
                	 self.topic, self.title, self.rating, self.site_url)
		if self.rating<7:
			return ("If you want to learn about: {}\n"
            	"Go to the wikipedia article called: {} \n"
            	"We gave this article a rating of: {} out of 10 \n"
				"You can visit the article here: {} \n"
				"Unfortunately, this article does not have a better rating. Maybe this is an article that should be replaced soon!").format(
                	self.topic, self.title, self.rating, self.site_url)
# food=Knowledge(site_url="https://en.wikipedia.org/wiki/Food", rating=7, topic="food", title="food")
# print(food)
# animal=Knowledge(site_url="https://en.wikipedia.org/wiki/Animal", rating=6, topic="animals", title="animal")
# print(animal)
# sport=Knowledge(site_url="https://en.wikipedia.org/wiki/Sport", rating=9, topic="sports", title="sport")
# print(sport)

	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
