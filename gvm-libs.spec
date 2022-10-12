Name:    gvm-libs
Version: 21.4.4
Release: 1%{?dist}
Summary: GVM Libraries

License: GPLv3
Source0: https://github.com/greenbone/%{name}/archive/v%{version}.tar.gz
# download sources with spectool:
# spectool -g -R gvm-libs.spec

BuildRequires: cmake doxygen gcc glib2-devel glibc-headers gnutls-devel
BuildRequires: gpgme-devel graphviz hiredis-devel libgcrypt-devel
BuildRequires: libnet-devel libpcap-devel libssh-devel libuuid-devel
BuildRequires: libxml2-devel make openldap-devel radcli-devel zlib-devel

Requires: cyrus-sasl glib2 glibc gnutls gpgme hiredis libgcrypt libnet
Requires: libpcap libssh libuuid libxml2 openldap radcli zlib

%description
GVM Libraries.

%prep
%setup -q

%build
mkdir build && \
cd build && \
CFLAGS='-O2 -g -pipe -Wall -Wno-error=maybe-uninitialized -Wno-error=stringop-truncation -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions -fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection' \
%cmake -DSYSCONFDIR=/etc -DLOCALSTATEDIR=/var ..
%make_build

%install
cd build && %make_install

%files
/usr/include/gvm/base/array.h
/usr/include/gvm/base/credentials.h
/usr/include/gvm/base/cvss.h
/usr/include/gvm/base/drop_privileges.h
/usr/include/gvm/base/hosts.h
/usr/include/gvm/base/logging.h
/usr/include/gvm/base/networking.h
/usr/include/gvm/base/nvti.h
/usr/include/gvm/base/pidfile.h
/usr/include/gvm/base/prefs.h
/usr/include/gvm/base/proctitle.h
/usr/include/gvm/base/pwpolicy.h
/usr/include/gvm/base/settings.h
/usr/include/gvm/base/strings.h
/usr/include/gvm/base/version.h
/usr/include/gvm/boreas/alivedetection.h
/usr/include/gvm/boreas/arp.h
/usr/include/gvm/boreas/boreas_error.h
/usr/include/gvm/boreas/boreas_io.h
/usr/include/gvm/boreas/cli.h
/usr/include/gvm/boreas/ping.h
/usr/include/gvm/boreas/sniffer.h
/usr/include/gvm/boreas/util.h
/usr/include/gvm/gmp/gmp.h
/usr/include/gvm/osp/osp.h
/usr/include/gvm/util/authutils.h
/usr/include/gvm/util/compressutils.h
/usr/include/gvm/util/fileutils.h
/usr/include/gvm/util/gpgmeutils.h
/usr/include/gvm/util/kb.h
/usr/include/gvm/util/ldaputils.h
/usr/include/gvm/util/nvticache.h
/usr/include/gvm/util/passwordbasedauthentication.h
/usr/include/gvm/util/radiusutils.h
/usr/include/gvm/util/serverutils.h
/usr/include/gvm/util/sshutils.h
/usr/include/gvm/util/uuidutils.h
/usr/include/gvm/util/xmlutils.h
/usr/lib64/libgvm_base.so
/usr/lib64/libgvm_base.so.*
/usr/lib64/libgvm_boreas.so
/usr/lib64/libgvm_boreas.so.*
/usr/lib64/libgvm_gmp.so
/usr/lib64/libgvm_gmp.so.*
/usr/lib64/libgvm_osp.so
/usr/lib64/libgvm_osp.so.*
/usr/lib64/libgvm_util.so
/usr/lib64/libgvm_util.so.*
/usr/lib64/pkgconfig/libgvm_base.pc
/usr/lib64/pkgconfig/libgvm_boreas.pc
/usr/lib64/pkgconfig/libgvm_gmp.pc
/usr/lib64/pkgconfig/libgvm_osp.pc
/usr/lib64/pkgconfig/libgvm_util.pc

%changelog
* Thu Apr 07 2022 BM
- updated for 21.4.4.

* Wed Dec 15 2021 BM
- updated for 21.4.3.
- now requires libnet-devel.
- two additional header files installed.
