%global srcname robotframework

Name:           python-%{srcname}
Version:        5.0.1
Release:        5%{?dist}
Summary:        Generic automation framework for acceptance testing and RPA
License:        Apache-2.0
URL:            https://github.com/robotframework/robotframework
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
# https://github.com/robotframework/robotframework/issues/4401
Patch0:         0001-Patch_tests_with_Python_3_11.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-jsonschema

%global _description %{expand:
Robot Framework is a generic open source automation framework for acceptance
testing, acceptance test driven development (ATDD), and robotic process
automation (RPA).
It has simple plain text syntax and it can be extended easily with libraries
implemented using Python or Java.}


%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}


%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -p 1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files robot


%check
%{python3} utest/run.py


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst BUILD.rst INSTALL.rst CONTRIBUTING.rst
%license LICENSE.txt
%{_bindir}/{robot,rebot,libdoc}


%changelog
* Fri Sep 30 2022 Federico Pellegrin <fede@evolware.org> - 5.0.1-5
- Improve spec file after package review

* Wed Sep 28 2022 Federico Pellegrin <fede@evolware.org> - 5.0.1-4
- Improve spec file after package review

* Fri Aug 05 2022 Federico Pellegrin <fede@evolware.org> - 5.0.1-3
- Fix tests with Python 3.11

* Thu May 19 2022 Piotr Szubiakowski <pszubiak@eso.org> - 5.0.1-2
- Use pyproject_save_files macro

* Tue May 17 2022 Piotr Szubiakowski <pszubiak@eso.org> - 5.0.1-1
- Update to 5.0.1

* Fri May 13 2022 Piotr Szubiakowski <pszubiak@eso.org> - 4.1.3-2
- Adapt to Fedora Python Packaging Guidelines

* Fri Feb 18 2022 Federico Pellegrin <fede@evolware.org> - 4.1.3-1
- First packaging of robotframework
