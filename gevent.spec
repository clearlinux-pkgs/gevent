#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gevent
Version  : 1.4.0
Release  : 30
URL      : https://files.pythonhosted.org/packages/ed/27/6c49b70808f569b66ec7fac2e78f076e9b204db9cf5768740cff3d5a07ae/gevent-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ed/27/6c49b70808f569b66ec7fac2e78f076e9b204db9cf5768740cff3d5a07ae/gevent-1.4.0.tar.gz
Summary  : Coroutine-based network library
Group    : Development/Tools
License  : BSD-2-Clause CC-BY-4.0 MIT Python-2.0
Requires: gevent-license = %{version}-%{release}
Requires: gevent-python = %{version}-%{release}
Requires: gevent-python3 = %{version}-%{release}
Requires: cffi
Requires: dnspython
Requires: greenlet
Requires: idna
BuildRequires : Cython
BuildRequires : buildreq-distutils3

%description
## Overview
libuv is a multi-platform support library with a focus on asynchronous I/O. It
was primarily developed for use by [Node.js][], but it's also
used by [Luvit](http://luvit.io/), [Julia](http://julialang.org/),
[pyuv](https://github.com/saghul/pyuv), and [others](https://github.com/libuv/libuv/wiki/Projects-that-use-libuv).

%package license
Summary: license components for the gevent package.
Group: Default

%description license
license components for the gevent package.


%package python
Summary: python components for the gevent package.
Group: Default
Requires: gevent-python3 = %{version}-%{release}

%description python
python components for the gevent package.


%package python3
Summary: python3 components for the gevent package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gevent package.


%prep
%setup -q -n gevent-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546658193
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gevent
cp LICENSE %{buildroot}/usr/share/package-licenses/gevent/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/gevent/NOTICE
cp deps/c-ares/LICENSE.md %{buildroot}/usr/share/package-licenses/gevent/deps_c-ares_LICENSE.md
cp deps/libev/LICENSE %{buildroot}/usr/share/package-licenses/gevent/deps_libev_LICENSE
cp deps/libuv/LICENSE %{buildroot}/usr/share/package-licenses/gevent/deps_libuv_LICENSE
cp deps/libuv/LICENSE-docs %{buildroot}/usr/share/package-licenses/gevent/deps_libuv_LICENSE-docs
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gevent/LICENSE
/usr/share/package-licenses/gevent/NOTICE
/usr/share/package-licenses/gevent/deps_c-ares_LICENSE.md
/usr/share/package-licenses/gevent/deps_libev_LICENSE
/usr/share/package-licenses/gevent/deps_libuv_LICENSE
/usr/share/package-licenses/gevent/deps_libuv_LICENSE-docs

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
