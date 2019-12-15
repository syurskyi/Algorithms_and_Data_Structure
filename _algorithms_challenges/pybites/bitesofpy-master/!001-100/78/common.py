from collections import Counter


def common_languages(programmers):
    languages = Counter(lang for _, langs in programmers.items() for lang in langs)
    return list(lang for lang, count in languages.items() if count == len(programmers))
