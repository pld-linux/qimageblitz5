Summary:	Blitz Qt 5 image filter library
Summary(pl.UTF-8):	Biblioteka filtrów obrazu Blitz dla Qt 5
Name:		qimageblitz5
Version:	0.0.6
%define	snap	20131029
%define	rel	1
Release:	1.%{snap}.%{rel}
License:	BSD
Group:		X11/Libraries
Source0:	https://dev.gentoo.org/~asturm/distfiles/qimageblitz-%{version}_p%{snap}.tar.xz
# Source0-md5:	98e14003f2a7f2a4d83442c401ab6780
Patch0:		%{name}-noexecstack.patch
Patch1:		%{name}-suffix.patch
URL:		http://sourceforge.net/projects/qimageblitz/
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	cmake >= 2.6.4
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blitz is a graphical effect and filter library for Qt 5 that contains
many improvements over KDE 3.x's kdefx library including bugfixes,
memory and speed improvements, and MMX/SSE support.

%description -l pl.UTF-8
Blitz to biblioteka efektów i filtrów graficznych dla Qt 5
zawierająca wiele ulepszeń w stosunku do biblioteki kdefx z KDE 3.x, w
tym poprawki błędów, poprawę wydajności (pod względem wykorzystania
pamięci i szybkości działania) oraz obsługę MMX/SSE.

%package devel
Summary:	Header files for Blitz library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Blitz
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Gui-devel >= 5

%description devel
Header files needed for build programs that use qimageblitz.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do tworzenia programów z użyciem
qimageblitz.

%prep
%setup -q -n qimageblitz-%{version}_p%{snap}
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake .. \
	-DQT4_BUILD=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_bindir}/blitztest{,5}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING Changelog README.BLITZ
%attr(755,root,root) %{_bindir}/blitztest5
%attr(755,root,root) %{_libdir}/libqimageblitz5.so.5.0.0
%attr(755,root,root) %ghost %{_libdir}/libqimageblitz5.so.5

%files devel
%defattr(644,root,root,755)
%doc README.PORTING
%attr(755,root,root) %{_libdir}/libqimageblitz5.so
%dir %{_includedir}/qimageblitz5
%{_includedir}/qimageblitz5/blitzcpu.h
%{_includedir}/qimageblitz5/qimageblitz.h
%{_includedir}/qimageblitz5/qimageblitz_export.h
%{_pkgconfigdir}/qimageblitz5.pc
