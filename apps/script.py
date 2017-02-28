from flask import current_app

from flask_script import Command
from flask_security.confirmable import confirm_user

from apps.models import FlaskDocument



class ResetDB(Command):
    """Drop all tables and recreate them """
    def run(self,**kwargs):
        self.drop_collections()

    @staticmethod
    def drop_collections():
        for klass in FlaskDocument.all_subclasses():
            klass.drop_collection()


class PopulateDB(Command):
    """ Fills in predefined data to DB """
    def run(self,**kwargs):
        self.create_roles()
        self.create_users()


    @staticmethod
    def create_roles():
        for role in ('admin','editor','author'):
            current_app.user_datastore.create_role(name=role,description=role)
        current_app.user_datastore.commid()


    @staticmethod
    def create_users():
        for u in (('Rose','rose@friends.com','rose',['admin'],True),
                ('Joe','joe@friends.com','joe',['editor'],True),
                ('Chandle','chandle@friends.com','chandle',['author'],True),
                ('Monica','monica@friends.com','monica',[],False),
                ('Rich','rich@friends.com','rich',['Guest'],False),
                ('Pheb','pheb@friends.com','pheb',['editor'],True)):
            user = current_app.user_datastore.create_user(
                    username=u[0],
                    email=u[1],
                    password=u[2],
                    roles=u[3],
                    active=u[4]
                    )
            confirm_user(user)

            current_app.user_datastore.commit()
