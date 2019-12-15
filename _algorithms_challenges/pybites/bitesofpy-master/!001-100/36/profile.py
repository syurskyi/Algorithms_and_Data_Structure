def get_profile(name: str, age: int, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError("Age must be a whole number")
    if len(sports) > 5:
        raise ValueError("A maximum of five sports are allowed")
    res = {"name": name, "age": age}
    if len(sports) > 0:
        res["sports"] = sorted(sports)
    if len(awards) > 0:
        res["awards"] = awards
    return res
