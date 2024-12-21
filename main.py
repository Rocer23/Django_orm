import django_setup
from django_orm.models import Role, Admin, User

role_admin = Role(short_role='a', full_role="admin").save()
role_user = Role(short_role='u', full_role='user').save()

admin = Admin(name='Admin', email='admin@gmail.com', role=Role(id='1')).save()
user1 = User(name='user1', email='user1@gmail.com', role=Role(id='2')).save()

# def create_role():
#     role_admin = Role(role_name='a').save()
#     role_user = Role(role_name='u').save()
#     return role_admin, role_user
#
#
# def create_admin():
#     admin = Admin(name="Ivan", email='ivan@gmail.com', role='a')
#     admin.save()
#
#
# def create_user():
#     user = User(name='User1', email='example@gmail.com', role='u')
#     user.save()
