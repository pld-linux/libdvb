Summary:	libdvb (formerly dvb-mpegtools)
Summary(pl):	libdvb (formalnie dvd-mpegtools)
Name:		libdvb
Version:	0.5.0
Release:	0.1
License:	GPL
Group:		Multimedia
######		Unknown group!
Source0:	http://www.metzlerbros.org/dvb/%{name}-%{version}.tar.gz
# Source0-md5:	220c81e0efbcfbb47dbc6f212f463318
Patch0:		%{name}-install.patch
URL:		http://www.metzlerbros.de/mbros/dvb/
#BuildRequires:	-
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvb (formerly dvb-mpegtools) contains three libraries with examples
for their usage. libdvb is a library for switching channels using the
Linux DVB API and keeping channel list for DVB-C, DVB-S and DVB-T.

%description -l pl
libdvb zawiera trzy biblioteki z przyk³adami ich u¿ycia. libdvb jest
biblioteka prze³aczaj±c± kana³y u¿ywaj±c linux DVB API, i trzynaj±ca
liste kana³ów dla DVB-C, DVB-S i DVB-T.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=$RPM_BUILD_ROOT\%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}*
%{_includedir}/*.h
