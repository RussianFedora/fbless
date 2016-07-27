Name:           fbless
Version:        0.2.3
Release:        1%{?dist}
Summary:        Console FB2 reader

License:        GPLv2+
URL:            https://github.com/matimatik/fbless
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       ncurses

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup

%build
%py2_build

%install
%py2_install

%files
%license LICENSE
%doc AUTHORS Changelog README TODO
%{_bindir}/%{name}
%{python2_sitelib}/%{name}-%version-py%{python2_version}.egg-info/
%{python2_sitelib}/%{name}_lib/

%changelog
* Wed Jul 20 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.2.3-1
- Initial packaging
