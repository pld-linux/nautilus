#
# Conditinal build:
%bcond_without	beagle		# enable beagle search
#
Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl.UTF-8):   Nautilus - powłoka GNOME i zarządca plików
Summary(pt_BR.UTF-8):   Nautilus é um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	2.16.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/nautilus/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	05a0fe98d524ca5287da21845ab8490c
Source1:	%{name}.PLD.readme
Patch0:		%{name}-includes.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-capplet.patch
Patch3:		%{name}-copy_label.patch
Patch4:		%{name}-dnd-user-owned.patch
URL:		http://nautilus.eazel.com/
BuildRequires:	GConf2-devel >= 2.16.0
BuildRequires:	ORBit2-devel >= 1:2.14.3
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
%{?with_beagle:BuildRequires:	beagle-devel >= 0.2.13}
BuildRequires:	docbook-utils >= 0.6.11
BuildRequires:	eel-devel >= 2.16.3
BuildRequires:	esound-devel >= 1:0.2.36
BuildRequires:	freetype-devel >= 2.1.4
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.16.2
BuildRequires:	gnome-vfs2-devel >= 2.16.3
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libart_lgpl-devel >= 2.3.17
BuildRequires:	libexif-devel >= 1:0.6.13
BuildRequires:	libgnomeui-devel >= 2.16.1
BuildRequires:	librsvg-devel >= 1:2.16.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	startup-notification-devel >= 0.8
Requires(post,preun):	GConf2 >= 2.16.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Requires:	gnome-icon-theme >= 2.16.0.1
Requires:	gnome-vfs2 >= 2.16.3
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

%description -l pl.UTF-8
GNU Nautilus jest programem do zarządzania plikami i graficzną powłoką
dla GNOME. Służy również bardzo dobrze jako przeglądarka stron WWW.

%description -l pt_BR.UTF-8
O nautilus é um excelente gerenciador de arquivos para o GNOME.

%package libs
Summary:	Nautilus libraries
Summary(pl.UTF-8):   Biblioteki Nautilusa
Group:		X11/Libraries
Requires:	eel >= 2.16.3
Requires:	gnome-vfs2-libs >= 2.16.3

%description libs
Nautilus libraries.

%description libs -l pl.UTF-8
Biblioteki Nautilusa.

%package devel
Summary:	Libraries and include files for developing Nautilus components
Summary(pl.UTF-8):   Pliki nagłówkowe do tworzenia komponentów dla Nautilusa
Summary(pt_BR.UTF-8):   Bibliotecas e arquivos para desenvolvimento com o nautilus
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	eel-devel >= 2.16.3
Requires:	gnome-vfs2-devel >= 2.16.3
Requires:	librsvg-devel >= 1:2.16.1

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
Summary(pl.UTF-8):   Biblioteki statyczne Nautilusa
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Nautilus libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Nautilusa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p0

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
install -d $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0

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

%preun
%gconf_schema_uninstall apps_nautilus_preferences.schemas

%postun
%update_desktop_database_postun
%update_mime_database

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
%{_desktopdir}/*.desktop
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
