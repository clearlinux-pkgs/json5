#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : json5
Version  : 0.9.5
Release  : 12
URL      : https://files.pythonhosted.org/packages/8d/b4/d09c00cb7bc88b17118be48f94d4b8d0ce7b572690625ca2b5477e05ce0e/json5-0.9.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/8d/b4/d09c00cb7bc88b17118be48f94d4b8d0ce7b572690625ca2b5477e05ce0e/json5-0.9.5.tar.gz
Summary  : A Python implementation of the JSON5 data format.
Group    : Development/Tools
License  : Apache-2.0
Requires: json5-bin = %{version}-%{release}
Requires: json5-license = %{version}-%{release}
Requires: json5-python = %{version}-%{release}
Requires: json5-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
A Python implementation of the JSON5 data format.

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
Provides: pypi(json5)

%description python3
python3 components for the json5 package.


%prep
%setup -q -n json5-0.9.5
cd %{_builddir}/json5-0.9.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590678205
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/json5
cp %{_builddir}/json5-0.9.5/LICENSE %{buildroot}/usr/share/package-licenses/json5/c700a8b9312d24bdc57570f7d6a131cf63d89016
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
