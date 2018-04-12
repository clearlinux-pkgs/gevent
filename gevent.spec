#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gevent
Version  : 1.2.2
Release  : 15
URL      : https://pypi.debian.net/gevent/gevent-1.2.2.tar.gz
Source0  : https://pypi.debian.net/gevent/gevent-1.2.2.tar.gz
Summary  : Coroutine-based network library
Group    : Development/Tools
License  : BSD-2-Clause MIT Python-2.0
Requires: gevent-python3
Requires: gevent-python
Requires: greenlet
BuildRequires : Cython
BuildRequires : greenlet
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
gevent
        ========
        
        gevent_ is a coroutine-based Python networking library.

%package python
Summary: python components for the gevent package.
Group: Default
Requires: gevent-python3

%description python
python components for the gevent package.


%package python3
Summary: python3 components for the gevent package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gevent package.


%prep
%setup -q -n gevent-1.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523558364
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
