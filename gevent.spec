#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gevent
Version  : 21.1.2
Release  : 56
URL      : https://files.pythonhosted.org/packages/0b/50/1b1175ea3a269b5fa3f0f7fed11149888180695bef5fbf568adbb196efaf/gevent-21.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/0b/50/1b1175ea3a269b5fa3f0f7fed11149888180695bef5fbf568adbb196efaf/gevent-21.1.2.tar.gz
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
Requires: setuptools
Requires: zope.event
Requires: zope.interface
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : dnspython
BuildRequires : greenlet
BuildRequires : idna
BuildRequires : setuptools
BuildRequires : zope.event
BuildRequires : zope.interface

%description
gevent
        ========

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
Provides: pypi(gevent)
Requires: pypi(greenlet)
Requires: pypi(setuptools)
Requires: pypi(zope.event)
Requires: pypi(zope.interface)

%description python3
python3 components for the gevent package.


%prep
%setup -q -n gevent-21.1.2
cd %{_builddir}/gevent-21.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611425192
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gevent
cp %{_builddir}/gevent-21.1.2/LICENSE %{buildroot}/usr/share/package-licenses/gevent/e390b2ea7c66d8859ed575dcad84522b804123ae
cp %{_builddir}/gevent-21.1.2/NOTICE %{buildroot}/usr/share/package-licenses/gevent/c3c1f290cd381675b69efce2eee3c2ce03d398d8
cp %{_builddir}/gevent-21.1.2/deps/c-ares/LICENSE.md %{buildroot}/usr/share/package-licenses/gevent/e9c597f9b6cf935773ee731d4170b0c2ba142dbb
cp %{_builddir}/gevent-21.1.2/deps/libev/LICENSE %{buildroot}/usr/share/package-licenses/gevent/10e633ee2e9f8a961554d0d579f03a1d0755ff3b
cp %{_builddir}/gevent-21.1.2/deps/libuv/LICENSE %{buildroot}/usr/share/package-licenses/gevent/848f7398f89046426a7ba23cb56cd3c93c030c64
cp %{_builddir}/gevent-21.1.2/deps/libuv/LICENSE-docs %{buildroot}/usr/share/package-licenses/gevent/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gevent/10e633ee2e9f8a961554d0d579f03a1d0755ff3b
/usr/share/package-licenses/gevent/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb
/usr/share/package-licenses/gevent/848f7398f89046426a7ba23cb56cd3c93c030c64
/usr/share/package-licenses/gevent/c3c1f290cd381675b69efce2eee3c2ce03d398d8
/usr/share/package-licenses/gevent/e390b2ea7c66d8859ed575dcad84522b804123ae
/usr/share/package-licenses/gevent/e9c597f9b6cf935773ee731d4170b0c2ba142dbb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
