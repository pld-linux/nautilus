# TODO:
# separate libnautilus
Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl):	nautilus - pow³oka GNOME i menad¿er plików
Summary(pt_BR):	Nautilus é um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	2.0.7
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/2.0.2/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am.patch
URL:		http://nautilus.eazel.com/
Requires:	gnome-mime-data >= 2.0.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-activation-devel >= 1.0.3
BuildRequires:	cdparanoia-III-devel
BuildRequires:	docbook-utils >= 0.6.10
BuildRequires:	eel-devel >= 2.0.7
BuildRequires:	esound-devel >= 0.2.29
BuildRequires:	freetype-devel
BuildRequires:	GConf2-devel >= 1.2.1
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0.6
BuildRequires:	gnome-desktop-devel >= 2.0.8
BuildRequires:	gnome-vfs2-devel >= 2.0.4
BuildRequires:	gtk+2-devel >= 2.0.6
BuildRequires:	intltool
BuildRequires:	libart_lgpl-devel >= 2.3.10
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRequires:	libbonoboui-devel >= 2.0.3
BuildRequires:	libgnome >= 2.0.5
BuildRequires:	libgnomecanvas >= 2.0.4
BuildRequires:	libgnomeui >= 2.0.5
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.0.1
BuildRequires:	libxml2-devel >= 2.4.24
# need check medusa for building with gnome-vfs2
#BuildRequires:	medusa-devel >= 0.5.1
BuildRequires:	ORBit2-devel >= 2.4.3
BuildRequires:	pango-devel >= 1.0.4
Prereq:		/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME2

%description
Nautilus integrates access to files, applications, media,
Internet-based resources and the Web. Nautilus delivers a dynamic and
rich user experience. Nautilus is an free software project developed
under the GNU General Public License and is a core component of the
GNOME desktop project.

%description -l pl
GNU Nautilus jest mened¿erem plików i graficzn± pow³ok± dla GNOME.
S³u¿y równie¿ bardzo dobrze jako przegl±darka stron WWW.

%description -l pt_BR
O nautilus é um excelente gerenciador de arquivos para o GNOME.

%package libs
Summary:	Nautilus libraries
Summary(pl):	Biblioteki Nautilusa
Group:		X11/Libraries

%description libs
Nautilus libraries.

%description libs -l pl
Biblioteki Nautilusa.

%package devel
Summary:	Libraries and include files for developing Nautilus components
Summary(pl):	Pliki nag³ówkowe do tworzenia komponentów dla Nautilusa
Summary(pt_BR):	Bibliotecas e arquivos para desenvolvimento com o nautilus
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}
Requires:	eel-devel
Requires:	librsvg-devel

%description devel
This package provides the necessary development libraries and include
files to allow you to develop Nautilus components.

%description devel -l pl
Biblioteki i pliki nag³ówkowe potrzebne do programowania.

%description devel -l pt_BR
Este pacote fornece os arquivos necessários para desenvolvimento
utilizando componentes do nautilus.

%package static
Summary:	Static Nautilus libraries
Summary(pl):	Biblioteki statyczne Nautilusa
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Nautilus libraries.

%description static -l pl
Biblioteki statyczne Nautilusa.

%prep
%setup -q
%patch0 -p1

%build
intltoolize --copy --force
glib-gettextize --copy --force
libtoolize --copy --force
aclocal
%{__autoconf}
%{__automake}

%configure \
	--enable-static \
	--enable-hardware

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" /usr/X11R6/bin/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/*
%{_sysconfdir}/X11
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/nautilus-*
%attr(755,root,root) %{_libdir}/bonobo/lib*.??
%{_libdir}/bonobo/servers/*
%{_datadir}/applications/*
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/idl/*
%{_datadir}/nautilus
%{_pixmapsdir}/*.png
%{_pixmapsdir}/nautilus

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus.so
%attr(755,root,root) %{_libdir}/libnautilus.la
%attr(755,root,root) %{_libdir}/libnautilus-adapter.so
%attr(755,root,root) %{_libdir}/libnautilus-adapter.la
%attr(755,root,root) %{_libdir}/libnautilus-private.so
%attr(755,root,root) %{_libdir}/libnautilus-private.la
%{_includedir}/libnautilus
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/bonobo/lib*.a
