from views import db
from models import Task
from datetime import date

# create the database and database table
# initialize databae scheme by calling this 
db.create_all()

# insert data
# insert some data using Task object from models.py
# db.session.add(Task("Finish this tutorial", date(13, 3, 2015), 10, 1))
# db.session.add(Task("Finish Real Python", date(14, 3, 2015), 10, 1))

# commit the changes
db.session.commit()