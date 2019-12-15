import pytest

from screenfetch import output, sysinfo_scrape

debian = """
         _,met$$$$$gg.           mohh@SERENiTY
      ,g$$$$$$$$$$$$$$$P.        OS: Mint 19 tara
    ,g$$P""       ""'Y$$.".      Kernel: x86_64 Linux 4.15.0-34-generic
   ,$$P'              '$$$.      Uptime: 1d 2h 50m
  ',$$P       ,ggs.     '$$b:    Packages: 2352
  'd$$'     ,$P"'   .    $$$     Shell: zsh 5.4.2
   $$P      d$'     ,    $$P     Resolution: 1366x768
   $$:      $$.   -    ,d$$'     DE: Cinnamon 3.8.9
   $$\;      Y$b._   _,d$P'      WM: Muffin
   Y$$.    '.'"Y$$$$P"'          WM Theme: Linux Mint (Mint-Y)
   '$$b      "-.__               GTK Theme: Mint-Y [GTK2/3]
    'Y$$                         Icon Theme: Mint-Y
     'Y$$.                       Font: Noto Sans 9
       '$$b.                     CPU: AMD A10-7400P Radeon R6, 10 Compute Cores 4C+6G @ 4x 2.5GHz [101.0°C]
         'Y$$b.                  GPU: AMD KAVERI (DRM 2.50.0 / 4.15.0-34-generic, LLVM 6.0.0)
            '"Y$b._              RAM: 2429MiB / 6915MiB
                '"'""           
"""
mac = """
                -/+:.          ejo@BlackOil
               :++++.          OS: 64bit Mac OS X 10.13.6 17G65
              /+++/.           Kernel: x86_64 Darwin 17.7.0
      .:-::- .+/:-''.::-       Uptime: 1d 49m
   .:/++++++/::::/++++++/:'    Packages: 236
 .:///////////////////////:'   Shell: bash 4.4.23
 ////////////////////////'     Resolution: 2560x1600
-+++++++++++++++++++++++'      DE: Aqua
/++++++++++++++++++++++/       WM: Quartz Compositor
/sssssssssssssssssssssss.      WM Theme: Blue
:ssssssssssssssssssssssss-     Font: SourceCodePro-Medium
 osssssssssssssssssssssssso/'  CPU: Intel Core i7-4980HQ @ 2.80GHz
 'syyyyyyyyyyyyyyyyyyyyyyyy+'  GPU: Intel Iris Pro / NVIDIA GeForce GT 750M
  'ossssssssssssssssssssss/    RAM: 9960MiB / 16384MiB
    :ooooooooooooooooooo+.    
     ':+oo+/:-..-:/+o+/-      
"""


@pytest.fixture(scope="module")
def sysinfo():
    """Make a module scope sysinfo object"""
    return sysinfo_scrape(output)


def test_sysinfo_scrape_type(sysinfo):
    """Test for proper object"""
    assert isinstance(sysinfo, dict)


def test_sysinfo_scrape_name(sysinfo):
    """Test for inclusion of the 'Name' key"""
    assert sysinfo["Name"] == "mohh@SERENiTY"


def test_sysinfo_scrape_length(sysinfo):
    """Test for correct amount of entries"""
    assert len(sysinfo) == 16


def test_sysinfo_scrape_keys(sysinfo):
    """Test for the proper keys"""
    expected = [
        'Name', 'OS', 'Kernel', 'Uptime', 'Packages', 'Shell', 
        'Resolution', 'DE', 'WM', 'WM Theme', 'GTK Theme', 'Icon Theme', 
        'Font', 'CPU', 'GPU', 'RAM'
    ]
    assert list(sysinfo.keys()) == expected


def test_sysinfo_scrape_values(sysinfo):
    """Test for the proper values"""
    expected = [
        'mohh@SERENiTY', 'Mint 19 tara', 'x86_64 Linux 4.15.0-34-generic', 
        '1d 4m', '2351', 'zsh 5.4.2', '1366x768', 'Cinnamon 3.8.9', 'Muffin', 
        'Linux Mint (Mint-Y)', 'Mint-Y [GTK2/3]', 'Mint-Y', 'Noto Sans 9', 
        'AMD A10-7400P Radeon R6, 10 Compute Cores 4C+6G @ 4x 2.5GHz [101.0°C]', 
        'AMD KAVERI (DRM 2.50.0 / 4.15.0-34-generic, LLVM 6.0.0)', 
        '1886MiB / 6915MiB'
    ]
    assert list(sysinfo.values()) == expected


def test_sysinfo_scrape_debian():
    """Test to see if it works with different distro logos"""
    sysinfo = sysinfo_scrape(debian)
    assert sysinfo["Resolution"] == "1366x768"


def test_sysinfo_scrape_mac():
    """Test to see if it works with different distro logos"""
    sysinfo = sysinfo_scrape(mac)
    assert sysinfo["Name"] == "ejo@BlackOil"