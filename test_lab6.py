import pytest
from pydantic import ValidationError
from models import Person, Source, Block

def test_valid_person():
    p = Person(id=101, name="Anna", addr="Lviv, UA")  
    assert p.name == "Anna"

def test_invalid_person_name():
    with pytest.raises(ValidationError):
        Person(id=101, name="A", addr="Lviv")

def test_valid_source():
    s = Source(id=1, ip_addr="192.168.1.1", country_code="UA")
    assert s.country_code == "UA"

def test_invalid_source_ip():
    with pytest.raises(ValidationError):
        Source(id=1, ip_addr="999.999", country_code="UA")

def test_valid_block():
    b = Block(id="face1234", view=10, desc="Test block")
    assert b.id == "face1234"

def test_invalid_block_id_short():
    with pytest.raises(ValidationError):
        Block(id="abc", view=10, desc="Short ID")

def test_invalid_block_negative_view():
    with pytest.raises(ValidationError):
        Block(id="face1234", view=-1, desc="Negative view")