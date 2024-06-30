from database import db,User, Announcement

#Create Database
db.connect()
db.create_tables([User,Announcement])
