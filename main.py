from database import db,User, Announcement

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

#List all user table
list_users = User.select()
for u in list_users:
    print(u.id)


#Get user from ID
user1 = User.get(User.id == 1)
print (f"get user: {user1.name}")


#Update user
user2 = User.get(User.id == 2)
old_name = user2.name
user2.name = "Marco"
user2.save()
print (f"Update name user - old name {old_name}, new name: {user2.name}")


#Delete user
print("Delete user id 3")
user3 = User.get(User.id == 3)
user3.delete_instance()

try:
    User.get(User.id == 3)
except:
    print('user deleted')


#Show all announcement from user@zicstardust.com
announcement_zic = Announcement.select().join(User).where(User.email == "user@zicstardust.com")
for a in announcement_zic:
    print("-", a.id, a.title, a.description, a.value)


#Delete all announcements table
Announcement.delete().execute()
