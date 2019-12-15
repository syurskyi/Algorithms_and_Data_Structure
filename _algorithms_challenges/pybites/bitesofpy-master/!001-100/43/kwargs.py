def get_profile(*args, **kwargs) -> str:
    name = profession = None
    for kw in kwargs:
        if kw == 'name':
            name = kwargs['name']
        elif kw == 'profession':
            profession = kwargs['profession']
        else:
            raise TypeError
    if name is None:
        name = 'julian'
    if profession is None:
        profession = 'programmer'
    if type(profession) != str or type(name) != str or len(args) > 0:
        raise TypeError
    return f'{name} is a {profession}'
