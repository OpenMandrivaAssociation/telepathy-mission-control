%define major 0
%define libname %mklibname mission-control-plugins %major
%define libname_devel %mklibname -d mission-control-plugins

Name:           telepathy-mission-control
Version:        5.7.11
Release:        %mkrel 1
Summary:        Telepathy component managing connection managers
Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            http://mission-control.sourceforge.net/
Source0:        http://telepathy.freedesktop.org/releases/telepathy-mission-control/%{name}-%{version}.tar.gz
Patch0: telepathy-mission-control-5.7.11-fix-linking.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: dbus-glib-devel
BuildRequires: libtelepathy-glib-devel
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
Provides:      %{name}-devel = %version-%release
Obsoletes:     %{_lib}missioncontrol-devel < 5.6.0

%description -n %libname_devel
Development library for telepathy-mission-control

%package -n %libname
Summary: Run time library for telepathy-mission-control
Group:   System/Libraries
Obsoletes: %{_lib}missioncontrol5.4.0 < 5.6.0

%description -n %libname
Run time library for telepathy-mission-control

%prep
%setup -q
%apply_patches
autoreconf

%build
%configure2_5x --enable-gnome-keyring=yes --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS 
%{_bindir}/*
%{_datadir}/dbus-1/services/*.service
%{_libexecdir}/mission-control-5
%_mandir/man1/*
%_mandir/man8/*

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/*.so.%{major}*

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %libname_devel
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*pc
