%define major 0
%define libname %mklibname mission-control-plugins %major
%define develname %mklibname -d mission-control-plugins
%define _disable_ld_no_undefined 1

Name:           telepathy-mission-control
Version:        5.14.0
Release:        5
Summary:        Telepathy component managing connection managers
Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            http://mission-control.sourceforge.net/
Source0:        http://telepathy.freedesktop.org/releases/telepathy-mission-control/%{name}-%{version}.tar.gz

BuildRequires: chrpath
BuildRequires: glib2.0-common
BuildRequires: python
BuildRequires: xsltproc
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(telepathy-glib) => 0.17.5

Requires:      telepathy-filesystem

%description
Mission Control, or MC, is a Telepathy component providing a way for "end-user"
applications to abstract some of the details of connection managers, to provide
a simple way to manipulate a bunch of connection managers at once, and to
remove the need to have in each program the account definitions
and credentials.

%package -n %{libname}
Summary: Run time library for telepathy-mission-control
Group:   System/Libraries
Obsoletes: %{_lib}missioncontrol5.4.0 < 5.6.0

%description -n %{libname}
Run time library for telepathy-mission-control

%package -n %{develname}
Summary: Development library for telepathy-mission-control
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}missioncontrol-devel < 5.6.0

%description -n %{develname}
Development library for telepathy-mission-control

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--enable-gnome-keyring=yes \
	--disable-static

%make

%install
%makeinstall_std

%files
%doc AUTHORS 
%{_bindir}/*
%{_datadir}/glib-2.0/schemas/im.telepathy.MissionControl.FromEmpathy.gschema.xml
%{_datadir}/dbus-1/services/*.service
%{_libexecdir}/mission-control-5
%{_mandir}/man1/*
%{_mandir}/man8/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_datadir}/gtk-doc/html/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*pc
