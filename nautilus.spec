%bcond_without	esd	# do not require esd daemon to play MP3 files
#
Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl):	Nautilus - pow�oka GNOME i zarz�dca plik�w
Summary(pt_BR):	Nautilus � um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	2.9.91
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/nautilus/2.9/%{name}-%{version}.tar.bz2
# Source0-md5:	430e3615efe75ff07d5cc3c109987675
Source1:	%{name}.PLD.readme
Patch0:		%{name}-mpg123-esd.patch
Patch1:		%{name}-includes.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-capplet.patch
URL:		http://nautilus.eazel.com/
BuildRequires:	GConf2-devel >= 2.9.90
BuildRequires:	ORBit2-devel >= 1:2.12.1
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	cdparanoia-III-devel
BuildRequires:	docbook-utils >= 0.6.10
BuildRequires:	eel-devel >= 2.9.91
BuildRequires:	esound-devel >= 1:0.2.30
BuildRequires:	freetype-devel >= 2.1.4
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.9.91
BuildRequires:	gnome-vfs2-devel >= 2.9.90
BuildRequires:	intltool >= 0.31
BuildRequires:	libart_lgpl-devel >= 2.3.15
BuildRequires:	libbonobo-devel >= 2.8.1
BuildRequires:	libexif-devel >= 1:0.6.9
BuildRequires:	libgnomeui-devel >= 2.9.1
BuildRequires:	librsvg-devel >= 1:2.9.5
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5.10
BuildRequires:	popt-devel
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel >= 0.8
Requires(post):	GConf2
Requires:	gnome-icon-theme >= 2.9.91
Requires:	gnome-mime-data >= 2.4.0
Requires:	gnome-vfs2 >= 2.9.90
Requires:	%{name}-libs = %{version}-%{release}
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
Requires:	eel >= 2.9.91
Requires:	libbonobo >= 2.8.1

%description libs
Nautilus libraries.

%description libs -l pl
Biblioteki Nautilusa.

%package devel
Summary:	Libraries and include files for developing Nautilus components
Summary(pl):	Pliki nag��wkowe do tworzenia komponent�w dla Nautilusa
Summary(pt_BR):	Bibliotecas e arquivos para desenvolvimento com o nautilus
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	eel-devel >= 2.9.91
Requires:	librsvg-devel >= 1:2.9.5

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
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Nautilus libraries.

%description static -l pl
Biblioteki statyczne Nautilusa.

%prep
%setup -q
%{?with_esd:%patch0 -p1}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no
install %{SOURCE1} .

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README nautilus.PLD.readme
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/nautilus
%dir %{_libdir}/nautilus/extensions-1.0
%{_libdir}/bonobo/servers/*
%{_datadir}/nautilus
%{_sysconfdir}/gconf/schemas/*
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
