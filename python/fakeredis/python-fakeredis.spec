%global srcname fakeredis

%if %{undefined fc36}
# pytest-asyncio >= 0.19.0 is missing in <= FC36
%bcond_without  tests
%endif

Name:           python-%{srcname}
Version:        1.9.4
Release:        1%{?dist}
Summary:        Fake implementation of redis API (redis-py) for testing purposes
License:        BSD-3-Clause
URL:            https://github.com/cunla/fakeredis-py
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core)
BuildRequires:  python3dist(sortedcontainers)
# Note: for python3-redis <= 4.2 ( so <= FC36) the aioredis features do not work
# as aioredis is required (which is not packaged in Fedora)
BuildRequires:  python3dist(redis)

%if %{with tests}
# Test dependencies:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  poetry
# Uses fixtures not present in previous versions
BuildRequires:  python3dist(pytest-asyncio) >= 0.19
BuildRequires:  python3dist(flaky)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(pytest-trio)
%endif


%global _description %{expand:
Fake implementation of redis API (redis-py) for testing purposes}

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -p 1 -n %{srcname}-py-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files fakeredis


%check
%if %{with tests}
# Run self-tests without a real Redis instance, as that makes
# depdendencies much more extended and requires a real Redis server
# running and listening.
export PYTHONPATH=%{buildroot}/%{python3_sitelib}
poetry run pytest -m fake
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md REDIS_COMMANDS.md CODE_OF_CONDUCT.md
%license LICENSE


%changelog
* Tue Oct 25 2022 Federico Pellegrin <fede@evolware.org> - 1.9.4-1
- Init at 1.9.4
