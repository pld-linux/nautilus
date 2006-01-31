Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl):	Nautilus - pow³oka GNOME i zarz±dca plików
Summary(pt_BR):	Nautilus é um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	2.13.90
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/nautilus/2.13/%{name}-%{version}.tar.bz2
# Source0-md5:	914a761043497e8250126bb84a5bfeec
Source1:	%{name}.PLD.readme
Patch0:		%{name}-includes.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-capplet.patch
URL:		http://nautilus.eazel.com/
BuildRequires:	GConf2-devel >= 2.12.0
BuildRequires:	ORBit2-devel >= 1:2.12.3
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	beagle-devel >= 0.0.12
BuildRequires:	docbook-utils >= 0.6.10
BuildRequires:	eel-devel >= 2.13.90
BuildRequires:	esound-devel >= 1:0.2.30
BuildRequires:	freetype-devel >= 2.1.4
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.12.1
BuildRequires:	gnome-vfs2-devel >= 2.13.2
BuildRequires:	intltool >= 0.33
BuildRequires:	libart_lgpl-devel >= 2.3.17
BuildRequires:	libbonobo-devel >= 2.10.1
BuildRequires:	libexif-devel >= 1:0.6.12
BuildRequires:	libgnomeui-devel >= 2.12.0
BuildRequires:	librsvg-devel >= 1:2.9.5-2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.21
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	startup-notification-devel >= 0.8
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Requires:	gnome-icon-theme >= 2.12.0
Requires:	gnome-vfs2 >= 2.13.2
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	gstreamer-player-nautilus
Obsoletes:	nautilus-gtkhtml
Obsoletes:	nautilus-media
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus integrates access to files, applications, media,
Internet-based resources and the Web. Nautilus delivers a dynamic and
rich user experience. Nautilus is an free software project developed
under the GNU General Public License and is a core component of the
GNOME desktop project.

%description -l pl
GNU Nautilus jest programem do zarz±dzania plikami i graficzn± pow³ok±
dla GNOME. S³u¿y równie¿ bardzo dobrze jako przegl±darka stron WWW.

%description -l pt_BR
O nautilus é um excelente gerenciador de arquivos para o GNOME.

%package libs
Summary:	Nautilus libraries
Summary(pl):	Biblioteki Nautilusa
Group:		X11/Libraries
Requires:	eel >= 2.13.90
Requires:	libbonobo >= 2.10.1

%description libs
Nautilus libraries.

%description libs -l pl
Biblioteki Nautilusa.

%package devel
Summary:	Libraries and include files for developing Nautilus components
Summary(pl):	Pliki nag³ówkowe do tworzenia komponentów dla Nautilusa
Summary(pt_BR):	Bibliotecas e arquivos para desenvolvimento com o nautilus
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	eel-devel >= 2.13.4
Requires:	librsvg-devel >= 1:2.9.5-2

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
Requires:	%{name}-devel = %{version}-%{release}

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
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static \
	--disable-update-mimedb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

# kill it - use banner instead
install %{SOURCE1} .

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
update-mime-database %{_datadir}/mime >/dev/null 2>&1 ||:
%gconf_schema_install apps_nautilus_preferences.schemas
%update_desktop_database_post

%preun
%gconf_schema_uninstall apps_nautilus_preferences.schemas

%postun
%update_desktop_database_postun
if [ $1 = 0 ]; then
	umask 022
	update-mime-database %{_datadir}/mime >/dev/null 2>&1 ||:
fi

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README THANKS nautilus.PLD.readme
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/nautilus
%dir %{_libdir}/nautilus/extensions-1.0
%{_libdir}/bonobo/servers/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/nautilus
%{_desktopdir}/*
%{_pixmapsdir}/nautilus
%{_sysconfdir}/gconf/schemas/apps_nautilus_preferences.schemas

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus*.so
%{_libdir}/libnautilus*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
