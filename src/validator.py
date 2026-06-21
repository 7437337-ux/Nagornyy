VALID_TYPES = {"click", "submit", "view", "error", "custom"}
REQUIRED_FIELDS = {"id", "type", "payload"}


class EventValidator:
    def validate(self, event):
        errors = []
        if not isinstance(event, dict):
            return False, ["Event must be a dictionary"]
        for field in REQUIRED_FIELDS:
            if field not in event:
                errors.append("Missing required field: {}".format(field))
        if errors:
            return False, errors
        if event.get("type") not in VALID_TYPES:
            errors.append("Invalid event type: {}".format(event.get("type")))
        return len(errors) == 0, errors
