import pytest
from main import (
    create_random_document,
    save_document,
    find_document_by_uuid,
    update_document_field,
    delete_document_by_uuid,
)
import uuid

def test_create_random_document():
    uuid = create_random_document()
    assert find_document_by_uuid(uuid) is not None


def test_save_document():
    document = {"UUID": str(uuid.uuid4()), "name": "TestDoc", "value": 200}
    save_document(document)
    assert find_document_by_uuid(document["UUID"]) == document



def test_find_document_by_uuid():
    uuid = create_random_document()
    document = find_document_by_uuid(uuid)
    assert document is not None
    assert document["UUID"] == uuid   


def test_update_document_field():
    uuid = create_random_document()
    update_document_field(uuid, "value", 500)
    updated_document = find_document_by_uuid(uuid)
    assert updated_document["value"] == 500


def test_delete_document_by_uuid():
    uuid = create_random_document()
    delete_document_by_uuid(uuid)
    assert find_document_by_uuid(uuid) is None