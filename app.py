from flask import Flask, request

from database.firebase_connector import FireBaseConnector
from services.retrieve_user_service import RetrieveUserService
from services.update_user_service import UpdateUserService

app = Flask(__name__)

# Initialize connector
firebase_connector = FireBaseConnector()

# Initialize services
retrieve_user_service = RetrieveUserService(firebase_connector)
update_user_service = UpdateUserService(firebase_connector)


# Routes
@app.route("/")
def health():
    return {'message': 'service is up and running.'}


@app.route("/user/retrieve")
def retrieve_user():
    return retrieve_user_service.retrieve_user()


@app.route("/user/update")
def update_user():
    return update_user_service.update_user()


if __name__ == '__main__':
    app.run()