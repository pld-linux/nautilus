#
# Conditinal build:
%bcond_without	apidocs		# disable API documentation
#
Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl.UTF-8):	Nautilus - powłoka GNOME i zarządca plików
Summary(pt_BR.UTF-8):	Nautilus é um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	2.91.6
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus/2.91/%{name}-%{version}.tar.bz2
# Source0-md5:	6d7fdfd571884f9c4a6206a17aa4274f
Source1:	%{name}.PLD.readme
URL:		http://www.gnome.org/projects/nautilus/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	exempi-devel >= 1.99.5
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.27.2
BuildRequires:	gnome-desktop3-devel >= 2.91.4
BuildRequires:	gobject-introspection-devel >= 0.6.4
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 2.91.7
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.40.1
BuildRequires:	libexif-devel >= 1:0.6.13
BuildRequires:	libselinux-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
# libegg
BuildRequires:	xorg-lib-libSM-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2 >= 1:2.27.2
Requires:	gnome-icon-theme >= 2.26.0
Requires:	gsettings-desktop-schemas
Requires:	gvfs >= 1.6.0
Obsoletes:	eel
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
Requires:	glib2-devel >= 1:2.27.2
Requires:	gtk+3-devel >= 2.91.7
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

sed -i -e 's#^en@shaw##' po/LINGUAS
sed -i -e 's#^io##' po/LINGUAS
rm -f po/en@shaw.po
rm -f po/io.po

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

# kill it - use banner instead
install %{SOURCE1} .

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.{a,la}

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%update_desktop_database_post
%update_icon_cache hicolor
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas

%postun
%update_desktop_database_postun
%update_mime_database
%update_icon_cache hicolor
if [ "$1" = "0" ]; then
	%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas
fi

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README THANKS nautilus.PLD.readme
%attr(755,root,root) %{_bindir}/nautilus
%attr(755,root,root) %{_bindir}/nautilus-autorun-software
%attr(755,root,root) %{_bindir}/nautilus-connect-server
%attr(755,root,root) %{_libexecdir}/nautilus-convert-metadata
%dir %{_libdir}/nautilus
%dir %{_libdir}/nautilus/extensions-3.0
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-sendto.so
%{_datadir}/GConf/gsettings/nautilus.convert
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/mime/packages/*.xml
%{_datadir}/nautilus
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/nautilus.*
%{_mandir}/man1/nautilus*.1*
%{_pixmapsdir}/nautilus

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-extension.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnautilus-extension.so.1
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-extension.so
%{_libdir}/libnautilus-extension.la
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
