Name:    gsa
Version: 20.8.0
Release: 1%{?dist}
Summary: Greenbone Security Assistant

License: GPLv3
Source0: https://github.com/greenbone/%{name}/archive/v%{version}.tar.gz
Patch0: gsad-configs.patch

BuildRequires: cmake doxygen gcc gcc-c++ glib2-devel glibc-headers gnutls-devel
BuildRequires: graphviz gvm-libs libgcrypt-devel libmicrohttpd-devel
BuildRequires: libuuid-devel libxml2-devel make nodejs xmltoman yarn zlib-devel

Requires: glib2 glibc gnutls gvm-libs gvmd libgcrypt libmicrohttpd libuuid
Requires: libxml2 nodejs zlib

%description
The Greenbone Security Assistant is the web interface for the Greenbone Security Manager appliances.

%prep
%setup -q
%patch0 -p1

%build
mkdir build && \
cd build && \
CFLAGS='-O2 -g -pipe -Wall -Wno-error=maybe-uninitialized -Wno-error=stringop-truncation -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions -fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection' \
%cmake -DSYSCONFDIR=/etc -DDEFAULT_CONFIG_DIR=/etc/default -DLOGROTATE_DIR=/etc/logrotate.d -DLOCALSTATEDIR=/var -DGVM_RUN_DIR=/var/run/gvm ..
%make_build

%install
cd build && %make_install

%files
/etc/default/gsad
/etc/gvm/gsad_log.conf
/etc/logrotate.d/gsad
/usr/lib/systemd/system/gsad.service
/usr/sbin/gsad
/usr/share/gvm/gsad/web/*
/usr/share/man/man8/gsad.8.gz

%changelog
