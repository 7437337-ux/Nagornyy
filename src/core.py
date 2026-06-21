from src.validator import EventValidator
from src.logger import logger


class EventProcessor:
    VERSION = "1.0.0"

    def __init__(self):
        self.validator = EventValidator()
        self._stats = {"processed": 0, "errors": 0}

    def process(self, event):
        is_valid, errors = self.validator.validate(event)
        if not is_valid:
            self._stats["errors"] += 1
            logger.error("Invalid event: %s", errors)
            raise ValueError("Invalid event: {}".format(errors))
        self._stats["processed"] += 1
        logger.info("Processed event id=%s type=%s", event.get("id"), event.get("type"))
        return {"status": "ok", "event": event}

    def process_batch(self, events: list) -> list:
        """Process a list of events, collect errors separately."""
        logger.info("Starting batch processing of %d events", len(events))
        results = []
        for event in events:
            try:
                results.append(self.process(event))
            except ValueError as e:
                results.append({"status": "error", "error": str(e)})
        return results

    def get_stats(self):
        return dict(self._stats)
