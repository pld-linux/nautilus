#
# TODO:
# - tracker bcond
#
# Conditinal build:
%bcond_without	beagle		# disable beagle search
#
Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl.UTF-8):	Nautilus - powłoka GNOME i zarządca plików
Summary(pt_BR.UTF-8):	Nautilus é um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	2.21.5
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus/2.21/%{name}-%{version}.tar.bz2
# Source0-md5:	cd1e6dbab5cd31678c0a8bc4ecd979fd
Source1:	%{name}.PLD.readme
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-capplet.patch
Patch3:		%{name}-dnd-user-owned.patch
URL:		http://www.gnome.org/projects/nautilus/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	ORBit2-devel >= 1:2.14.8
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
%{?with_beagle:BuildRequires:	beagle-devel >= 0.2.13}
BuildRequires:	docbook-utils >= 0.6.11
BuildRequires:	eel-devel >= 2.21.5
BuildRequires:	esound-devel >= 1:0.2.37
BuildRequires:	exempi-devel >= 1.99.2
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	glib2-devel >= 1:2.15.2
BuildRequires:	gnome-desktop-devel >= 2.21.4
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libexif-devel >= 1:0.6.13
BuildRequires:	libgnomeui-devel >= 2.20.1
BuildRequires:	librsvg-devel >= 1:2.18.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	startup-notification-devel >= 0.8
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
Requires:	eel >= 2.21.5
Requires:	gvfs
Requires:	gnome-icon-theme >= 2.20.0
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	gstreamer-player-nautilus
Obsoletes:	nautilus-gtkhtml
Obsoletes:	nautilus-media
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus integrates access to files, applications, media,
Internet-based resources and the Web. Nautilus delivers a dynamic and
rich user experience. Nautilus is an free software project developed
under the GNU General Public License and is a core component of the
GNOME desktop project.

%description -l pl.UTF-8
GNU Nautilus jest programem do zarządzania plikami i graficzną powłoką
dla GNOME. Służy również bardzo dobrze jako przeglądarka stron WWW.

%description -l pt_BR.UTF-8
O nautilus é um excelente gerenciador de arquivos para o GNOME.

%package libs
Summary:	Nautilus libraries
Summary(pl.UTF-8):	Biblioteki Nautilusa
Group:		X11/Libraries

%description libs
Nautilus libraries.

%description libs -l pl.UTF-8
Biblioteki Nautilusa.

%package devel
Summary:	Libraries and include files for developing Nautilus components
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia komponentów dla Nautilusa
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos para desenvolvimento com o nautilus
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.15.2
Requires:	gtk+2-devel >= 2:2.12.0

%description devel
This package provides the necessary development libraries and include
files to allow you to develop Nautilus components.

%description devel -l pl.UTF-8
Biblioteki i pliki nagłówkowe potrzebne do programowania.

%description devel -l pt_BR.UTF-8
Este pacote fornece os arquivos necessários para desenvolvimento
utilizando componentes do nautilus.

%package static
Summary:	Static Nautilus libraries
Summary(pl.UTF-8):	Biblioteki statyczne Nautilusa
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Nautilus libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Nautilusa.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
#%patch3 -p0

sed -i -e s#sr@Latn#sr@latin# po/LINGUAS
mv -f po/sr@{Latn,latin}.po

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static \
	%{?!with_beagle:--disable-beagle} \
	--disable-update-mimedb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# kill it - use banner instead
install %{SOURCE1} .

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%gconf_schema_install apps_nautilus_preferences.schemas
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall apps_nautilus_preferences.schemas

%postun
%update_desktop_database_postun
%update_mime_database
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README THANKS nautilus.PLD.readme
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/nautilus
%dir %{_libdir}/nautilus/extensions-2.0
%{_libdir}/bonobo/servers/Nautilus_shell.server
%{_datadir}/mime/packages/*.xml
%{_datadir}/nautilus
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/nautilus.*
%{_pixmapsdir}/nautilus
%{_sysconfdir}/gconf/schemas/apps_nautilus_preferences.schemas

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-extension.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnautilus-extension.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-extension.so
%{_libdir}/libnautilus-extension.la
%{_includedir}/nautilus
%{_pkgconfigdir}/libnautilus-extension.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnautilus-extension.a
