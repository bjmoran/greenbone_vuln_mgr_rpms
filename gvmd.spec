Name:    gvmd
Version: 21.4.4
Release: 1%{?dist}
Summary: Greenbone Vulnerability Manager

License: GPLv3
Source0: https://github.com/greenbone/%{name}/archive/v%{version}.tar.gz
# download sources with spectool:
# spectool -g -R gvmd.spec

BuildRequires: cmake doxygen gcc make glib2-devel glibc-headers gnutls-devel
BuildRequires: gpgme-devel graphviz gvm-libs libical-devel libpq-devel
BuildRequires: libuuid-devel perl-XML-Twig postgresql-server-devel xmltoman
BuildRequires: zlib-devel

Requires: glib2 glibc gnutls gnutls-utils gpgme gvm-libs libical libpq libuuid
Requires: openvas-scanner postgresql-contrib postgresql-server zlib

%description
The Greenbone Vulnerability Manager is the central management service between security scanners and the user clients.

%prep
%setup -q

%build
sed -i 's|postgresql/||' src/sql_pg.c
mkdir build && \
cd build && \
CFLAGS='-O2 -g -pipe -Wall -Wno-error=maybe-uninitialized -Wno-error=stringop-truncation -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions -fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection' \
%cmake -DSYSCONFDIR=/etc -DDEFAULT_CONFIG_DIR=/etc/default -DLOGROTATE_DIR=/etc/logrotate.d -DLOCALSTATEDIR=/var -DGVM_RUN_DIR=/var/run/gvm ..
%make_build

%install
cd build && %make_install

%files
/etc/gvm/gvmd_log.conf
/etc/gvm/pwpolicy.conf
/etc/logrotate.d/gvmd
/lib/systemd/system/gvmd.service
/usr/bin/gvm-manage-certs
/usr/lib/libgvm-pg-server.so
/usr/lib/libgvm-pg-server.so.*
/usr/sbin/greenbone-certdata-sync
/usr/sbin/greenbone-feed-sync
/usr/sbin/greenbone-scapdata-sync
/usr/sbin/gvmd
/usr/share/doc/gvm/example-gvm-manage-certs.conf
/usr/share/doc/gvm/html/gmp.html
/usr/share/gvm/cert/cert_bund_getbyname.xsl
/usr/share/gvm/cert/dfn_cert_getbyname.xsl
/usr/share/gvm/gvm-lsc-deb-creator
/usr/share/gvm/gvm-lsc-exe-creator
/usr/share/gvm/gvm-lsc-rpm-creator
/usr/share/gvm/gvmd/*
/usr/share/gvm/scap/cpe_getbyname.xsl
/usr/share/gvm/scap/cve_getbyname.xsl
/usr/share/gvm/scap/ovaldef_getbyname.xsl
/usr/share/man/man1/gvm-manage-certs.1.gz
/usr/share/man/man8/greenbone-certdata-sync.8.gz
/usr/share/man/man8/greenbone-scapdata-sync.8.gz
/usr/share/man/man8/gvmd.8.gz
/var/lib/gvm/gvmd

%pre
#!/bin/bash
useradd gvm
usermod -aG redis gvm
echo "gvm ALL = NOPASSWD: /usr/sbin/gsad" >> /etc/sudoers.d/gvm
echo "gvm ALL = NOPASSWD: /usr/sbin/openvas" >> /etc/sudoers.d/gvm

%post
#!/bin/bash
mkdir -p /var/log/gvm
chown -R gvm: /var/lib/gvm /var/log/gvm
if [ ! -f "/var/lib/pgsql/data/postgresql.conf" ]
then
	su - postgres -c initdb
fi
systemctl enable postgresql
systemctl start postgresql
export PGUSER=postgres
createuser -DRS gvm
createdb -O gvm gvmd
psql -d gvmd -c 'create role dba with superuser noinherit;'
psql -d gvmd -c 'grant dba to gvm;'
psql -d gvmd -c 'create extension "uuid-ossp";'
psql -d gvmd -c 'create extension "pgcrypto";'

%changelog
* Wed Dec 15 2021 BM
- updated for 21.4.4.
- patch for systemd unit file no longer required
- /etc/default/gvmd no longer packaged
- systemd unit file now in /lib, rather than /usr/lib
- packaging scripts moved
