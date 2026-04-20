class AdapterService:
    def normalize(self, payload: dict) -> dict:
        # basic normalization logic
        return {
            "normalized_payload": payload,
            "status": "normalized"
        }
