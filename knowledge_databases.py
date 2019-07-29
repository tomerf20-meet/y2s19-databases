from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(site_url, rating, topic, title):
	new_article=Knowledge(site_url=site_url, rating=rating, topic=topic, title=title)
	session.add(new_article)
	session.commit()
#add_article("https://en.wikipedia.org/wiki/Food", 7, "food", "food")
#add_article("https://en.wikipedia.org/wiki/Animal", 7, "animal", "animal")
#add_article("https://en.wikipedia.org/wiki/Sport", 7, "sport", "sport")

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles
all_articles = query_all_articles()
# print(all_articles)
def query_article_by_topic(food):
	food_article = session.query(Knowledge).filter_by(
       topic=food).first()
	return food_article
query_food = query_article_by_topic("food")
print(query_food)

def delete_article_by_topic(sport):
	session.query(Knowledge).filter_by(topic=sport).delete()
	session.commit()
delete_sport = delete_article_by_topic("sport")
print (all_articles)

def delete_all_articles():
	pass

def edit_article_rating():
	pass
