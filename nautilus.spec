Summary:	nautilus - gnome shell and file manager
Summary(pl):	nautilus - pow³oka gnome i menad¿er plików
Name:		nautilus
Version:	1.0.1.1
Release:	1
License:	GPL
Group:		Utilities/File
Group(pl):	Narzêdzia/Pliki
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-time.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-gettext.patch
Patch3:		%{name}-m4-gnome.patch
URL:		http://nautilus.eazel.com/
BuildRequires:	perl
BuildRequires:	esound-devel >= 0.2.7
BuildRequires:	ORBit-devel >= 0.5.1
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	pam-devel
BuildRequires:	mozilla-devel >= 0.8
BuildRequires:	bzip2-devel
BuildRequires:	glib-devel >= 1.2.9
BuildRequires:	gtk+-devel >= 1.2.9
BuildRequires:	gnome-libs-devel >= 1.2.11
BuildRequires:	bonobo-devel >= 0.37
BuildRequires:	gnome-vfs-devel >= 1.0
BuildRequires:	control-center-devel >= 1.3
BuildRequires:	oaf-devel >= 0.6.5
BuildRequires:	GConf-devel >= 0.12
BuildRequires:	gnome-http-devel
BuildRequires:	gdk-pixbuf-devel >= 0.10.0
BuildRequires:	zlib-devel >= 1.0.3
BuildRequires:	libpng-devel
BuildRequires:	medusa-devel >= 0.5.0
BuildRequires:	gettext-devel
BuildRequires:	XFree86-devel
BuildRequires:	rpm-devel >= 4.0.2
BuildRequires:	db1-devel
BuildRequires:	db3-devel
BuildRequires:	ammonite-devel >= 1.0.0
BuildRequires:	libxml-devel
BuildRequires:	automake
BuildRequires:	autoconf
# TODO: conditional build
# BuildRequires list for nautilus-installer
# BuildRequires:	glibc-static
# BuildRequires:	gdk-pixbuf-static
# BuildRequires:	gtk+-static
# BuildRequires:	XFree86-static
# BuildRequires:	gnome-libs-static
# BuildRequires:	imlib-static
# BuildRequires:	esound-static
# BuildRequires:	audiofile-static
# BuildRequires:	db1-static
# BuildRequires:	db3-static
# BuildRequires:	libghttp-static
# BuildRequires:	zlib-static
# BuildRequires:	libxml-static

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir  /var

%description
GNU Nautilus is a free software file manager and graphical shell for GNOME.

%description -l pl
GNU Nautilus jest mened¿erem plików i graficzn± pow³ok± dla GNOME.

%package devel
Summary:	Libraries and header files for developing
Summary(pl):	Biblioteki i pliki nag³ówkowe
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries and header files needed for developing.

%description devel -l pl
Biblioteki i pliki nag³ówkowe potrzebne do programowania.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
gettextize --force --copy
aclocal -I %{_aclocaldir}/gnome
autoconf
automake -a -c
%configure \
	--enable-eazel-services \
	--with-mozilla-include-place=%{_includedir}/mozilla \
	--with-mozilla-lib-place=%{_libdir} \
#	--enable-installer

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	realsysconfdir=/etc \
	Applicationsdir=%{_applnkdir}/Applications

install -d $RPM_BUILD_ROOT%{_datadir}/idl
mv $RPM_BUILD_ROOT%{_prefix}/idl/* $RPM_BUILD_ROOT%{_datadir}/idl

%find_lang %{name}

gzip -9nf AUTHORS ChangeLog README TODO

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%{_sysconfdir}/CORBA/servers/*
%{_sysconfdir}/vfs/modules/*
%config /etc/pam.d/*
%config /etc/security/console.apps/*
%{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/vfs/modules/*
%{_mandir}/man?/*
%{_applnkdir}/*/*
%{_datadir}/gnome/ui
%{_datadir}/nautilus
%{_datadir}/omf/nautilus
%{_pixmapsdir}/*.*
%{_pixmapsdir}/nautilus

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/oaf/*
