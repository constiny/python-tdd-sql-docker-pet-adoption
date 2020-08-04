from pet import Pet

def test_pet_class():
    p = Pet()
    assert isinstance(p, Pet)
    assert p.name == "molly"

def test_pet_has_name():
    p = Pet("fido")
    assert p.name == "fido"

def test_pet_has_name_and_species():
    d1 = {"age": 3, "sex": "female"}
    p1 = Pet(**d1)
    assert p1.name == "molly"
    assert p1.species == "dog"
    d2 = {"name": "frank", "species": "spider"}
    p2 = Pet(**d2)
    assert p2.name == "frank"
    assert p2.species == "spider"

def test_pet_has_age_and_sex():
    d = {"age": 7, "sex": "male"}
    p = Pet(**d)
    assert p.name == "molly"
    assert p.species == "dog"
    assert p.age == 7
    assert p.sex == "male"
