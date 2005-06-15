# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	A C++ interface for the libbonobo
Summary(pl):	Interfejs C++ dla libbonobo
Name:		libbonobomm
Version:	1.3.8
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libbonobomm/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	b464048a99191e0ce3ad8504f460731f
Patch0:		%{name}-gtkmm24.patch
Patch1:		%{name}-gcc34.patch
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibmm-devel >= 2.4.0
BuildRequires:	libbonobo-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	orbitcpp-devel >= 1.3.9
BuildRequires:	pkgconfig
Requires:	cpp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a C++ interface for libbonobo library.

%description -l pl
Ten pakiet dostarcza interfejs C++ dla biblioteki libbonobo.

%package devel
Summary:	Header files for libbonobomm library
Summary(pl):	Pliki nag³ówkowe biblioteki libbonobomm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.4.0
Requires:	libbonobo-devel >= 2.4.0
Requires:	orbitcpp-devel >= 1.3.9

%description devel
Header files for libbonobomm library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libbonobomm.

%package static
Summary:	libbonobomm static libraries
Summary(pl):	Biblioteki statyczne libbonobomm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libbonobomm static libraries.

%description static -l pl
Biblioteki statyczne libbonobomm.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# exceptions and rtti are used in this package --misiek
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	--enable-static \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/libbonobomm-*
%{_libdir}/glibmm-*/proc/m4/*
%{_includedir}/libbonobomm-2.0
%{_pkgconfigdir}/*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
