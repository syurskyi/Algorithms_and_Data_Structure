def convert(number):
    result = ""
    for factor, sound in {
        3: "Pling",
        5: "Plang",
        7: "Plong"
    }.items():
        if number % factor == 0:
            result += sound
    return f"{result or number}"
