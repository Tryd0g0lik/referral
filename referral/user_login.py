"""This is a description for the status of user_login """
from referral.models import Session, Users

session = Session()

class UserLogin:
    """
    This a class make the present of single user after
    the event authorization.
    """
   
    def is_authenticated(self):
        """Here is a property of Authenticate"""
        self.is_authenticated = True
        return self
    
    def is_active(self):
        """Here is change an user's status. """
        self.is_active = True
        return self
    
    def is_anonymous(self):
        self.is_anonymous = False
        return self
    
    def get_id(self):
        return str(self.__user['id'])
    
    def create(self, user: object):
        """
        :param user: object
        :return: user's object from db
        """
        self.__user = user
        return self
    
    
    def fromDB(self, user_activation_token: str):
        try:
            self.__user = session.query(Users)\
                .filter_by(
                activation_token=user_activation_token
            ).first()
            if self.__user == None:
                """If we have a problem to the user's search then
                the user.id to install int('-1')
                """
                print("[UserLogin => fromDB]: None")
                self.id = -1
                
        except Exception as err:
            print(f"[UserLogin => fromDB]: Error => {err.__str__()}")
        finally:
            session.close()
            return self
    
    
        
    
    