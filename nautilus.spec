Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl):	Nautilus - pow�oka GNOME i zarz�dca plik�w
Summary(pt_BR):	Nautilus � um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	2.5.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	e6ff9394e006e48b44b27a23a4314eed
Patch0:		%{name}-vcategories.patch
Patch1:		%{name}-mpg123-esd.patch
Patch2:		%{name}-gtk23.patch
URL:		http://nautilus.eazel.com/
BuildRequires:	GConf2-devel >= 2.3.3
BuildRequires:	ORBit2-devel >= 2.9.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cdparanoia-III-devel
BuildRequires:	docbook-utils >= 0.6.10
BuildRequires:	eel-devel >= 2.5.0
BuildRequires:	esound-devel >= 0.2.30
BuildRequires:	freetype-devel >= 2.1.4
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.3.0
BuildRequires:	gnome-desktop-devel >= 2.3.90
BuildRequires:	gnome-vfs2-devel >= 2.5.0
BuildRequires:	gtk+2-devel >= 2.3.0
BuildRequires:	intltool
BuildRequires:	libart_lgpl-devel >= 2.3.15
BuildRequires:	libbonobo-devel >= 2.4.0
BuildRequires:	libbonoboui-devel >= 2.4.0
BuildRequires:	libgnome-devel >= 2.4.0
BuildRequires:	libgnomecanvas-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5.10
BuildRequires:	pango-devel >= 1.2.5
Requires(post):	GConf2
Requires:	gnome-icon-theme >= 1.0.9
Requires:	gnome-mime-data >= 2.3.1
Requires:	mpg123-esd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus integrates access to files, applications, media,
Internet-based resources and the Web. Nautilus delivers a dynamic and
rich user experience. Nautilus is an free software project developed
under the GNU General Public License and is a core component of the
GNOME desktop project.

%description -l pl
GNU Nautilus jest programem do zarz�dzania plikami i graficzn� pow�ok�
dla GNOME. S�u�y r�wnie� bardzo dobrze jako przegl�darka stron WWW.

%description -l pt_BR
O nautilus � um excelente gerenciador de arquivos para o GNOME.

%package libs
Summary:	Nautilus libraries
Summary(pl):	Biblioteki Nautilusa
Group:		X11/Libraries
Requires:	eel >= 2.4.1
Requires:	libbonobo >= 2.4.0

%description libs
Nautilus libraries.

%description libs -l pl
Biblioteki Nautilusa.

%package devel
Summary:	Libraries and include files for developing Nautilus components
Summary(pl):	Pliki nag��wkowe do tworzenia komponent�w dla Nautilusa
Summary(pt_BR):	Bibliotecas e arquivos para desenvolvimento com o nautilus
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}
Requires:	eel-devel >= 2.4.0
Requires:	librsvg-devel >= 2.4.0

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
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Nautilus libraries.

%description static -l pl
Biblioteki statyczne Nautilusa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
intltoolize --copy --force
glib-gettextize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static \
	--enable-hardware

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/bonobo/*.a

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/nautilus-*
%attr(755,root,root) %{_libdir}/bonobo/lib*.so
%{_libdir}/bonobo/lib*.la
%{_libdir}/bonobo/servers/*
%{_datadir}/control-center-2.0/capplets/*.desktop
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/idl/*
%{_datadir}/gnome/network
%{_datadir}/nautilus
%{_sysconfdir}/gconf/schemas/*
%{_sysconfdir}/X11/*
%{_pixmapsdir}/nautilus
%{_desktopdir}/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus*.so
%{_libdir}/libnautilus*.la
%{_includedir}/libnautilus
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
