import unittest
from kink import di
from bootstrap import Bootstrap
from domain.user.user_model_interface import IUserModel


class TestUserModel(unittest.TestCase):

    # def testGetUserBy(self):
    #     bootstrap = Bootstrap()
    #     user_model = di[IUserModel]
    #     user = user_model.getUserBy('username', 'username')
    #     print(user.username)

    # def testAddUser(self):
    #     bootstrap = Bootstrap()
    #     user_model = di[IUserModel]
    #     new_user = UserEntity()
    #     new_user.email = "eemsfgsaieel@gmail.com"
    #     new_user.password = "password"
    #     new_user.created_at = "3213256"
    #     new_user.slug = "eeeeemail"
    #     new_user.username = "eeeesdgfemail"
    #     new_user.access_token = "sfsfs321sfsq321sf321"
    #     user_model.addUser(new_user)

    def testListUser(self):
        bootstrap = Bootstrap()
        user_model = di[IUserModel]
        users = user_model.listUser()
        print(users[0].username)

    def testDeleteUser(self):
        bootstrap = Bootstrap()
        user_model = di[IUserModel]
        user_model.deleteUserBy('username', 'username3333')


if __name__ == "__main__":
    unittest.main()
