%global srcname robotframework
%global debug_package %{nil}

Name:           python-%{srcname}
Version:        4.1.3
Release:        1%{?dist}
Summary:        Generic automation framework for acceptance testing and RPA
License:        ASL 2.0
URL:            https://github.com/robotframework/robotframework
#Source0:        % { pypi_source robotframework}
Source0:        https://files.pythonhosted.org/packages/51/68/30dc6a4372b1a991e22663d74d8fb9b6cedb328167c426db6431a030813f/robotframework-4.1.3.zip
BuildArch:      noarch
BuildRequires:  gcc

%global _description\
Robot Framework is a generic open source automation framework for acceptance testing, acceptance test driven development (ATDD), and robotic process automation (RPA). It has simple plain text syntax and it can be extended easily with libraries implemented using Python or Java.

%description
%{_description}

%package -n python3-%{srcname}

Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

%prep
%autosetup -p 1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst BUILD.rst INSTALL.rst CONTRIBUTING.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/robot/
%{_bindir}/*

%changelog
* Fri Feb 18 2022 Federico Pellegrin <fede@evolware.org> - 4.1.3-1
- First packaging of robotframework

