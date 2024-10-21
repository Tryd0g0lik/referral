"""This is a description for the status of user_login """
from referral.models import Session, Users

session = Session()

class UserLogin:
    """
    This a class make the present of single user after
    the event authorization.
    """
    def __init__(self):
        self.__user = None
        # self.__user = user.__dict__
    def create(self, user):
        """
        :param user: object
        :return: user's object from db
        """
        self.__user = user.__dict__
        return self
    
    def is_authenticated(self):
        """Here is a property of Authenticate"""
        # self.is_authenticated = True
        return True
    
    def is_active(self):
        """Here is change an user's status. """
        # self.is_active = True
        return True
    
    def is_anonymous(self):
        # self.is_anonymous = False
        return False
    
    def get_id(self):
        # return str(self.__user.pk)
        # ind = str(self.__user["id"])
        ind = self.__user["id"]
        return ind
    def get_token(self):
        return self.__user["activation_token"]
    
    def get_firstname(self):
        return self.__user['firstname']
    
    
    
    def fromDB(self, user_id: str):
        try:
            # users = Users()
            # self.__user = users.query\
            sess = Session()
            self.__user = sess.query(Users).filter_by(
                pk=int(user_id)
            ).first()
            sess.close()
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
            user = self.__user
            return user
    
    
        
    
    