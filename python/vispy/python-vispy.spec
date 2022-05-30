%global srcname vispy

Name:           python-%{srcname}
Version:        0.10.0
Release:        1%{?dist}
Summary:        VisPy: interactive scientific visualization in Python
License:        BSD
URL:            https://github.com/vispy/vispy
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Patch0:         0001-Numpy_dependency.patch
BuildArch:      x86_64

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-Cython
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-setuptools_scm_git_archive
BuildRequires:  python3-freetype
BuildRequires:  python3-hsluv

%global _description %{expand:
VisPy is a high-performance interactive 2D/3D data visualization library. VisPy leverages the computational power of modern Graphics Processing Units (GPUs) through the OpenGL library to display very large datasets.}

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}


%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -p 1 -n %{srcname}-%{version}
# %patch -p1

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files vispy


%check


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CONTRIBUTING.md CHANGELOG.md
%license LICENSE.txt


%changelog
* Mon May 30 2022 Federico Pellegrin <fede@evolware.org> - 0.10.0-1
- First packaging of vispy
