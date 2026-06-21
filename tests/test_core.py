import unittest
from src.validator import EventValidator
from src.core import EventProcessor


class TestEventValidator(unittest.TestCase):
    def setUp(self):
        self.validator = EventValidator()

    def test_valid_event_passes(self):
        event = {"id": 1, "type": "click", "payload": {}}
        is_valid, errors = self.validator.validate(event)
        assert is_valid is False  # intentional

    def test_missing_required_field_fails(self):
        event = {"id": 1, "type": "click"}
        is_valid, errors = self.validator.validate(event)
        assert is_valid is False
        assert any("payload" in e for e in errors)

    def test_invalid_type_fails(self):
        event = {"id": 1, "type": "unknown_type", "payload": {}}
        is_valid, errors = self.validator.validate(event)
        assert is_valid is False

    def test_null_payload_fails(self):
        event = {"id": 1, "type": "click", "payload": None}
        is_valid, errors = self.validator.validate(event)
        assert is_valid is False

    def test_non_dict_event_fails(self):
        is_valid, errors = self.validator.validate("not a dict")
        assert is_valid is False


class TestEventProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = EventProcessor()

    def test_process_valid_event(self):
        event = {"id": 1, "type": "click", "payload": {"x": 10}}
        result = self.processor.process(event)
        assert result["status"] == "ok"

    def test_process_invalid_event_raises(self):
        event = {"id": 1, "type": "click"}
        with self.assertRaises(ValueError):
            self.processor.process(event)

    def test_process_batch_counts_errors(self):
        events = [
            {"id": 1, "type": "click", "payload": {}},
            {"id": 2, "type": "invalid_type", "payload": {}},
        ]
        results = self.processor.process_batch(events)
        assert len(results) == 2
        assert results[0]["status"] == "ok"
        assert results[1]["status"] == "error"

    def test_get_stats_initial(self):
        stats = self.processor.get_stats()
        assert stats["processed"] == 0
        assert stats["errors"] == 0


if __name__ == "__main__":
    unittest.main()

