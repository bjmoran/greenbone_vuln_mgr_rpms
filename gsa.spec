Name:    gsa
Version: 21.4.4
Release: 1%{?dist}
Summary: Greenbone Security Assistant Daemon Web Content

License: GPLv3
Source0: https://github.com/greenbone/%{name}/archive/v%{version}.tar.gz
# download sources with spectool:
# spectool -g -R gsa.spec

BuildRequires: nodejs yarn

Requires: gsad nodejs

%description
Web Content for the Greenbone Security Assistant Daemon (gsad).

%global debug_package %{nil}

%prep
%setup -q

%build
yarn
yarn build

%install
mkdir -p %{buildroot}/usr/share/gvm/gsad/web
cp -a build/* %{buildroot}/usr/share/gvm/gsad/web

%files
/usr/share/gvm/gsad/web

%changelog
* Wed Oct 12 2022 BM
- Initial version.
