Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl):	Nautilus - pow³oka GNOME i zarz±dca plików
Summary(pt_BR):	Nautilus é um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	2.7.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	cf40444160759da44fe3b40d77cc2632
Patch1:		%{name}-mpg123-esd.patch
Patch2:		%{name}-includes.patch
Patch3:		%{name}-locale-names.patch
Patch4:		%{name}-disable_medusa.patch
Patch5:		%{name}-desktop.patch
Patch6:		%{name}-launcher.patch
URL:		http://nautilus.eazel.com/
BuildRequires:	GConf2-devel >= 2.7.1
BuildRequires:	ORBit2-devel >= 1:2.10.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cdparanoia-III-devel
BuildRequires:	docbook-utils >= 0.6.10
BuildRequires:	eel-devel >= 2.7.1
BuildRequires:	esound-devel >= 1:0.2.30
BuildRequires:	freetype-devel >= 2.1.4
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.7.1
BuildRequires:	gnome-vfs2-devel >= 2.7.1
BuildRequires:	intltool >= 0.30
BuildRequires:	libart_lgpl-devel >= 2.3.15
BuildRequires:	libbonoboui-devel >= 2.6.0
BuildRequires:	libgnomeui-devel >= 2.7.1
BuildRequires:	libjpeg-devel
BuildRequires:	librsvg-devel >= 1:2.6.2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5.10
BuildRequires:	popt-devel
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel >= 0.6
Requires(post):	GConf2
Requires:	gnome-icon-theme >= 1.3.2
Requires:	gnome-mime-data >= 2.4.0
Requires:	mpg123-esd
Requires:	gnome-vfs2 >= 2.7.1
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
Requires:	eel >= 2.7.1
Requires:	libbonobo >= 2.6.0

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
Requires:	eel-devel >= 2.7.1
Requires:	librsvg-devel >= 1:2.6.2

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

mv po/{no,nb}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
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

rm -f $RPM_BUILD_ROOT%{_libdir}/bonobo/*.{la,a}

install -d $RPM_BUILD_ROOT%{_datadir}/gnome/capplets
mv $RPM_BUILD_ROOT%{_datadir}/control-center-2.0/capplets/*.desktop $RPM_BUILD_ROOT%{_datadir}/gnome/capplets

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
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome/capplets/*.desktop
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/idl/*
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
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
