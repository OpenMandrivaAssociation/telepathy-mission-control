
%define libname %mklibname missioncontrol 0
%define libname_devel %mklibname -d missioncontrol

Name:           telepathy-mission-control
Version:        4.67
Release:        %mkrel 2
Summary:        Telepathy component managing connection managers
Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            http://mission-control.sourceforge.net/
Source0:        %{name}-%{version}.tar.gz
# Debian/upstream patch
Patch0:		0003-Don-t-close-channels-on-dispose.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: pkgconfig
BuildRequires: glib2-devel
BuildRequires: dbus-glib-devel
BuildRequires: libtelepathy-devel
BuildRequires: chrpath
BuildRequires: libxslt-proc
BuildRequires: libGConf2-devel
BuildRequires: python
BuildRequires: libgnome-keyring-devel
Requires:      telepathy-filesystem

%description
Mission Control, or MC, is a Telepathy component providing a way for "end-user"
applications to abstract some of the details of connection managers, to provide
a simple way to manipulate a bunch of connection managers at once, and to
remove the need to have in each program the account definitions
and credentials.

%package -n %libname_devel
Summary: Development library for telepathy-mission-control
Requires:      %libname = %version
Group:         Development/C
Provides:      %{name}-devel
Obsoletes:	%libname-devel

%description -n %libname_devel
Development library for telepathy-mission-control

%package -n %libname
Summary: Run time library for telepathy-mission-control
Group:   System/Libraries
%description -n %libname
Run time library for telepathy-mission-control


%prep
%setup -q
%patch0 -p1 -b .dispose

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
chrpath -d $RPM_BUILD_ROOT/%{_bindir}/*
chrpath -d $RPM_BUILD_ROOT/%{_libdir}/*.so.0*
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS 
%{_bindir}/*
%{_datadir}/dbus-1/services/*.service
%{_libdir}/mission-control

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/*.so.0*
%{_libdir}/*.so.1*
%{_libdir}/*.so.5*

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %libname_devel
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*pc
