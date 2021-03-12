from interfaces.ifirebase_connector import IFireBaseConnector
from interfaces.iupdate_user_service import IUpdateUserService

class UpdateUserService(IUpdateUserService):
    def __init__(self, firebase: IFireBaseConnector):
        self.firebase = firebase
