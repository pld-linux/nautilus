#
# Conditinal build:
%bcond_without	apidocs		# disable API documentation

Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl.UTF-8):	Nautilus - powłoka GNOME i zarządca plików
Summary(pt_BR.UTF-8):	Nautilus é um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	3.28.0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus/3.28/%{name}-%{version}.tar.xz
# Source0-md5:	48fb205089ea8e5d85d11285111af7cb
URL:		http://www.gnome.org/projects/nautilus/
BuildRequires:	docbook-dtd412-xml
BuildRequires:	exempi-devel >= 2.1.0
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.56.0
BuildRequires:	gnome-autoar-devel >= 0.2.1
BuildRequires:	gnome-desktop-devel >= 3.2.0
BuildRequires:	gobject-introspection-devel >= 0.6.4
BuildRequires:	gsettings-desktop-schemas-devel >= 3.8.0
BuildRequires:	gtk+3-devel >= 3.22.26
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	libexif-devel >= 1:0.6.20
BuildRequires:	libselinux-devel
BuildRequires:	libxml2-devel >= 1:2.7.8
BuildRequires:	meson >= 0.41.0
BuildRequires:	ninja
BuildRequires:	pango-devel >= 1:1.28.3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	tracker-devel >= 1.0.0
BuildRequires:	xorg-lib-libSM-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.52.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
Requires:	exempi >= 2.1.0
Requires:	glib2 >= 1:2.56.0
Requires:	gnome-autoar >= 0.2.1
Requires:	gnome-desktop >= 3.2.0
Requires:	gsettings-desktop-schemas >= 3.8.0
Requires:	gvfs >= 1.16.0
Requires:	hicolor-icon-theme
Requires:	libexif >= 1:0.6.20
Requires:	libxml2 >= 1:2.7.8
Requires:	pango >= 1:1.28.3
Requires:	tracker >= 1.0.0
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
Requires:	glib2 >= 1:2.56.0
Requires:	gtk+3 >= 3.22.26

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
Requires:	glib2-devel >= 1:2.56.0
Requires:	gtk+3-devel >= 3.22.26
Requires:	libselinux-devel
Obsoletes:	eel-devel
Obsoletes:	nautils-static

%description devel
This package provides the necessary development libraries and include
files to allow you to develop Nautilus components.

%description devel -l pl.UTF-8
Biblioteki i pliki nagłówkowe potrzebne do programowania.

%description devel -l pt_BR.UTF-8
Este pacote fornece os arquivos necessários para desenvolvimento
utilizando componentes do nautilus.

%package apidocs
Summary:	Nautilus API documentation
Summary(pl.UTF-8):	Dokumentacja API Nautilusa
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Nautilus API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Nautilusa.

%prep
%setup -q

%build
%meson build \
	-Dpackagekit=true \
	-Ddocs=%{__true_false apidocs}

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}}

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr@ije,sr@ijekavian}
# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{io,ln}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
if [ "$1" = "0" ]; then
	%glib_compile_schemas
fi

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/nautilus
%attr(755,root,root) %{_bindir}/nautilus-autorun-software
%dir %{_libdir}/nautilus
%dir %{_libdir}/nautilus/extensions-3.0
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-image-properties.so
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-sendto.so
%{_datadir}/metainfo/org.gnome.Nautilus.appdata.xml
%{_datadir}/dbus-1/services/org.freedesktop.FileManager1.service
%{_datadir}/dbus-1/services/org.gnome.Nautilus.service
%{_datadir}/glib-2.0/schemas/org.gnome.nautilus.gschema.xml
%{_desktopdir}/nautilus-autorun-software.desktop
%{_desktopdir}/org.gnome.Nautilus.desktop
%{_mandir}/man1/nautilus.1*
%{_datadir}/gnome-shell/search-providers/nautilus-search-provider.ini
%{_iconsdir}/hicolor/*/*/org.gnome.Nautilus.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Nautilus-symbolic.svg

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-extension.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnautilus-extension.so.1
%{_libdir}/girepository-1.0/Nautilus-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-extension.so
%{_includedir}/nautilus
%{_datadir}/gir-1.0/Nautilus-3.0.gir
%{_pkgconfigdir}/libnautilus-extension.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libnautilus-extension
%endif
