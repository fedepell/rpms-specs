%global srcname rellu
%global debug_package %{nil}

Name:           python-%{srcname}
Version:        0.7
Release:        1%{?dist}
Summary:        rellu -- Utilities to ease creating releases
License:        ASL 2.0
URL:            https://github.com/robotframework/rellu
Source0:        %{pypi_source rellu}
# Source0:        https://files.pythonhosted.org/packages/08/7c/697c97aca50e27aba9e0d834cad32906ff7f20e3fb511d7d13652ac46f6a/rellu-0.7.tar.gz
BuildArch:      noarch
BuildRequires:  gcc

%global _description\
This project contains tooling and templates to ease creating releases on GitHub and publishing them on PyPI.\
Designed to be used by Robot Framework and tools and libraries in its ecosystem, but can naturally be used\
also by other projects.

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
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Fri Feb 18 2022 Federico Pellegrin <fede@evolware.org> - 0.7-1
- First packaging of rellu Python module

