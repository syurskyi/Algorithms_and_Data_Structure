import inspect

from email_header import get_email_details, EMAIL_HEADER

OTHER_HEADER = """
Return-Path: <info@pybit.es>
From: Bob & Julian from PyBites (info@pybit.es)
To: pybites@ninja.com
Subject: New regex learning path!
Date: Sun, 18 Aug 2019 17:16:10 -0700 (PDT)
Envelope-To: pybites@ninja.com
...
X-SendGrid-Contentd-ID: {"test_id":"1371661776"}
"""


def test_source():
    src = inspect.getsource(get_email_details)
    assert 're.match' in src or 're.search' in src
    assert 'groupdict' in src


def test_given_header():
    actual = get_email_details(EMAIL_HEADER)
    expected = {'from': 'redacted-address',
                'to': 'redacted-address',
                'subject': 'A Test From SendGrid',
                'date': 'Wed, 19 Jun 2013 17:09:33'}
    assert actual == expected


def test_other_header():
    actual = get_email_details(OTHER_HEADER)
    expected = {'from': 'Bob & Julian from PyBites (info@pybit.es)',
                'to': 'pybites@ninja.com',
                'subject': 'New regex learning path!',
                'date': 'Sun, 18 Aug 2019 17:16:10'}
    assert actual == expected


def test_no_match():
    assert get_email_details('bogus') is None