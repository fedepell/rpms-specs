%global srcname robotframework-redislibrary

Name:           python-%{srcname}
Version:        1.2.3
Release:        1%{?dist}
Summary:        RedisLibrary is a Robot Framework test library which provides keywords for manipulating in-memory data stores in Redis
License:        MIT
URL:            https://github.com/robotframework-thailand/robotframework-redislibrary
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-redis
BuildRequires:  python3-robotframework
BuildRequires:  %{py3_dist pytest}


%global _description %{expand:
RedisLibrary is a Robot Framework test library which provides keywords for
manipulating in-memory data stores in Redis.}


%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}


%description -n python3-%{srcname} %{_description}


%prep
%autosetup -p 1 -n robotframework-redislibrary-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files RedisLibrary


%check
# Tests require "fakeredis" Python module which is currently not packaged


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGE.md docs/

%changelog
* Fri Aug 05 2022 Federico Pellegrin <fede@evolware.org> - 1.2.3-1
- Init at 1.2.3

