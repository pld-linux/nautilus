Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl):	nautilus - pow�oka GNOME i menad�er plik�w
Summary(pt_BR):	Nautilus � um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	1.1.17
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://nautilus.eazel.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-activation-devel >= 0.9.9
BuildRequires:	cdparanoia-III-devel
BuildRequires:	docbook-utils >= 0.6.10
BuildRequires:	eel-devel >= 1.1.15
BuildRequires:	esound-devel >= 0.2.23
BuildRequires:	freetype-devel
BuildRequires:	GConf2-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gnome-desktop-devel >= 1.5.11
BuildRequires:	gnome-vfs2-devel >= 1.9.16
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	intltool
BuildRequires:	libart_lgpl-devel >= 2.3.6
BuildRequires:	libbonobo-devel >= 1.113.0
BuildRequires:	libbonoboui-devel >= 1.116.1
BuildRequires:	libgnome >= 1.105.0
BuildRequires:	libgnomecanvas >= 1.105.0
BuildRequires:	libgnomeui >= 1.110.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2.3
BuildRequires:	librsvg-devel >= 1.1.6
BuildRequires:	libxml2-devel >= 2.4.7
# need check medusa for building with gnome-vfs2
#BuildRequires:	medusa-devel >= 0.5.1
BuildRequires:	ORBit2-devel
BuildRequires:	pango-devel
BuildRequires:	scrollkeeper
Prereq:		/sbin/ldconfig
Prereq:		scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME2
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
Nautilus integrates access to files, applications, media,
Internet-based resources and the Web. Nautilus delivers a dynamic and
rich user experience. Nautilus is an free software project developed
under the GNU General Public License and is a core component of the
GNOME desktop project.

%description -l pl
GNU Nautilus jest mened�erem plik�w i graficzn� pow�ok� dla GNOME.
S�u�y r�wnie� bardzo dobrze jako przegl�darka stron WWW.

%description -l pt_BR
O nautilus � um excelente gerenciador de arquivos para o GNOME.

%package devel
Summary:	Libraries and include files for developing Nautilus components
Summary(pl):	Pliki nag��wkowe do tworzenia komponent�w dla Nautilusa
Summary(pt_BR):	Bibliotecas e arquivos para desenvolvimento com o nautilus
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	eel-devel
Requires:	librsvg-devel

%description devel
This package provides the necessary development libraries and include
files to allow you to develop Nautilus components.

%description devel -l pl
Biblioteki i pliki nag��wkowe potrzebne do programowania.

%description devel -l pt_BR
Este pacote fornece os arquivos necess�rios para desenvolvimento
utilizando componentes do nautilus.

%package static
Summary:	Static Nautilus libraries
Summary(pl):	Biblioteki statyczne Nautilusa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Nautilus libraries.

%description static -l pl
Biblioteki statyczne Nautilusa.

%prep
%setup -q

%build
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
scrollkeeper-update
GCONF_CONFIG_SOURCE="" /usr/X11R6/bin/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null

%postun
/sbin/ldconfig
scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/*
%{_sysconfdir}/X11
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libnautilus-history-view.so
%attr(755,root,root) %{_libdir}/libnautilus-history-view.la
%attr(755,root,root) %{_libdir}/libnautilus-notes-view.so
%attr(755,root,root) %{_libdir}/libnautilus-notes-view.la
%attr(755,root,root) %{_libdir}/libnautilus-tree-view.so
%attr(755,root,root) %{_libdir}/libnautilus-tree-view.la
%{_libdir}/bonobo/servers/*
%{_datadir}/applications/*
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/idl/*
%{_datadir}/nautilus
%{_pixmapsdir}/*.png
%{_pixmapsdir}/nautilus
%{_omf_dest_dir}/nautilus

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
