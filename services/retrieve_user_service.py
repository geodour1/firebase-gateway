from interfaces.ifirebase_connector import IFireBaseConnector
from interfaces.iretrieve_user_service import IRetrieveUserService

class RetrieveUserService(IRetrieveUserService):
    def __init__(self, firebase: IFireBaseConnector):
        self.firebase = firebase
