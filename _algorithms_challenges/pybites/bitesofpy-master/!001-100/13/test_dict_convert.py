import json

from Previous.dict_convert import blog, dict2nt, nt2json

nt = dict2nt(blog)


def test_dict2nt():
    assert nt.name == 'PyBites'
    assert nt.founders[1] == 'Bob'
    assert nt.tags[2] == 'Learn by Doing'
    assert nt.started.year == 2016

    assert nt.__class__.__base__ == tuple
    assert hasattr(nt, '_asdict')


def test_nt2json():
    output = nt2json(nt)
    assert type(output) == str

    data = json.loads(output)
    assert data['name'] == 'PyBites'
    assert data['founders'][0] == 'Julian'
    assert data['tags'][0] == 'Python'
    assert data['started'][:4] == '2016'