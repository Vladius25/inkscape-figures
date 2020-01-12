# Created by pyp2rpm-3.3.2
%global pypi_name inotify
%global my_name notpyinotify

Name:           python-%{my_name}
Version:        0.2.10
Release:        1%{?dist}
Summary:        An adapter to Linux kernel support for inotify directory-watching

License:        GPL 2
URL:            https://github.com/dsoprea/PyInotify
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(setuptools)

%description
Inotify functionality is available from the
Linux kernel and allows you to register one or more directories for watching,
and to simply block and wait for notification events.

%package -n     python3-%{my_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{my_name}}
 
Requires:       python3dist(nose)
%description -n python3-%{my_name}
Inotify functionality is available from the
Linux kernel and allows you to register one or more directories for watching,
and to simply block and wait for notification events.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{my_name}
%doc README.rst %{pypi_name}/resources/README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun Jan 12 2020 Vladius25 <vkorol2509@icloud.com> - 0.2.10-1
- Initial package.
