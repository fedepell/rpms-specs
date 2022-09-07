%global srcname doxypypy
# Note: package has no tags/releases, not nice!
%global commit a739b1289bbba7bd56caeb7b06d9b7f1883c0a3b
%global gittag master

Name:           python-%{srcname}
Version:        0.8.8.6
Release:        1%{?dist}
Summary:        A more Pythonic version of doxypy, a Doxygen filter for Python.
License:        GPL-2.0
URL:            https://github.com/Feneric/doxypypy
Source0:        %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# Needed for testing
BuildRequires:  python3dist(pytest)

%global _description %{expand:
A more Pythonic version of doxypy, a Doxygen filter for Python.
}

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}


%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -p 1 -n %{srcname}-%{commit}
# These test files fail to bytecompile as they contain \x00 chars
rm -rf doxypypy/test/sample_utf*ebom.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files doxypypy


%check
# Exclude the tests for which we removed the files, see above
%{pytest} -k 'not test_utf16be_bom and not test_utf16le_bom and not test_utf32be_bom and not test_utf32le_bom'


%files -n python3-%{srcname} -f %{pyproject_files}
%doc *.rst
%license LICENSE.txt
%{_bindir}/doxypypy


%changelog
* Wed Sep 7 2022 Federico Pellegrin <fede@evolware.org> - 0.8.8.6-1
- First packaging of python-doxypypy
