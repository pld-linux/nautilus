Summary:	Nautilus is a file manager for the GNOME desktop environment
Summary(pl):	nautilus - pow³oka GNOME i menad¿er plików
Summary(pt_BR):	Nautilus é um gerenciador de arquivos para o GNOME
Name:		nautilus
Version:	1.1.13
Release:	0.1
License:	GPL
Group:		X11/Window Managers
Source0:	%{name}/%{name}-%{version}.tar.bz2
URL:		http://nautilus.eazel.com/
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-activation-devel
BuildRequires:	eel-devel
BuildRequires:	esound-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
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
%configure \
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
%{_omf_dest_dir}/%{name}
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
