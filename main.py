from database import db,User, Announcement

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
