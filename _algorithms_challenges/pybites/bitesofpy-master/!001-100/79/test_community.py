from Previous.community import get_csv, create_user_bar_chart


# making sure to call requests just once!
content = get_csv()

expected_output = """Africa/Algiers       | ++
Africa/Cairo         | +
Africa/Monrovia      | +
Africa/Nairobi       | ++++
America/Buenos_Aires | +
America/Chicago      | ++++++++++++++
America/Denver       | ++++
America/Fortaleza    | +
America/Los_Angeles  | +++++++++++++++++++++++++++++++++++
America/Manaus       | +
America/Mexico_City  | +++
America/New_York     | +++++++++++++++++++++++++++
America/Regina       | +
America/Santiago     | +
America/Sao_Paulo    | ++++
Asia/Amman           | +
Asia/Bangkok         | +
Asia/Chongqing       | ++++
Asia/Dhaka           | +
Asia/Istanbul        | ++
Asia/Jerusalem       | +
Asia/Kolkata         | +++++++++++++
Asia/Kuala_Lumpur    | +
Asia/Muscat          | +
Asia/Taipei          | +
Australia/Brisbane   | +
Australia/Canberra   | ++++++
Australia/Perth      | +
Europe/Amsterdam     | ++++++++++++++
Europe/Athens        | ++
Europe/Belgrade      | +
Europe/Helsinki      | +
Europe/London        | ++++++++++++
Europe/Moscow        | ++
Europe/Warsaw        | ++
Pacific/Honolulu     | +
""".splitlines()


def test_output(capfd):
    create_user_bar_chart(content)
    actual_output = [line.strip().replace(' ', '') for line in
                     capfd.readouterr()[0].splitlines()]

    for line in expected_output:
        assert line.strip().replace(' ', '') in actual_output, \
               f'{line} not in {actual_output}'