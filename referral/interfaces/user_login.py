"""
This is a description of user_login.
"""

from referral.models import Session, Users

session = Session()


class UserLogin:
    """
    This a class/subclass make the present of single user after
    the event authorization. This is
    for  a LoginManager!!
    """
    
    def create(self, user):
        """
        This method is received user's object from entrypoint. After,
        transfer from the object to dict.
        After transfer data into a private variable (self)
        :param user: object
        :return: self
        """
        if not user:
            return self
        self.__user = user.__dict__
        return self
    
    def is_authenticated(self, status=True) -> bool:
        """
        Here is a property of Authenticate
        By default value is a True
        :param status: bool.
        :return: status
        """
        
        return status
    
    def is_active(self, status=True) -> bool:
        """
        Here is change an user's status of is_active.
        By default value is a True
        :param status: bool.
        :return: status
        """
        return status
    
    def is_anonymous(self, status=False) -> bool:
        """
        Here is change an user's status of is_anonymous.
        By default value is a False
        :param status: bool.
        :return: status
        """
        return status
    
    def get_id(self) -> str:
        """

        :return: Here , an id from user.
        """
        ind = self.__user["id"]
        return str(ind)
    
    def get_token(self) -> bool:
        """
        This is 'activation_token' from db.
        :return: True or False
        """
        return self.__user["activation_token"]
    
    def get_firstname(self) -> str:
        """
        This is 'firstname' from db.
        :return: True or False
        """
        return self.__user["firstname"]
    
    def fromDB(self, user_id: str) -> dict:
        """
        For of decorate '@login_manager.user_loader'
        :param user_id: str
        :return:
        """
        try:
            sess = Session()
            self.__user = sess.query(Users).filter_by(id=int(user_id)).first()
            sess.close()
            if self.__user == None:
                """If we have a problem to the user's search then
                the user.id to install int('-1')
                """
                print("[UserLogin => fromDB]: None")
                return self.__dict__
        except Exception as err:
            print(f"[UserLogin => fromDB]: Error => {err.__str__()}")
        finally:
            # session.close()
            user = self.__user
            return user
