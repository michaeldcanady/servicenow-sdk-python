from servicenow._internal._collection import Collection


def test_collection_init():

    collection = Collection(**{"ExAmPLE": "value"})

    assert list(collection.keys()) == ["example"]
    assert list(collection.values()) == ["value"]


def test_collection_setitem():
    collection = Collection()

    collection["ExAmPLE"] = "value"

    assert list(collection.keys()) == ["example"]
    assert list(collection.values()) == ["value"]


def test_collection_getitem():
    collection = Collection()
    collection["ExAmPLE"] = "value"

    assert collection["example"] == "value"
