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