#
# Conditinal build:
%bcond_without	apidocs		# disable API documentation
%bcond_without	selinux		# SELinux context support in file properties dialog

%ifarch alpha ia64 m68k parisc parisc64 sh4 sparc sparcv9 sparc64
%define	use_seccomp	0
%else
%define	use_seccomp	1
%endif
Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl.UTF-8):	Nautilus - powłoka GNOME i zarządca plików
Summary(pt_BR.UTF-8):	Nautilus é um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	3.36.3
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus/3.36/%{name}-%{version}.tar.xz
# Source0-md5:	c3c8dbb90d8eeed6c127aa568e131395
URL:		https://wiki.gnome.org/Apps/Files
BuildRequires:	docbook-dtd412-xml
BuildRequires:	fontconfig-devel
# -std=c11
BuildRequires:	gcc >= 6:4.7
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	gexiv2-devel >= 0.10.0
BuildRequires:	glib2-devel >= 1:2.58.1
BuildRequires:	gnome-autoar-devel >= 0.2.1
BuildRequires:	gnome-desktop-devel >= 3.0.0
BuildRequires:	gobject-introspection-devel >= 0.6.4
BuildRequires:	gsettings-desktop-schemas-devel >= 3.8.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.22.27
BuildRequires:	gtk-doc >= 1.10
%if %{use_seccomp}
BuildRequires:	libseccomp-devel
%endif
%{?with_selinux:BuildRequires:	libselinux-devel >= 2.0}
BuildRequires:	libxml2-devel >= 1:2.7.8
BuildRequires:	meson >= 0.47.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker-devel >= 2.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.58.1
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gexiv2 >= 0.10.0
Requires:	glib2 >= 1:2.58.1
Requires:	gnome-autoar >= 0.2.1
Requires:	gsettings-desktop-schemas >= 3.8.0
Requires:	gvfs >= 1.16.0
Requires:	hicolor-icon-theme
Requires:	libxml2 >= 1:2.7.8
Requires:	tracker >= 2.0
Provides:	gnome-volume-manager
Obsoletes:	eel
Obsoletes:	gnome-volume-manager
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

%description -l pl.UTF-8
GNU Nautilus jest programem do zarządzania plikami i graficzną powłoką
dla GNOME. Służy również bardzo dobrze jako przeglądarka stron WWW.

%description -l pt_BR.UTF-8
O nautilus é um excelente gerenciador de arquivos para o GNOME.

%package libs
Summary:	Nautilus libraries
Summary(pl.UTF-8):	Biblioteki Nautilusa
Group:		X11/Libraries
Requires:	glib2 >= 1:2.58.1
Requires:	gtk+3 >= 3.22.27

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
Requires:	glib2-devel >= 1:2.58.1
Requires:	gtk+3-devel >= 3.22.27
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
%if "%{_rpmversion}" >= "4.6"
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
	-Ddocs=%{__true_false apidocs} \
	-Dpackagekit=true \
	%{?with_selinux:-Dselinux=true}

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}}

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr@ije,sr@ijekavian}
# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/io

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
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libtotem-properties-page.so
%{_datadir}/metainfo/org.gnome.Nautilus.appdata.xml
%{_datadir}/dbus-1/services/org.freedesktop.FileManager1.service
%{_datadir}/dbus-1/services/org.gnome.Nautilus.service
%{_datadir}/glib-2.0/schemas/org.gnome.nautilus.gschema.xml
%{_desktopdir}/nautilus-autorun-software.desktop
%{_desktopdir}/org.gnome.Nautilus.desktop
%{_mandir}/man1/nautilus.1*
%{_mandir}/man1/nautilus-autorun-software.1*
%{_datadir}/gnome-shell/search-providers/org.gnome.Nautilus.search-provider.ini
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Nautilus.svg
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
