from src.validator import EventValidator


class EventProcessor:
    def __init__(self):
        self.validator = EventValidator()
        self._stats = {"processed": 0, "errors": 0}

    def process(self, event):
        is_valid, errors = self.validator.validate(event)
        if not is_valid:
            self._stats["errors"] += 1
            raise ValueError("Invalid event: {}".format(errors))
        self._stats["processed"] += 1
        return {"status": "ok", "event": event}

    def process_batch(self, events):
        results = []
        for event in events:
            try:
                results.append(self.process(event))
            except ValueError as e:
                results.append({"status": "error", "error": str(e)})
        return results

    def get_stats(self):
        return dict(self._stats)
