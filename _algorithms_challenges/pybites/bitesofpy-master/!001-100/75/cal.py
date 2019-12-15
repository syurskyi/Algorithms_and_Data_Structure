def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    lines = calendar_output.splitlines(keepends=False)
    days = lines[1].split()
    result = dict()
    for line in lines[2:]:
        for p in range(7):
            s = line[p * 3:p * 3 + 2].strip()
            if s:
                result[int(s)] = days[p]
    return result
