from passwd import get_users_for_shell

# https://www.ibm.com/support/knowledgecenter/en/ssw_aix_72/com.ibm.aix.security/passwords_etc_passwd_file.htm
OTHER_PASSWD_OUTPUT = """root:!:0:0::/:/usr/bin/ksh
daemon:!:1:1::/etc:
bin:!:2:2::/bin:
sys:!:3:3::/usr/sys:
adm:!:4:4::/var/adm:
uucp:!:5:5::/usr/lib/uucp:
guest:!:100:100::/home/guest:
nobody:!:4294967294:4294967294::/:
lpd:!:9:4294967294::/:
lp:*:11:11::/var/spool/lp:/bin/false
invscout:*:200:1::/var/adm/invscout:/usr/bin/ksh
nuucp:*:6:5:uucp login user:/var/spool/uucppublic:/usr/sbin/uucp/uucico
paul:!:201:1::/home/paul:/usr/bin/ksh
jdoe:*:202:1:John Doe:/home/jdoe:/usr/bin/ksh"""


def test_get_users_for_shell_default_args():
    actual = get_users_for_shell()
    expected = ['artagnon', 'avar', 'chad', 'gerrit2',
                'git-svn-mirror', 'root', 'ssh-rsa']
    assert sorted(actual) == expected


def test_get_users_for_sh_shell():
    actual = get_users_for_shell(grep_shell='sh')
    expected = ['backup', 'bin', 'daemon', 'games', 'gnats', 'irc',
                'libuuid', 'list', 'lp', 'mail', 'man', 'news',
                'nobody', 'proxy', 'sys', 'uucp', 'www-data']
    assert sorted(actual) == expected


def test_get_users_for_false_shell():
    actual = get_users_for_shell(grep_shell='false')
    expected = ['Debian-exim', 'avahi', 'ftp', 'messagebus',
                'mysql', 'postfix', 'statd']
    assert sorted(actual) == expected


def test_get_users_for_different_passwd_output_and_ksh_shell():
    actual = get_users_for_shell(passwd_output=OTHER_PASSWD_OUTPUT,
                                 grep_shell='ksh')
    expected = ['invscout', 'jdoe', 'paul', 'root']
    assert sorted(actual) == expected