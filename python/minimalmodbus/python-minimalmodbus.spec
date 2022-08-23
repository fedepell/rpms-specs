%global srcname minimalmodbus

Name:           python-%{srcname}
Version:        2.0.1
Release:        1%{?dist}
Summary:        Easy-to-use Modbus RTU and Modbus ASCII implementation for Python
License:        ASL 2.0
URL:            https://github.com/pyhys/minimalmodbus
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# Needed for testing
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Easy-to-use Modbus RTU and Modbus ASCII implementation for Python.
}

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
%pyproject_save_files minimalmodbus


%check
%{pytest}


%files -n python3-%{srcname} -f %{pyproject_files}
%doc *.rst docs
%license LICENSE


%changelog
* Tue Aug 23 2022 Federico Pellegrin <fede@evolware.org> - 2.0.1-1
- First packaging of python-minimalmodbus
