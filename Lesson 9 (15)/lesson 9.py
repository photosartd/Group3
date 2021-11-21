class User:
    def __init__(self,
                 f_name,
                 l_name,
                 age,
                 height,
                 weight=70,
                 login_attempts=0,
                 ):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.height = height
        self.weight = weight
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f'Name: {self.f_name}')
        print(f'Surname: {self.l_name}')
        print(f'Age: {self.age}')
        print(f'Height: {self.height}')
        print(f'Weight: {self.weight}')
        print(f'Login: {self.login_attempts}')

    def greet_user(self, user2):
        print(f'Hi {user2.f_name}')

    def get_older(self):
        self.age += 1

    def increase_login_att(self):
        self.login_attempts += 1

    def reset_login_att(self):
        self.login_attempts = 0

    def show_login_att(self):
        print(self.login_attempts)

user1 = User(
    'Semev',
    'Birukov',
    15,
    172,
    65
)

user2 = User(
    'Fedor',
    'Smirnov',
    12,
    175
)

user1.show_login_att()
user1.increase_login_att()
user1.increase_login_att()
user1.increase_login_att()
user1.increase_login_att()
user1.show_login_att()


user2.show_login_att()
