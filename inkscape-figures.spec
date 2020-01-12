%global pypi_name inkscape-figures

Name:           python-%{pypi_name}
Version:        1.0.4
Release:        4%{?dist}
Summary:        Script for managing inkscape figures

License:        MIT
URL:            https://github.com/gillescastel/inkscape-figures
Source0:        https://github.com/Vladius25/%{pypi_name}/archive/v%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Inkscape figure manager. A script I use to manage figures for my LaTeX
documents.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3.7dist(appdirs)
Requires:       python3.7dist(click)
Requires:       python3.7dist(daemonize)
Requires:       python3-notpyinotify
%{?python_disable_dependency_generator}
%description -n python3-%{pypi_name}
Inkscape figure manager. A script I use to manage figures for my LaTeX
documents. 

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/inkscape-figures
%{python3_sitelib}/inkscapefigures
%{python3_sitelib}/inkscape_figures-%{version}-py?.?.egg-info

%changelog
* Sun Jan 13 2020 vladius25 <vkorol2509@icloud.com> - 1.0.4-4
- Change source to own fork.
* Sun Jan 12 2020 vladius25 <vkorol2509@icloud.com> - 1.0.4-3
- Fix description and dependecy.
* Sun Jan 12 2020 vladius25 <vkorol2509@icloud.com> - 1.0.4-2
- Fix inotify to pyinotify.
* Sun Jan 12 2020 Vladius25 <vkorol2509@icloud.com> - 1.0.4-1
- Initial package.
