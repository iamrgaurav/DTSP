import uuid
from src.common.database import Database
import src.models.sim.constants as SimConstants
import datetime

class Sim:
    def __init__(self, aadhaar_no, mobile_no, issue_date, _id=None, local_service_area=None):
        self.aadhaar_no = aadhaar_no
        self.mobile_no = mobile_no
        self.issue_date = datetime.datetime.strptime(issue_date, "%Y-%m-%d") if isinstance(issue_date, str) else issue_date
        self._id = uuid.uuid4().hex if _id is None else _id
        self.local_service_area = local_service_area

    def json(self):
        return {
            'aadhaar_no': self.aadhaar_no,
            'issue_date':self.issue_date.strftime("%Y-%m-%d"),
            'mobile_no': self.mobile_no,
            'local_service_area': self.local_service_area,
            '_id': self._id
        }

    def save_to_db(self):
        return Database.update(SimConstants.COLLECTION, {'_id': self._id}, self.json())

    @classmethod
    def get_by_id(cls, sim_id):
        data = Database.find_one(SimConstants.COLLECTION, {"_id": sim_id})
        return cls(**data) if data is not None else False

    @classmethod
    def get_by_aadhaar(cls, aadhaar_id):
        cluster_data = Database.find(SimConstants.COLLECTION, {"aadhaar_no": aadhaar_id})
        return [cls(**data) for data in cluster_data if cluster_data is not None] if cluster_data is not None else False

