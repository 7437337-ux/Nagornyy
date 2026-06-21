VALID_TYPES = {"click", "submit", "view", "error", "custom"}
REQUIRED_FIELDS = {"id", "type", "payload"}


class EventValidator:
    def validate(self, event):
        return True, []
