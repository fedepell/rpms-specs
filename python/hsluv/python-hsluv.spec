%global srcname hsluv

Name:           python-%{srcname}
Version:        5.0.3
Release:        1%{?dist}
Summary:        A Python implementation of HSLuv (revision 4)
License:        MIT
URL:            https://github.com/hsluv/hsluv-python
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
A Python implementation of HSLuv (revision 4)}

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}


%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -p 1 -n %{srcname}-python-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files hsluv

%check
%{python3} setup.py test


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt


%changelog
* Mon May 30 2022 Federico Pellegrin <fede@evolware.org> - 5.0.3-1
- First packaging of python-hsluv
