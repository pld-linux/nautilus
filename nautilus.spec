Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl):	nautilus - pow³oka GNOME i menad¿er plików
Summary(pt_BR):	Nautilus é um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	1.0.6
Release:	6
License:	GPL
Group:		X11/Window Managers
Group(cs):	X11/Okenní mana¾ery
Group(de):	X11/Fenstermanager
Group(es):	X11/Administradores de Ventanas
Group(fr):	X11/Gestionnaires de fenêtres
Group(pl):	X11/Zarz±dcy okien
Group(pt):	X11/Gestores de Janelas
Group(ru):	X11/ïËÏÎÎÙÅ ÍÅÎÅÄÖÅÒÙ
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-applnk.patch
Patch2:		%{name}-aclocal.patch
Patch3:		%{name}-amfix.patch
Patch4:		%{name}-bonobo-workaround.patch
Patch5:		%{name}-cpp.patch
Patch6:		%{name}-omf-encoding.patch
Patch7:		%{name}-mozilla-profile-startup.patch
Patch8:		%{name}-ac25.patch
URL:		http://nautilus.eazel.com/
BuildRequires:	GConf-devel >= 0.12
BuildRequires:	ORBit-devel >= 0.5.7
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel >= 1.0.9
BuildRequires:	control-center-devel >= 1.3
BuildRequires:	eel-devel >= 1.0.2
BuildRequires:	esound-devel >= 0.2.22
BuildRequires:	freetype-devel >= 2.0.1
BuildRequires:	gdk-pixbuf-devel >= 0.10.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-applets
BuildRequires:	gnome-core-devel >= 1.4.0.4
BuildRequires:	gnome-http-devel
BuildRequires:	gnome-libs-devel >= 1.2.11
BuildRequires:	gnome-vfs-devel >= 1.0.3
BuildRequires:	gtk+-devel >= 1.2.9
BuildRequires:	imlib-devel >= 1.9.8
BuildRequires:	intltool
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1.0.1
BuildRequires:	libxml-devel >= 1.8.10
BuildRequires:	medusa-devel >= 0.5.1
BuildRequires:	mozilla-devel >= 0.9.8
BuildRequires:	oaf-devel >= 0.6.5
BuildRequires:	scrollkeeper >= 0.1.4
BuildRequires:	xpdf >= 0.90
Requires:	gnome-http
Requires:	GConf >= 1.0.2
Prereq:		/sbin/ldconfig
Prereq:		scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)
%define		_sysconfdir	/etc/X11/GNOME

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
Group(cs):	Vývojové prostøedky/Knihovny
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

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
Group(cs):	Vývojové prostøedky/Knihovny
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Static Nautilus libraries.

%description static -l pl
Biblioteki statyczne Nautilusa.

%package mozilla
Summary:	Nautilus component for use with Mozilla
Summary(pl):	Czê¶æ Nautilisa do u¿ywania z Mozill±
Group:		X11/Window Managers
Group(cs):	X11/Okenní mana¾ery
Group(de):	X11/Fenstermanager
Group(es):	X11/Administradores de Ventanas
Group(fr):	X11/Gestionnaires de fenêtres
Group(pl):	X11/Zarz±dcy okien
Group(pt):	X11/Gestores de Janelas
Group(ru):	X11/ïËÏÎÎÙÅ ÍÅÎÅÄÖÅÒÙ
Requires:	%{name} = %{version}
Requires:	mozilla >= 0.8
Conflicts:	mozilla = M18
Conflicts:	mozilla = M17

%description mozilla
This enables the use of embedded Mozilla as a Nautilus component.

%description mozilla -l pl
Ten pakiet pozwala na u¿ywanie wbudowanej Mozilli jako sk³adnika
Nautilusa.

%description mozilla -l pt_BR
Espe pacote permite a utilização do Mozilla como um componente
Nautilus.

%prep -q
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
rm -f missing
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
xml-i18n-toolize --force --copy --automake
libtoolize --copy --force
gettextize --force --copy
aclocal
autoconf
automake -a -c
CFLAGS="%{rpmcflags} -DENABLE_SCROLLKEEPER_SUPPORT"
CPPFLAGS="`/usr/bin/nspr-config --cflags`"; export CPPFLAGS
LDFLAGS="%{rpmldflags} `/usr/bin/nspr-config --libs`"
%configure \
	%{?debug:--enable-more-warnings} \
	%{!?debug:--disable-more-warnings} \
	--with-mozilla-lib-place=%{_libdir} \
	--with-mozilla-include-place=%{_includedir}/mozilla \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/omf/%{name}

gzip -9nf ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
scrollkeeper-update

%postun 
/sbin/ldconfig
scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gnome-db2html2
%attr(755,root,root) %{_bindir}/gnome-db2html3
%attr(755,root,root) %{_bindir}/gnome-info2html2
%attr(755,root,root) %{_bindir}/gnome-man2html2
%attr(755,root,root) %{_bindir}/hyperbola
%attr(755,root,root) %{_bindir}/nautilus
%attr(755,root,root) %{_bindir}/nautilus-adapter
%attr(755,root,root) %{_bindir}/nautilus-clean.sh
%attr(755,root,root) %{_bindir}/nautilus-content-loser
%attr(755,root,root) %{_bindir}/nautilus-error-dialog
%attr(755,root,root) %{_bindir}/nautilus-hardware-view
%attr(755,root,root) %{_bindir}/nautilus-history-view
%attr(755,root,root) %{_bindir}/nautilus-image-view
%attr(755,root,root) %{_bindir}/nautilus-launcher-applet
%attr(755,root,root) %{_bindir}/nautilus-music-view
%attr(755,root,root) %{_bindir}/nautilus-news
%attr(755,root,root) %{_bindir}/nautilus-notes
%attr(755,root,root) %{_bindir}/nautilus-preferences-applet
%attr(755,root,root) %{_bindir}/nautilus-restore-settings-to-default.sh
%attr(755,root,root) %{_bindir}/nautilus-sample-content-view
%attr(755,root,root) %{_bindir}/nautilus-sidebar-loser
%attr(755,root,root) %{_bindir}/nautilus-text-view
%attr(755,root,root) %{_bindir}/nautilus-throbber
%attr(755,root,root) %{_bindir}/nautilus-verify-rpm.sh
%attr(755,root,root) %{_bindir}/nautilus-xml-migrate
%attr(755,root,root) %{_bindir}/run-nautilus
%attr(755,root,root) %{_libdir}/libnautilus.so.*.*
%attr(755,root,root) %{_libdir}/libnautilus-*.so.*.*
%attr(755,root,root) %{_libdir}/libnautilus-*.so
%attr(755,root,root) %{_libdir}/vfs/modules/*.so
%attr(755,root,root) %{_libdir}/vfs/modules/*.la
%{_mandir}/man1/*
%{_sysconfdir}/vfs/modules/*.conf
%{_sysconfdir}/CORBA/servers/*
%{_applnkdir}/Utilities/*.desktop
%{_applnkdir}/Help/*.desktop
%{_datadir}/gnome/ui/*.xml
%{_datadir}/nautilus
%{_pixmapsdir}/*
%{_datadir}/oaf/Nautilus_ComponentAdapterFactory_std.oaf
%{_datadir}/oaf/Nautilus_Control_throbber.oaf
%{_datadir}/oaf/Nautilus_shell.oaf
%{_datadir}/oaf/Nautilus_View_content-loser.oaf
%{_datadir}/oaf/Nautilus_View_hardware.oaf
%{_datadir}/oaf/Nautilus_View_help.oaf
%{_datadir}/oaf/Nautilus_View_history.oaf
%{_datadir}/oaf/Nautilus_View_image.oaf
%{_datadir}/oaf/Nautilus_View_music.oaf
%{_datadir}/oaf/Nautilus_View_news.oaf
%{_datadir}/oaf/Nautilus_View_notes.oaf
%{_datadir}/oaf/Nautilus_View_sample.oaf
%{_datadir}/oaf/Nautilus_View_sidebar-loser.oaf
%{_datadir}/oaf/Nautilus_View_text.oaf
%{_datadir}/oaf/Nautilus_View_tree.oaf
%{_omf_dest_dir}/omf/%{name}
%{_datadir}/idl/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus.la
%attr(755,root,root) %{_libdir}/libnautilus.so
%attr(755,root,root) %{_libdir}/*.sh
%attr(755,root,root) %{_bindir}/nautilus-config
%{_includedir}/libnautilus

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/vfs/modules/*.a

%files mozilla
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nautilus-mozilla-content-view
%{_datadir}/oaf/Nautilus_View_mozilla.oaf
