Summary:	libdvb (formerly dvb-mpegtools)
Summary(pl.UTF-8):   libdvb (pakiet kiedyś znany jako dvd-mpegtools)
Name:		libdvb
Version:	0.5.5.1
Release:	2
License:	GPL
Group:		Applications/Multimedia
Source0:	http://www.metzlerbros.org/dvb/%{name}-%{version}.tar.gz
# Source0-md5:	47612d2f8a4d4dee746a166d8b7f6f77
Patch0:		%{name}-opt.patch
Patch1:		%{name}-libdir.patch
Patch2:		%{name}-gcc4.patch
URL:		http://www.metzlerbros.de/mbros/dvb/
BuildRequires:	libstdc++-devel
BuildRequires:	linux-libc-headers >= 7:2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvb (formerly dvb-mpegtools) contains three libraries with examples
for their usage. libdvb is a library for switching channels using the
Linux DVB API and keeping channel list for DVB-C, DVB-S and DVB-T.

%description -l pl.UTF-8
Pakiet libdvb (kiedyś znany jako dvb-mpegtools) zawiera trzy
biblioteki z przykładami ich użycia. libdvb jest biblioteką
przełączającą kanały używając API Linux DVB, i trzymająca
listę kanałów dla DVB-C, DVB-S i DVB-T.

%package devel
Summary:	Header files and static libdvb libraries
Summary(pl.UTF-8):   Pliki nagłówkowe i statyczne biblioteki libdvb
Group:		Development/Libraries
# static only for now - doesn't require base, no -static

%description devel
Header files and static libdvb libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe i statyczne biblioteki libdvb.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dvb-mpegtools/README
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%doc README
%{_libdir}/libdvb*.a
%{_includedir}/*.h*
