Name:    openvas-scanner
Version: 21.4.3
Release: 1%{?dist}
Summary: Open Vulnerability Assessment Scanner

License: GPLv3
Source0: https://github.com/greenbone/%{name}/archive/v%{version}.tar.gz
# download sources with spectool:
# spectool -g -R openvas-scanner.spec

BuildRequires: bison cmake doxygen gcc glib2-devel glibc-headers gnutls-devel
BuildRequires: gpgme-devel gvm-libs graphviz libgcrypt-devel libksba-devel
BuildRequires: libpcap-devel libssh-devel make net-snmp-devel

Requires: glib2 glibc gnutls gpgme gvm-libs libgcrypt libksba libpcap libssh
Requires: net-snmp redis

%description
Open Vulnerability Assessment Scanner - Scanner for Greenbone Vulnerability Management (GVM).

%prep
%setup -q

%build
mkdir build && \
cd build && \
CFLAGS='-O2 -g -pipe -Wall -Wno-error=maybe-uninitialized -Wno-error=stringop-truncation -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions -fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection' \
%cmake -DSYSCONFDIR=/etc -DLOCALSTATEDIR=/var -DOPENVAS_RUN_DIR=/var/run/gvm ..
%make_build

%install
cd build && %make_install

%files
/etc/openvas/openvas_log.conf
/usr/bin/greenbone-nvt-sync
/usr/bin/openvas-nasl
/usr/bin/openvas-nasl-lint
/usr/lib64/libopenvas_misc.so
/usr/lib64/libopenvas_misc.so.*
/usr/lib64/libopenvas_nasl.so
/usr/lib64/libopenvas_nasl.so.*
/usr/sbin/openvas
/usr/share/man/man1/openvas-nasl-lint.1.gz
/usr/share/man/man1/openvas-nasl.1.gz
/usr/share/man/man8/greenbone-nvt-sync.8.gz
/usr/share/man/man8/openvas.8.gz
/var/lib/openvas

%changelog
* Wed Dec 15 2021 BM
- updated for 21.4.3.
