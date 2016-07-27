Name:           fbless
Version:        0.2.3
Release:        1%{?dist}
Summary:        Console FB2 reader

License:        GPLv2+
URL:            https://github.com/matimatik/fbless
Source0:        https://github.com/matimatik/%{name}/archive/%{version}.tar.gz

BuildRequires:  python2-setuptools
BuildRequires:  python2-rpm-macros
Requires:       ncurses

BuildArch:      noarch

%description
Simple console FB2 reader.

%prep
%autosetup


%build
#nothing to build


%install
%{__python2} setup.py install --root=%{buildroot}


%files
%license LICENSE
%doc AUTHORS Changelog README TODO
%{_bindir}/%{name}
%{python2_sitelib}/%{name}-%version-py%{python2_version}.egg-info
%{python2_sitelib}/%{name}_lib


%changelog
* Wed Jul 20 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.2.3-1
- Initial packaging
