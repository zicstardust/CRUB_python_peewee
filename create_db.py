from database import db,User, Announcement

#Create Database
db.connect()
db.create_tables([User,Announcement])

#Insert users
User.create(
    name="Zic",
    email="user@zicstardust.com",
    password="pass123"
)

User.create(
    name="Mario",
    email="mario@zicstardust.com",
    password="easypass"
)

User.create(
    name="John",
    email="john@zicstardust.com",
    password="anotherpass"
)


#Insert announcements

Announcement.create(
    user = User.get(User.email == 'user@zicstardust.com'),
    title = "Item Title",
    description = "This is a item",
    value = 500.0
)

Announcement.create(
    user = User.get(User.id == 1),
    title = "Item Title 2",
    description = "This is a item 2",
    value = 300.0
)

Announcement.create(
    user = User.get(User.email == 'mario@zicstardust.com'),
    title = "Item Title 3",
    description = "This is a item 3",
    value = 400.0
)

Announcement.create(
    user = User.get(User.email == 'john@zicstardust.com'),
    title = "Item Title 4",
    description = "This is a item 4",
    value = 600.0
)