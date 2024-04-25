class UserEntity:
    id: int
    username: str
    email: str
    password: str
    created_at: str
    slug: str
    meta: dict

    @staticmethod
    def makeUser(user_data: tuple, user_metadata=None) -> "UserEntity":
        if user_metadata is None:
            user_metadata = {}
        user = UserEntity()
        user.id = user_data[0]
        user.username = user_data[1]
        user.created_at = user_data[2]
        user.password = user_data[3]
        user.email = user_data[4]
        user.slug = user_data[5]
        user.meta = user_metadata
        return user
