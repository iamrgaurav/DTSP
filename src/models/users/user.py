from src.common.database import Database
import datetime
import uuid
import src.models.users.constants as UserConstants


class User(object):
    def __init__(self, aadhaar_no, image, name, address, gender, dob, fingerprint=None, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.aadhaar_no = aadhaar_no
        self.name = name
        self.address = address
        self.gender = gender
        self.dob = datetime.datetime.strptime(dob, "%Y-%m-%d") if isinstance(dob, str) else dob
        self.image = image
        self.fingerprint = fingerprint

    def json(self):
        return {
            "_id": self._id,
            "aadhaar_no": self.aadhaar_no,
            "name": self.name,
            "gender": self.gender,
            "address": self.address,
            "dob": self.dob,
            "fingerprint": self.fingerprint,
            "image": self.image
        }

    def save_to_db(self):
        Database.update(UserConstants.COLLECTION, {"_id": self._id}, self.json())

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one(UserConstants.COLLECTION, {'_id': _id})
        return cls(**data) if data is not None else False

    @classmethod
    def get_by_aadhaar(cls, aadhaar):
        data = Database.find_one(UserConstants.COLLECTION, {'aadhaar_no': aadhaar})
        return cls(**data) if data is not None else False


