"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes


routes['default_controller'] = 'Users'
routes['POST']['/register'] = 'Users#register'
routes['POST']['/login'] = 'Users#login'
