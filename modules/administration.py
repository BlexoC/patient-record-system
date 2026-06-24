from datetime import datetime


class Administration:
    def __init__(self, patient_id, ward_id, administerd_at=None):
        self.patient_id = patient_id
        self.ward_id = ward_id
        self.administerd_at = administerd_at or datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "ward_id": self.ward_id,
            "administerd_at": self.administerd_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            patient_id=data["patient_id"],
            ward_id=data["ward_id"],
            administerd_at=data.get["administerd_at"],
        )
