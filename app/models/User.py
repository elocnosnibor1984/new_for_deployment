
from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def check_email(self, email):
        query = "SELECT * from users where email = :email"
        data = {'email': email}
        return self.db.query_db(query, data)

    def register(self, info):
        password=info['password']
        password_hash=self.bcrypt.generate_password_hash(password)
        query = "INSERT into users (first_name, last_name, email, user_name, password, created_at, updated_at) Values (:first_name, :last_name, :email, :user_name, :password, NOW(), NOW())"
        data = {'first_name': info['first_name'], 'last_name':info['last_name'], 'email':info['email'], 'user_name':info['user_name'], 'password':password_hash}
        self.db.query_db(query, data)

    def login(self, data):
        print data
        password=data['password']
        query = "SELECT * from users where email = :email"
        data = {'email': data['email']}

        check_email=self.db.query_db(query,data)
        print check_email
        if check_email:
            check_password_hash = self.bcrypt.check_password_hash(check_email[0]['password'], password)
            if check_password_hash:
                return True
        return False
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """