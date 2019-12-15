from reboot import calc_max_uptime, MAC1

MAC2 = """
reboot ~ Tue Sep 22 12:52
reboot ~ Sun Aug 30 23:17
reboot ~ Sat Aug 29 01:12
reboot ~ Fri Aug 28 22:07
"""

MAC3 = """
reboot    ~                         Fri Dec 18 23:58
reboot    ~                         Mon Dec 14 09:54
reboot    ~                         Wed Dec 11 23:21
reboot    ~                         Tue Nov 17 21:52
reboot    ~                         Tue Nov 17 06:01
reboot    ~                         Wed Nov 11 12:14
reboot    ~                         Sat Oct 31 13:40
reboot    ~                         Wed Oct 28 15:56
reboot    ~                         Wed Oct 28 11:35
reboot    ~                         Tue Oct 27 00:00
reboot    ~                         Sun Oct 18 17:28
reboot    ~                         Sun Oct 18 17:11
reboot    ~                         Mon Oct  5 09:35
reboot    ~                         Sat Oct  3 18:57
"""


def test_default_output():
    assert calc_max_uptime(MAC1) == (30, '2019-02-17')


def test_different_output():
    assert calc_max_uptime(MAC2) == (22, '2019-09-22')


def test_yet_another_output():
    assert calc_max_uptime(MAC3) == (24, '2019-12-11')