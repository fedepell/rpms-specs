%global srcname robotframeworklexer
%global debug_package %{nil}

Name:           python-%{srcname}
Version:        1.1
Release:        1%{?dist}
Summary:        Pygments lexer for Robot Framework test data
License:        ASL 2.0
URL:            https://github.com/robotframework/pygmentslexer
Source0:        %{pypi_source robotframeworklexer}
# Source0:        https://files.pythonhosted.org/packages/9a/9f/a1fcd44548cbd78e52a31277c1c69a421c32186db9cdb5ccc2effec0e633/robotframeworklexer-1.1.tar.gz
BuildArch:      noarch
BuildRequires:  gcc

%global _description\
This project implements a Pygments lexer for Robot Framework test data in plain text format.\
It is available as a separate plugin and included in Pygments 1.6 and newer.

%description
%{_description}

%package -n python3-%{srcname}

Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-pygments

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst BUILD.rst COPYRIGHT.txt
%license LICENSE.txt
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__

%changelog
* Fri Feb 18 2022 Federico Pellegrin <fede@evolware.org> - 1.1-1
- First packaging of robotframeworklexer Python module

