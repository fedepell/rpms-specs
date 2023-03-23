%global srcname pytest-custom_exit_code

Name:           python-%{srcname}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Exit pytest test session with custom exit code in different scenarios
License:        MIT
URL:            https://github.com/yashtodi94/pytest-custom_exit_code
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Exit pytest test session with custom exit code in different scenarios}

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
%pyproject_save_files pytest_custom_exit_code


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
* Thu Mar 23 2023 Federico Pellegrin <fede@evolware.org> - 0.3.0-1
- First import of 0.3.0
