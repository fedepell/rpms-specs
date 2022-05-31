%global srcname meshio

Name:           python-%{srcname}
Version:        7.0.0
Release:        1%{?dist}
Summary:        input/output for many mesh formats
License:        MIT
URL:            https://github.com/nschloe/meshio
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-rich

%global _description %{expand:
There are various mesh formats available for representing unstructured meshes. meshio can read and write all of the following and smoothly converts between them:
Abaqus (.inp), ANSYS msh (.msh), AVS-UCD (.avs), CGNS (.cgns), DOLFIN XML (.xml), Exodus (.e, .exo), FLAC3D (.f3grid), H5M (.h5m), Kratos/MDPA (.mdpa), Medit (.mesh, .meshb), MED/Salome (.med), Nastran (bulk data, .bdf, .fem, .nas), Netgen (.vol, .vol.gz), Neuroglancer precomputed format, Gmsh (format versions 2.2, 4.0, and 4.1, .msh), OBJ (.obj), OFF (.off), PERMAS (.post, .post.gz, .dato, .dato.gz), PLY (.ply), STL (.stl), Tecplot .dat, TetGen .node/.ele, SVG (2D output only) (.svg), SU2 (.su2), UGRID (.ugrid), VTK (.vtk), VTU (.vtu), WKT (TIN) (.wkt), XDMF (.xdmf, .xmf).
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
%pyproject_save_files meshio

%check
# %{python3} setup.py test


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_bindir}/meshio
%{_datadir}/paraview-5.9/plugins/*


%changelog
* Mon May 30 2022 Federico Pellegrin <fede@evolware.org> - 7.0.0-1
- First packaging of python-meshio
