#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clinfo
Version  : 3.0.20.11.20
Release  : 15
URL      : https://github.com/Oblomov/clinfo/archive/3.0.20.11.20/clinfo-3.0.20.11.20.tar.gz
Source0  : https://github.com/Oblomov/clinfo/archive/3.0.20.11.20/clinfo-3.0.20.11.20.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 Public-Domain
Requires: clinfo-bin = %{version}-%{release}
Requires: clinfo-license = %{version}-%{release}
BuildRequires : opencl-headers-dev
BuildRequires : pkgconfig(OpenCL)
Patch1: build.patch

%description
# What is this?
clinfo is a simple command-line application that enumerates all possible
(known) properties of the OpenCL platform and devices available on the
system.

%package bin
Summary: bin components for the clinfo package.
Group: Binaries
Requires: clinfo-license = %{version}-%{release}

%description bin
bin components for the clinfo package.


%package license
Summary: license components for the clinfo package.
Group: Default

%description license
license components for the clinfo package.


%prep
%setup -q -n clinfo-3.0.20.11.20
cd %{_builddir}/clinfo-3.0.20.11.20
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605901384
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1605901384
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clinfo
cp %{_builddir}/clinfo-3.0.20.11.20/LICENSE %{buildroot}/usr/share/package-licenses/clinfo/5447aca2f62e3ba417ad9ba64f6567d7fbac8ace
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clinfo

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clinfo/5447aca2f62e3ba417ad9ba64f6567d7fbac8ace
