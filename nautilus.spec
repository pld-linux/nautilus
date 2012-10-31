#
# Conditinal build:
%bcond_without	apidocs		# disable API documentation

Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl.UTF-8):	Nautilus - powłoka GNOME i zarządca plików
Summary(pt_BR.UTF-8):	Nautilus é um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	3.6.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	1fa690cdb93c1980a221907a95190d19
Patch0:		autostart-desc.patch
URL:		http://www.gnome.org/projects/nautilus/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	exempi-devel >= 2.1.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.34.0
BuildRequires:	gnome-desktop-devel >= 3.2.0
BuildRequires:	gobject-introspection-devel >= 0.6.4
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 3.6.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.40.1
BuildRequires:	libexif-devel >= 1:0.6.20
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libselinux-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.7.8
BuildRequires:	pango-devel >= 1.28.3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	tracker-devel >= 0.14
# libegg
BuildRequires:	xorg-lib-libSM-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2 >= 1:2.34.0
Requires:	gsettings-desktop-schemas
Requires:	gtk+3 >= 3.6.0
Requires:	gvfs >= 1.12.0
Provides:	gnome-volume-manager
Obsoletes:	eel
Obsoletes:	gnome-volume-manager
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
Requires:	glib2-devel >= 1:2.34.0
Requires:	gtk+3-devel >= 3.6.0
Requires:	libselinux-devel
Obsoletes:	eel-devel

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

%package apidocs
Summary:	Nautilus API documentation
Summary(pl.UTF-8):	Dokumentacja API Nautilusa
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Nautilus API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Nautilusa.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e 's#^io##' po/LINGUAS
%{__rm} po/io.po

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--enable-packagekit \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--disable-silent-rules \
	--disable-update-mimedb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.{a,la}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%update_desktop_database_post
%glib_compile_schemas

%postun
%update_desktop_database_postun
%update_mime_database
if [ "$1" = "0" ]; then
	%glib_compile_schemas
fi

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README THANKS
%attr(755,root,root) %{_bindir}/nautilus
%attr(755,root,root) %{_bindir}/nautilus-autorun-software
%attr(755,root,root) %{_bindir}/nautilus-connect-server
%attr(755,root,root) %{_libexecdir}/nautilus-convert-metadata
%attr(755,root,root) %{_libexecdir}/nautilus-shell-search-provider
%dir %{_libdir}/nautilus
%dir %{_libdir}/nautilus/extensions-3.0
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-sendto.so
%{_datadir}/GConf/gsettings/nautilus.convert
%{_datadir}/dbus-1/services/org.freedesktop.FileManager1.service
%{_datadir}/dbus-1/services/org.gnome.Nautilus.SearchProvider.service
%{_datadir}/dbus-1/services/org.gnome.Nautilus.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/mime/packages/*.xml
%{_datadir}/nautilus
%{_desktopdir}/*.desktop
%{_mandir}/man1/nautilus*.1*
%{_sysconfdir}/xdg/autostart/nautilus-autostart.desktop
%{_datadir}/gnome-shell/search-providers/nautilus-search-provider.ini

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-extension.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnautilus-extension.so.1
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-extension.so
%{_includedir}/nautilus
%{_pkgconfigdir}/libnautilus-extension.pc
%{_datadir}/gir-1.0/*.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libnautilus-extension.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libnautilus-extension
%endif
