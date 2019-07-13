#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : sphinxcontrib-websupport
Version  : 1.1.2
Release  : 29
URL      : https://files.pythonhosted.org/packages/e8/3d/b33240484f128c4fcbf7bb04837a9b93f8259d3fbcb8e521c7c6267a0da9/sphinxcontrib-websupport-1.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/e8/3d/b33240484f128c4fcbf7bb04837a9b93f8259d3fbcb8e521c7c6267a0da9/sphinxcontrib-websupport-1.1.2.tar.gz
Source99 : https://files.pythonhosted.org/packages/e8/3d/b33240484f128c4fcbf7bb04837a9b93f8259d3fbcb8e521c7c6267a0da9/sphinxcontrib-websupport-1.1.2.tar.gz.asc
Summary  : Sphinx API for Web Apps
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-websupport-license = %{version}-%{release}
Requires: sphinxcontrib-websupport-python = %{version}-%{release}
Requires: sphinxcontrib-websupport-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
===================================
===================================
This is the Sphinx documentation generator, see http://www.sphinx-doc.org/.

%package license
Summary: license components for the sphinxcontrib-websupport package.
Group: Default

%description license
license components for the sphinxcontrib-websupport package.


%package python
Summary: python components for the sphinxcontrib-websupport package.
Group: Default
Requires: sphinxcontrib-websupport-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-websupport package.


%package python3
Summary: python3 components for the sphinxcontrib-websupport package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sphinxcontrib-websupport package.


%prep
%setup -q -n sphinxcontrib-websupport-1.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559117351
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
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-websupport
cp LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-websupport/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-websupport/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
