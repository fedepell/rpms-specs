%global srcname snmpsim

%global common_description %{expand:
SNMP Simulator
snmplabs.com/snmpsim/}

Name:           python-%{srcname}
Version:        0.4.7
Release:        2%{?dist}
Summary:        SNMP Simulator
License:        BSD-2-Clause
URL:            https://github.com/etingof/snmpsim
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch


%description %{common_description}

%package -n python3-%{srcname}-doc
Summary:        %{summary}
BuildRequires:  python3-sphinx
%description -n python3-%{srcname}-doc
Docs for python-snmpsim %{srcname}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-pysnmp

%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
cd docs
make html

%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
# One of the tests connects to some SNMP server, so run (explicitly) just a local one.
# Some tests is better than no tests ;-)
PYTHONPATH=.:$PYTHONPATH python scripts/mib2dev.py --mib-module=SNMPv2-MIB

%files -n python3-%{srcname} -f %{pyproject_files}
/usr/bin/datafile.py
/usr/bin/mib2dev.py
/usr/bin/pcap2dev.py
/usr/bin/snmprec.py
/usr/bin/snmpsimd.py
/usr/snmpsim/*

%license LICENSE.txt
%doc README.md CHANGES.txt TODO.txt THANKS.txt

%files -n python3-%{srcname}-doc
%doc docs/build/html

%changelog
* Wed Sep 27 2023 Federico Pellegrin <fede@evolware.org> - 0.4.7-2
- Fix pysnmp dependency and download URL

* Wed Sep 27 2023 Federico Pellegrin <fede@evolware.org> - 0.4.7-1
- Init at 0.4.7


