%include        /usr/lib/rpm/macros.perl
Summary:	A C++ interface for the libbonobo
Summary(pl):	Wrapper C++ dla libbonobo
Name:		libbonobomm
Version:	1.3.3
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://switch.dl.sourceforge.net/sourceforge/gtkmm/%{name}-%{version}.tar.gz
URL:		http://gtkmm.sourceforge.net/
Requires:	cpp
BuildRequires:	autoconf
BuildRequires:	gtkmm-devel >= 2.0.0
BuildRequires:	ORBit2-devel >= 2.0.0
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRequires:	orbitcpp >= 1.3.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a C++ interface for libbonobo library.

%description -l pl
Ten pakiet dostarcza interface C++ dla biblioteki libbonobo.

%package devel
Summary:	libbonobomm header files, development documentation
Summary(pl):	Pliki nag³ówkowe libbonobomm, dokumentacja dla programistów
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

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

%build
# exceptions and rtti are used in this package --misiek
%configure \
	--enable-static=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%dir %{_libdir}/libbonobomm-*
%dir %{_libdir}/gtkmm-*/proc

%{_libdir}/libbonobomm-*/include
%{_libdir}/gtkmm-*/proc/m4

%{_pkgconfigdir}/*.pc
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
