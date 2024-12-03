def test_create_random_document():
    uuid = create_random_document()
    assert find_document_by_uuid(uuid) is not None