# Note that this is NOT a relocatable package

Summary:	Nautilus is a network user environment
Summary(pl):	nautilus - pow³oka gnome i menad¿er plików
Name:		nautilus
Version:	1.0.4
Release:	1
License:	GPL
Vendor:		GNOME
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(pl):	X11/Zarz±dcy Okien
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://nautilus.eazel.com/
BuildRequires:	glib-devel >= 1.2.9
BuildRequires:	gtk+-devel >= 1.2.9
BuildRequires:	imlib-devel >= 1.9.8
BuildRequires:	libxml-devel >= 1.8.10
BuildRequires:	gdk-pixbuf-devel >= 0.10.0
BuildRequires:	gnome-libs-devel >= 1.2.11
BuildRequires:	gnome-vfs-devel >= 1.0
BuildRequires:	gnome-http-devel
BuildRequires:	GConf-devel >= 0.12
BuildRequires:	ORBit-devel >= 0.5.7
BuildRequires:	oaf-devel >= 0.6.5
BuildRequires:	bonobo-devel >= 0.37
BuildRequires:	popt-devel >= 1.5
BuildRequires:	freetype-devel >= 2.0.1
BuildRequires:	medusa-devel >= 0.5.1
BuildRequires:	esound-devel >= 0.2.22
BuildRequires:	scrollkeeper >= 0.1.4
BuildRequires:	libpng-devel
BuildRequires:	control-center-devel >= 1.3
BuildRequires:	librsvg-devel >= 1.0.0
BuildRequires:	eel-devel >= 1.0
BuildRequires:	mozilla-devel >= 0.8
BuildRequires:	xpdf >= 0.90
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Nautilus integrates access to files, applications, media,
Internet-based resources and the Web. Nautilus delivers a dynamic and
rich user experience. Nautilus is an free software project developed
under the GNU General Public License and is a core component of the
GNOME desktop project.

%description -l pl
GNU Nautilus jest mened¿erem plików i graficzn± pow³ok± dla GNOME.

%package devel
Summary:	Libraries and include files for developing Nautilus components
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%name = %{version}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop Nautilus components.

%description devel -l pl
Biblioteki i pliki nag³ówkowe potrzebne do programowania.

%package mozilla
Summary:	Nautilus component for use with Mozilla
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(pl):	X11/Zarz±dcy Okien
Requires:	%name = %{version}
Requires:	mozilla >= 0.8
Conflicts:	mozilla = M18
Conflicts:	mozilla = M17

%description mozilla
This enables the use of embedded Mozilla as a Nautilus component.

%package extras
Summary:	Extra goodies to use with Nautilus
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(pl):	X11/Zarz±dcy Okien
Requires:	xpdf >= 0.90

%description extras
This is a meta-package that requires useful add-ons for Nautilus.

%package suggested
Summary:	Nautilus and a suggested set of components
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(pl):	X11/Zarz±dcy Okien
Requires:	%name = %{version}
Requires:	%name-mozilla = %{version}
##
## FIXME: We need to deal with the fact that trilobite builds after
##        nautilus.
##
##Requires:	%name-trilobite = %{version}
Requires:	%name-extras = %{version}

%description suggested
This is a meta-package that requires packages useful for running
Nautilus, and getting multimedia to work, such as eog and mpg123.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} -DENABLE_SCROLLKEEPER_SUPPORT"

%configure \
	--enable-more-warnings \
	--prefix=%{_prefix} \
	--datadir=%{_datadir} \
	--sysconfdir=%{_sysconfdir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--bindir=%{_bindir} \
%ifarch alpha
	--host=alpha-redhat-linux
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install
#    sysconfdir=$RPM_BUILD_ROOT/%{_sysconfdir} \
#   datadir=$RPM_BUILD_ROOT/%{_datadir} \
#    includedir=$RPM_BUILD_ROOT/%{_includedir} \
#    libdir=$RPM_BUILD_ROOT/%{_libdir} \
#    bindir=$RPM_BUILD_ROOT/%{_bindir} install

gzip -9nf 
%doc AUTHORS COPYING COPYING-DOCS COPYING.LIB TRADEMARK_NOTICE ChangeLog NEWS README

%post
if ! grep %{_libdir} /etc/ld.so.conf > /dev/null ; then
	echo "%{_libdir}" >> /etc/ld.so.conf
fi
/sbin/ldconfig
scrollkeeper-update

%postun -p /sbin/ldconfig
scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%defattr(0555, bin, bin)
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
# %{_bindir}/nautilus-mpg123
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
%{_libdir}/libnautilus-adapter.so.0
%{_libdir}/libnautilus-adapter.so.0.0.0
%{_libdir}/libnautilus-private.so.0
%{_libdir}/libnautilus-private.so.0.0.0
%{_libdir}/libnautilus-tree-view.so.0
%{_libdir}/libnautilus-tree-view.so.0.0.0
%{_libdir}/libnautilus.so.0
%{_libdir}/libnautilus.so.0.0.0
%{_libdir}/libnautilus-adapter.so
%{_libdir}/libnautilus-private.so
%{_libdir}/libnautilus-tree-view.so
%{_libdir}/libnautilus.so



%{_libdir}/vfs/modules/*.so


%defattr (0444, bin, bin)
%config %{_sysconfdir}/vfs/modules/*.conf
%config %{_sysconfdir}/CORBA/servers/nautilus-launcher-applet.gnorba
%{_applnkdir}/Applications/*.desktop
%{_datadir}/gnome/ui/*.xml
%{_datadir}/nautilus/components/hyperbola/maps/*.map
%{_datadir}/nautilus/components/hyperbola/*.xml
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/nautilus/*.xml
%{_datadir}/nautilus/emblems/*.png
%{_datadir}/nautilus/linksets/*.xml
%{_datadir}/nautilus/patterns/*.jpg
%{_datadir}/nautilus/patterns/*.png
%{_datadir}/nautilus/patterns/.*.png
%{_datadir}/nautilus/services/text/*.xml
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/nautilus/*.gif
%{_datadir}/pixmaps/nautilus/*.png
%{_datadir}/pixmaps/nautilus/*.svg
%{_datadir}/pixmaps/nautilus/*.xml
%{_datadir}/pixmaps/nautilus/tahoe/*.png
%{_datadir}/pixmaps/nautilus/tahoe/*.xml
%{_datadir}/pixmaps/nautilus/crux_teal/*.png
%{_datadir}/pixmaps/nautilus/crux_teal/*.xml
%{_datadir}/pixmaps/nautilus/crux_teal/throbber/*.png
%{_datadir}/pixmaps/nautilus/crux_teal/backgrounds/*.png
%{_datadir}/pixmaps/nautilus/crux_teal/sidebar_tab_pieces/*.png
%{_datadir}/pixmaps/nautilus/crux_eggplant/*.png
%{_datadir}/pixmaps/nautilus/crux_eggplant/*.xml
%{_datadir}/pixmaps/nautilus/crux_eggplant/throbber/*.png
%{_datadir}/pixmaps/nautilus/crux_eggplant/backgrounds/*.png
%{_datadir}/pixmaps/nautilus/crux_eggplant/sidebar_tab_pieces/*.png
%{_datadir}/pixmaps/nautilus/eazel-logos/*.png
%{_datadir}/pixmaps/nautilus/eazel-logos/*.xml
%{_datadir}/pixmaps/nautilus/eazel-logos/throbber/*.png
%{_datadir}/pixmaps/nautilus/eazel-logos/LICENSE
%{_datadir}/pixmaps/nautilus/gnome/*.png
%{_datadir}/pixmaps/nautilus/gnome/*.xml
%{_datadir}/pixmaps/nautilus/gnome/throbber/*.png
%{_datadir}/pixmaps/nautilus/sidebar_tab_pieces/*.png
%{_datadir}/pixmaps/nautilus/throbber/*.png
%{_datadir}/pixmaps/nautilus/sierra/*.xml
%{_datadir}/pixmaps/nautilus/sierra/*.png
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

# We put the idl files in the main package, not the devel package
# because the perl corba bindings can use the .idl files at run time.
%{_datadir}/idl/nautilus-view-component.idl
%{_datadir}/idl/nautilus-distributed-undo.idl

%defattr (-, root, root)
%{_datadir}/gnome/help
%{_datadir}/omf/nautilus

%files devel
%defattr(644,root,root,755)

%defattr(0555, bin, bin)
%{_libdir}/*.la
%{_libdir}/vfs/modules/*.la
%{_libdir}/*.sh
%attr(755,root,root) %{_bindir}/nautilus-config

%defattr(0444, bin, bin)
%{_includedir}/libnautilus/*.h

%files mozilla
%defattr(644,root,root,755)

%defattr(0555, bin, bin)
%attr(755,root,root) %{_bindir}/nautilus-mozilla-content-view

%defattr(0444, bin, bin)
%{_datadir}/oaf/Nautilus_View_mozilla.oaf

%files extras
%defattr(644,root,root,755)

%defattr(0444, bin, bin)
%{_datadir}/nautilus/nautilus-extras.placeholder

%files suggested
%defattr(644,root,root,755)

%defattr(0444, bin, bin)
%{_datadir}/nautilus/nautilus-suggested.placeholder
