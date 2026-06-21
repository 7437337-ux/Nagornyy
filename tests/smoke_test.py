from src.core import EventProcessor


def test_smoke_system_alive():
    processor = EventProcessor()
    assert processor is not None
    assert processor.get_stats()["total_processed"] == 0


def test_smoke_end_to_end():
    processor = EventProcessor()
    event = {"id": 1, "type": "click", "payload": {"page": "/home"}}
    result = processor.process(event)
    assert result["status"] == "ok"


def test_smoke_constants():
    from src.validator import ALLOWED_TYPES
    assert "unknown_type" in ALLOWED_TYPES  # intentional error for demo
