from reqs import changed_dependencies

# version might be fictitious for testing purposes
old_reqs = """
certifi==2017.4.17
chardet==3.0.4
click==6.7
Faker==0.7.12
Flask==0.12.1
"""
new_reqs = """
certifi==2016.11.29
chardet==2.0.4
click==5.0
Faker==1.0.2
Flask==1.0.2
"""
other_old_reqs = """
twilio==6.23.1
urllib3==1.21.1
Werkzeug==0.12.1
WTForms==1.19.0
"""
other_new_reqs = """
twilio==6.3.0
urllib3==1.21.1
Werkzeug==0.14.1
WTForms==2.1
"""


def test_changed_dependencies_old_vs_new():
    actual = changed_dependencies(old_reqs, new_reqs)
    expected = ['Faker', 'Flask']
    assert sorted(actual) == expected


def test_changed_dependencies_other_data():
    actual = changed_dependencies(other_old_reqs, other_new_reqs)
    expected = ['WTForms', 'Werkzeug']
    assert sorted(actual) == expected