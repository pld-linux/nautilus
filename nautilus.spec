Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl):	nautilus - pow³oka GNOME i menad¿er plików
Summary(pt_BR):	Nautilus é um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	1.1.16
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://nautilus.eazel.com/
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-activation-devel
BuildRequires:	eel-devel >= 1.1.11
BuildRequires:	esound-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1.1.6
BuildRequires:	libxml2-devel
BuildRequires:	medusa-devel
BuildRequires:	scrollkeeper
Prereq:		/sbin/ldconfig
Prereq:		scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME2
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
Nautilus integrates access to files, applications, media,
Internet-based resources and the Web. Nautilus delivers a dynamic and
rich user experience. Nautilus is an free software project developed
under the GNU General Public License and is a core component of the
GNOME desktop project.

%description -l pl
GNU Nautilus jest mened¿erem plików i graficzn± pow³ok± dla GNOME.
S³u¿y równie¿ bardzo dobrze jako przegl±darka stron WWW.

%description -l pt_BR
O nautilus é um excelente gerenciador de arquivos para o GNOME.

%package devel
Summary:	Libraries and include files for developing Nautilus components
Summary(pl):	Pliki nag³ówkowe do tworzenia komponentów dla Nautilusa
Summary(pt_BR):	Bibliotecas e arquivos para desenvolvimento com o nautilus
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	eel-devel
Requires:	librsvg-devel

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
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Nautilus libraries.

%description static -l pl
Biblioteki statyczne Nautilusa.

%prep
%setup -q

%build
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
        CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
%configure CPPFLAGS="$CPPFLAGS" \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

gzip -9nf ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
scrollkeeper-update
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
/usr/X11R6/bin/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null 2>&1

%postun
/sbin/ldconfig
scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%{_sysconfdir}/gconf/schemas/*
%{_sysconfdir}/X11
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/bonobo/servers/*
%{_datadir}/applications/*
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/idl/*
%{_datadir}/nautilus
%{_pixmapsdir}/*.png
%{_pixmapsdir}/nautilus
%{_omf_dest_dir}/nautilus

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.??
%{_includedir}/libnautilus
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
