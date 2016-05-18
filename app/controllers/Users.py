from system.core.controller import *
from time import strftime
import string, random, re
from system.core.model import Model
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        self.db = self._app.db

   
    def index(self):
        return self.load_view('index.html')

    def register(self):
        errors=0
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        email=request.form['email']
        user_name=request.form['user_name']
        password=request.form['password']
        confirm_password=request.form['confirm_password']
        if len(first_name) <2:
            errors+=1
            flash("Must enter a complete first name")
        if len(last_name) <2:
            errors+=1
            flash("Must enter a complete last name")
        if len(email) <1:
            errors+=1
            flash("email cannot be blank")
        if len(user_name) <1:
            errors+=1
            flash("user name cannot be blank")
        if len(password) <8:
            errors+=1
            flash("password must be at least 8 characters")
        if password != confirm_password:
            errors+=1
            flash("passwords do not match")
        if self.models['User'].check_email(email):
            errors+=1
            flash("this email is already registered")
        if not EMAIL_REGEX.match(request.form['email']):
            errors += 1
            flash("Invalid Email Address!")
        if errors:
            return redirect("/")
        data={
            'first_name':first_name,
            'last_name':last_name,
            'email':email,
            'user_name':user_name,
            'password':password
        }
        register=self.models['User'].register(data)
        session['user_id']=register
        return redirect("/dash")

    def login(self):
        info={
            'email':request.form['email'],
            'password':request.form['password']
        }
        check_user=self.models['User'].login(info)
        if check_user:
            return redirect('/dash')
        flash("email or password did not match our records")
        return self.load_view('/')

    