#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : json5
Version  : 0.9.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/96/fb/81f0ea3722a5cc379de7d1091e29a5eb6101c97c5040985634eabbe74ec5/json5-0.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/96/fb/81f0ea3722a5cc379de7d1091e29a5eb6101c97c5040985634eabbe74ec5/json5-0.9.0.tar.gz
Summary  : A Python implementation of the JSON5 data format.
Group    : Development/Tools
License  : Apache-2.0
Requires: json5-bin = %{version}-%{release}
Requires: json5-license = %{version}-%{release}
Requires: json5-python = %{version}-%{release}
Requires: json5-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# pyjson5
A Python implementation of the JSON5 data format.
[JSON5](https://json5.org) extends the
[JSON](http://www.json.org) data interchange format to make it
slightly more usable as a configuration language:

%package bin
Summary: bin components for the json5 package.
Group: Binaries
Requires: json5-license = %{version}-%{release}

%description bin
bin components for the json5 package.


%package license
Summary: license components for the json5 package.
Group: Default

%description license
license components for the json5 package.


%package python
Summary: python components for the json5 package.
Group: Default
Requires: json5-python3 = %{version}-%{release}

%description python
python components for the json5 package.


%package python3
Summary: python3 components for the json5 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the json5 package.


%prep
%setup -q -n json5-0.9.0
cd %{_builddir}/json5-0.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580491763
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/json5
cp %{_builddir}/json5-0.9.0/LICENSE %{buildroot}/usr/share/package-licenses/json5/c700a8b9312d24bdc57570f7d6a131cf63d89016
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3*/site-packages/README.md
rm -f %{buildroot}/usr/lib/python3*/site-packages/tests/__init__.py
rm -f %{buildroot}/usr/lib/python3*/site-packages/tests/__pycache__/__init__.cpython-3*.pyc
rm -f %{buildroot}/usr/lib/python3*/site-packages/tests/__pycache__/host_fake.cpython-3*.pyc
rm -f %{buildroot}/usr/lib/python3*/site-packages/tests/__pycache__/host_test.cpython-3*.pyc
rm -f %{buildroot}/usr/lib/python3*/site-packages/tests/__pycache__/lib_test.cpython-3*.pyc
rm -f %{buildroot}/usr/lib/python3*/site-packages/tests/__pycache__/tool_test.cpython-3*.pyc
rm -f %{buildroot}/usr/lib/python3*/site-packages/tests/host_fake.py
rm -f %{buildroot}/usr/lib/python3*/site-packages/tests/host_test.py
rm -f %{buildroot}/usr/lib/python3*/site-packages/tests/lib_test.py
rm -f %{buildroot}/usr/lib/python3*/site-packages/tests/tool_test.py

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyjson5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/json5/c700a8b9312d24bdc57570f7d6a131cf63d89016

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
