%global srcname ivi

Name:           python-%{srcname}
Version:        0.14.9
Release:        1%{?dist}
Summary:        Python-based interpretation of the Interchangeable Virtual Instrument standard
License:        MIT
URL:            https://github.com/python-ivi/python-ivi
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# Needed for testing
BuildRequires:  python3dist(pytest)

%global _description %{expand:
This package is a Python-based interpretation of the Interchangeable Virtual Instrument standard, a software abstraction for electronic test equipment that is remotely controllable.
}

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}


%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -p 1 -n python-%{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ivi


%check
%{python3} setup.py test


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md README AUTHORS doc/*.rst
%license COPYING


%changelog
* Tue Aug 23 2022 Federico Pellegrin <fede@evolware.org> - 0.14.9-1
- First packaging of python-ivi
