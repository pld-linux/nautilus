Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl):	nautilus - pow³oka GNOME i menad¿er plików
Summary(pt_BR):	Nautilus é um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	1.0.5
Release:	1
License:	GPL
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(pl):	X11/Zarz±dcy Okien
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-applnk.patch
Patch2:		%{name}-use_AM_GNU_GETTEXT.patch
Patch3:		%{name}-gmc.patch.bz2
Patch4:		%{name}-noflash.patch.bz2
Patch5:		%{name}-moz093.patch.bz2
URL:		http://nautilus.eazel.com/
BuildRequires:	GConf-devel >= 0.12
BuildRequires:	ORBit-devel >= 0.5.7
BuildRequires:	bonobo-devel >= 0.37
BuildRequires:	control-center-devel >= 1.3
BuildRequires:	esound-devel >= 0.2.22
BuildRequires:	gdk-pixbuf-devel >= 0.10.0
BuildRequires:	eel-devel >= 1.0.2
BuildRequires:	freetype-devel >= 2.0.1
BuildRequires:	gtk+-devel >= 1.2.9
BuildRequires:	imlib-devel >= 1.9.8
BuildRequires:	libxml-devel >= 1.8.10
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.11
BuildRequires:	gnome-vfs-devel >= 1.0.3
BuildRequires:	gnome-http-devel
BuildRequires:	gnome-core-devel >= 1.4.0.4
BuildRequires:	gnome-applets
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1.0.0
BuildRequires:	medusa-devel >= 0.5.1
BuildRequires:	mozilla-devel >= 0.8
BuildRequires:	oaf-devel >= 0.6.5
BuildRequires:	scrollkeeper >= 0.1.4
BuildRequires:	xpdf >= 0.90
BuildRequires:	automake
BuildRequires:	autoconf
Requires:	gnome-http
Requires:	GConf >= 1.0.2
Prereq:		/sbin/ldconfig
Prereq:		scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
Nautilus integrates access to files, applications, media,
Internet-based resources and the Web. Nautilus delivers a dynamic and
rich user experience. Nautilus is an free software project developed
under the GNU General Public License and is a core component of the
GNOME desktop project.

%description -l pl
GNU Nautilus jest mened¿erem plików i graficzn± pow³ok± dla GNOME.

%description -l pt_BR
O nautilus é um excelente gerenciador de arquivos para o GNOME.

%package devel
Summary:	Libraries and include files for developing Nautilus components
Summary(pt_BR):	Bibliotecas e arquivos para desenvolvimento com o nautilus
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop Nautilus components.

%description devel -l pl
Biblioteki i pliki nag³ówkowe potrzebne do programowania.

%description -l pt_BR devel
Este pacote fornece os arquivos necessários para desenvolvimento
utilizando componentes do nautilus.

%package static
Summary:	Static Nautilus libraries
Summary(pl):	Biblioteki statyczne Nautilusa
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Static Nautilus libraries.

%description -l pl static
Biblioteki statyczne Nautilusa.

%package mozilla
Summary:	Nautilus component for use with Mozilla
Summary(pl):	Czê¶æ Nautilisa do u¿ywania z Mozill±
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(pl):	X11/Zarz±dcy Okien
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
%patch2 -p0
#%patch3 -p1

# Dzimi removed this patch because its possibe hi is making a big with
# right panel in nautilus

#%patch4 -p1
#%patch5 -p1

%build
rm -f missing
CFLAGS="%{rpmcflags} -DENABLE_SCROLLKEEPER_SUPPORT"

aclocal
automake -a -c
%configure2_13 \
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
%attr(755,root,root) %{_bindir}/nautilus-clean.sh
%attr(755,root,root) %{_bindir}/nautilus-verify-rpm.sh
%attr(755,root,root) %{_bindir}/nautilus-restore-settings-to-default.sh
%attr(755,root,root) %{_bindir}/gnome-db2html2
%attr(755,root,root) %{_bindir}/gnome-info2html2
%attr(755,root,root) %{_bindir}/gnome-man2html2
%attr(755,root,root) %{_bindir}/hyperbola
%attr(755,root,root) %{_bindir}/nautilus
%attr(755,root,root) %{_bindir}/nautilus-adapter
%attr(755,root,root) %{_bindir}/nautilus-content-loser
%attr(755,root,root) %{_bindir}/nautilus-error-dialog
%attr(755,root,root) %{_bindir}/nautilus-hardware-view
%attr(755,root,root) %{_bindir}/nautilus-history-view
%attr(755,root,root) %{_bindir}/nautilus-image-view
%attr(755,root,root) %{_bindir}/nautilus-music-view
%attr(755,root,root) %{_bindir}/nautilus-news
%attr(755,root,root) %{_bindir}/nautilus-notes
%attr(755,root,root) %{_bindir}/nautilus-sample-content-view
%attr(755,root,root) %{_bindir}/nautilus-sidebar-loser
%attr(755,root,root) %{_bindir}/nautilus-text-view
%attr(755,root,root) %{_bindir}/nautilus-throbber
%attr(755,root,root) %{_bindir}/run-nautilus
%attr(755,root,root) %{_bindir}/nautilus-launcher-applet
%attr(755,root,root) %{_bindir}/nautilus-xml-migrate
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/vfs/modules/*.so
%{_mandir}/man1/*
%{_sysconfdir}/vfs/modules/*.conf
%{_sysconfdir}/CORBA/servers/*
%{_applnkdir}/Utilities/*.desktop
%{_datadir}/gnome/ui/*.xml
%{_datadir}/nautilus
%{_pixmapsdir}/*
%{_datadir}/oaf/Nautilus_View_help.oaf
%{_datadir}/oaf/Nautilus_ComponentAdapterFactory_std.oaf
%{_datadir}/oaf/Nautilus_View_content-loser.oaf
%{_datadir}/oaf/Nautilus_View_hardware.oaf
%{_datadir}/oaf/Nautilus_View_history.oaf
%{_datadir}/oaf/Nautilus_View_image.oaf
%{_datadir}/oaf/Nautilus_View_music.oaf
%{_datadir}/oaf/Nautilus_View_news.oaf
%{_datadir}/oaf/Nautilus_View_notes.oaf
%{_datadir}/oaf/Nautilus_View_sample.oaf
%{_datadir}/oaf/Nautilus_View_sidebar-loser.oaf
%{_datadir}/oaf/Nautilus_View_text.oaf
%{_datadir}/oaf/Nautilus_View_tree.oaf
%{_datadir}/oaf/Nautilus_shell.oaf
%{_datadir}/oaf/Nautilus_Control_throbber.oaf
%{_omf_dest_dir}/omf/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/vfs/modules/*.la
%attr(755,root,root) %{_libdir}/*.sh
%attr(755,root,root) %{_bindir}/nautilus-config
%{_includedir}/libnautilus
%{_datadir}/idl/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/vfs/modules/*.a

%files mozilla
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nautilus-mozilla-content-view
%{_datadir}/oaf/Nautilus_View_mozilla.oaf
