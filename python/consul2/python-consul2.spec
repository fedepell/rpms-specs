%global srcname consul2

Name:           python-%{srcname}
Version:        0.1.5
Release:        1%{?dist}
Summary:        Python client for the Consul HTTP API
License:        MIT
URL:            https://github.com/poppyred/python-consul2
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel


%global _description %{expand:
Python client for the Consul HTTP API ,Continue develop on
cablehead/python-consul }

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
%pyproject_save_files consul


# %check
# Tests cannot be run, missing dependency pytest-twisted (and maybe more)


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.rst
%license LICENSE


%changelog
* Tue Nov 29 2022 Federico Pellegrin <fede@evolware.org> - 0.1.5-1
- Init at 0.1.5
