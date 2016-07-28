Name:           fbless
Version:        0.2.3
Release:        1%{?dist}
Summary:        Console FB2 reader

License:        GPLv2+
URL:            https://github.com/matimatik/fbless
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python2-devel
Requires:       ncurses

BuildArch:      noarch

%description
Curses based FictionBook2 viewer.

%prep
%autosetup
#https://github.com/matimatik/fbless/pull/29
sed -ier "s|os.path.expanduser(\"~/.fblessrc\"),|'/etc/fblessrc',\n    os.path.expanduser(\"~/.fblessrc\"),|" fbless_lib/options.py

%build
%py2_build

%install
%py2_install
mkdir %{buildroot}%{_sysconfdir}
install -m 644 fblessrc.example %{buildroot}%{_sysconfdir}/fblessrc

%files
%license LICENSE
%doc AUTHORS Changelog README TODO
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/fblessrc
%{python2_sitelib}/%{name}-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/%{name}_lib/

%changelog
* Wed Jul 20 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.2.3-1
- Initial packaging
