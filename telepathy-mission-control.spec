
%define libname %mklibname missioncontrol 0
%define libname_devel %mklibname -d missioncontrol 0

Name:           telepathy-mission-control
Version:        4.22
Release:        %mkrel 1
Summary:        TODO
Group:          Networking/Instant messaging
License:        LGPL
URL:            http://mission-control.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
# stolen from debian, related to 
# http://sourceforge.net/tracker/index.php?func=detail&aid=1718949&group_id=190214&atid=932444
Patch0:         00_size_t_vs_guint.patch 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
# TODO
BuildRequires: pkgconfig
BuildRequires: glib2-devel
BuildRequires: dbus-glib-devel
BuildRequires: libtelepathy-devel
BuildRequires: chrpath
BuildRequires: libxslt-proc
Requires:	telepathy-filesystem

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
%description -n %libname_devel
Development library for telepathy-mission-control

%package -n %libname
Summary: Run time library for telepathy-mission-control
Group:   System/Libraries
%description -n %libname
Run time library for telepathy-mission-control


%prep
%setup -q
%patch -p0

%build
%configure 
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
%doc AUTHORS README INSTALL COPYING NEWS
%{_bindir}/*
%{_datadir}/dbus-1/services/*.service

%files -n %libname 
%defattr(-,root,root,-)
%{_libdir}/*.so.0*

%post -n %{libname}
/sbin/ldconfig

%postun -n %{libname}
/sbin/ldconfig

%files -n %libname_devel 
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*pc
