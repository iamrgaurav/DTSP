import uuid
from src.common.database import Database
import src.models.retailers.constants as RetailerConstants
import src.models.retailers.errors as Errors
from src.models.sim.sim import Sim
from src.models.users.user import User

from src.common.utils import Utils
import datetime


class Retailer:
    def __init__(self, username, password, aadhaar_no, image, name, address, gender, dob, phone, _id=None ):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.username = username
        self.password = password
        self.aadhaar_no = aadhaar_no
        self.name = name
        self.address = address
        self.gender = gender
        self.dob = datetime.datetime.strptime(dob, "%Y-%m-%d") if isinstance(dob, str) else dob
        self.phone = phone
        self.image = image

    def json(self):
        return {
            "_id": self._id,
            "username": self.username,
            "password": self.password,
            "aadhaar_no": self.aadhaar_no,
            "name": self.name,
            "gender": self.gender,
            "address": self.address,
            "dob": self.dob,
            "phone": self.phone,
            "image": self.image
        }

    def save_to_db(self):
        Database.update(RetailerConstants.COLLECTION, {"_id": self._id}, self.json())

    @classmethod
    def get_by_id(cls, retailer_id):
        data = Database.find_one(RetailerConstants.COLLECTION, {"_id": retailer_id})
        return cls(**data) if data is not None else False

    @classmethod
    def get_all_retailers(cls):
        cluster_data = Database.find(RetailerConstants.COLLECTION,{})
        return [cls(**data) for data in cluster_data] if cluster_data is not None else False

    @classmethod
    def get_by_username(cls, username):
        data = Database.find_one(RetailerConstants.COLLECTION, {'username': username})
        return cls(**data) if data is not None else False

    @classmethod
    def is_login_valid(cls, username, password):
        """
        This methods verifies that an e-mail/password combo as
        sent by the site form is valid or not. Checks that email
        exists, and the password associated to that e-mail is correct
        :param email:The user's email
        :param password: A sha-512 hashed password
        :return:true if Login successful otherwise false
        """
        user = cls.get_by_username(username)
        if user is None:
            # Tells that user doesn't exist
            raise Errors.UserNotExistError('There is no account with the username: {}'.format(username))
        if not Utils.check_hashed_password(password, user.password):
            raise Errors.PasswordIncorrectError('Incorrect Password')
        return True

    @classmethod
    def is_registered(cls, username, password):
        """
        This method register user using an email and password
        password comes already in hashed as sHa_512
        :param email:user's email (might be invalid)
        :param password: sha_512 password
        :return:True if registration successful else false otherwise exception can be raised
        """
        Retailer(username=username, password=Utils.hash_password(password)).save_to_db()
        return True

    @classmethod
    def is_authenticated(cls, aadhaar):
        """
        This method authenticate user  using fingerprint and aadhaar.
        :param aadhaar:

        :return:True if authentication is successful else false
        """
        user =User.get_by_aadhaar(aadhaar)

    @staticmethod
    def get_user_by_adhaar(adhaar):
        return User.get_by_aadhaar(aadhaar)

    @staticmethod
    def get_user_sim(aadhaar):
        return Sim.get_by_aadhaar(aadhaar)
