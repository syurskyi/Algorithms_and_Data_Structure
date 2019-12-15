import re


def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    fix_text = trans_text
    pattern = r'<(?P<tag>pre|code).*?>(?P<content>.*?)</(?P=tag)>'
    eng = re.finditer(pattern, org_text, re.MULTILINE | re.DOTALL)
    rus = re.finditer(pattern, trans_text, re.MULTILINE | re.DOTALL)
    for (e_t, r_t) in list(zip(eng, rus)):
        if e_t.group('tag') in {'code', 'pre'}:
            fix_text = fix_text.replace(r_t.group('content'), e_t.group('content'), 1)
    return fix_text
