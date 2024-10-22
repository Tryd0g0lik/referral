"""
This is a description of user_login.
"""

from typing import Union

from referral.models import Session
from referral.models_more.model_users import Users

session = Session()


class UserLogin:
    """
    This a class make the present of single user after
    the event authorization. It is
    for  a LoginManager work
    """

    def create(self, user):
        """
        :param user: object
        :return: user's object from db
        """
        if not user:
            return self
        self.__user = user.__dict__
        return self

    def is_authenticated(self) -> bool:
        """Here is a property of Authenticate"""
        return True

    def is_active(self) -> bool:
        """Here is change an user's status."""
        return True

    def is_anonymous(self) -> bool:
        return False

    def get_id(self) -> str:
        """

        :return: Here , an id from user.
        """
        ind = self.__user["id"]
        return str(ind)

    def get_token(self) -> bool:
        return self.__user["activation_token"]

    def get_firstname(self) -> str:
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
                return self
        except Exception as err:
            print(f"[UserLogin => fromDB]: Error => {err.__str__()}")
        finally:
            session.close()
            user = self.__user
            return user
