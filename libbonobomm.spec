Summary:	A C++ interface for the libbonobo
Summary(pl):	Interfejs C++ dla libbonobo
Name:		libbonobomm
Version:	1.3.7
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	98a835a9c5ceb6f807fbe8745d6a421f
Patch0:		%{name}-orbitcpp_1_3_8.patch
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	gtkmm-devel >= 2.2.8
BuildRequires:	libbonobo-devel >= 2.4.0
BuildRequires:	orbitcpp-devel >= 1.3.8
BuildRequires:	pkgconfig
Requires:	cpp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a C++ interface for libbonobo library.

%description -l pl
Ten pakiet dostarcza interfejs C++ dla biblioteki libbonobo.

%package devel
Summary:	libbonobomm header files, development documentation
Summary(pl):	Pliki nag³ówkowe libbonobomm, dokumentacja dla programistów
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtkmm-devel >= 2.2.8
Requires:	libbonobo-devel >= 2.4.0
Requires:	orbitcpp-devel >= 1.3.8

%description devel
Header files and development documentation for libbonobomm library.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja dla programistów dla biblioteki
libbonobomm.

%package static
Summary:	libbonobomm static libraries
Summary(pl):	Biblioteki statyczne libbonobomm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libbonobomm static libraries.

%description static -l pl
Biblioteki statyczne libbonobomm.

%prep
%setup -q
%patch0 -p1

%build
# exceptions and rtti are used in this package --misiek
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	--enable-static
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
%{_libdir}/gtkmm-*/proc/m4/*
%{_includedir}/libbonobomm-2.0
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
