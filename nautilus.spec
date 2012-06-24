# Note that this is NOT a relocatable package
%define name		nautilus
%define ver		1.0.4
%define RELEASE		0_cvs_0
%define rel		%{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}

Name:		%name
Vendor:		GNOME
Distribution:	CVS
Summary:	Nautilus is a network user environment
Summary(pl):	nautilus - pow�oka gnome i menad�er plik�w

Version: 	%ver
Release: 	%rel
Copyright: 	GPL
Group:		User Interface/Desktop
Source: 	ftp://ftp.gnome.org/pub/GNOME/stable/sources/%{name}-%{ver}.tar.gz
URL: 		http://nautilus.eazel.com/
BuildRoot:	/var/tmp/%{name}-%{ver}-root
Requires:	glib >= 1.2.9
Requires:	gtk+ >= 1.2.9
Requires:	imlib >= 1.9.8
Requires:	libxml >= 1.8.10
Requires:	gnome-libs >= 1.2.11
Requires:	GConf >= 0.12
Requires:	ORBit >= 0.5.7
Requires:	oaf >= 0.6.5
Requires:	gnome-vfs >= 1.0.1
Requires:	gdk-pixbuf >= 0.10.0
Requires:	bonobo >= 0.37
Requires:	popt >= 1.5
Requires:	freetype >= 2.0.1
Requires:	medusa >= 0.5.1
Requires:	esound >= 0.2.22
Requires:	scrollkeeper >= 0.1.4
Requires:	libpng
Requires:	control-center >= 1.3
Requires:	librsvg >= 1.0.0
Requires:	eel >= 1.0

BuildRequires:	glib-devel >= 1.2.9
BuildRequires:	gtk+-devel >= 1.2.9
BuildRequires:	imlib-devel >= 1.9.8
BuildRequires:	libxml-devel >= 1.8.10
BuildRequires:	gnome-libs-devel >= 1.2.11
BuildRequires:	GConf-devel >= 0.12
BuildRequires:	ORBit-devel >= 0.5.7
BuildRequires:	oaf-devel >= 0.6.5
BuildRequires:	gnome-vfs-devel >= 1.0.1
BuildRequires:	gdk-pixbuf-devel >= 0.10.0
BuildRequires:	bonobo-devel >= 0.37
BuildRequires:	popt >= 1.5
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

%description
Nautilus integrates access to files, applications, media, Internet-based
resources and the Web.  Nautilus delivers a dynamic and rich user
experience.  Nautilus is an free software project developed under the
GNU General Public License and is a core component of the GNOME desktop
project.

%description -l pl
GNU Nautilus jest mened�erem plik�w i graficzn� pow�ok� dla GNOME.

%package devel
Summary:	Libraries and include files for developing Nautilus components
Group:		Development/Libraries
Requires:	%name = %{PACKAGE_VERSION}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop Nautilus components.

%description devel -l pl
Biblioteki i pliki nag��wkowe potrzebne do programowania.

%package mozilla
Summary:        Nautilus component for use with Mozilla
Group:          User Interface/Desktop
Requires:       %name = %{PACKAGE_VERSION}
Requires:	mozilla >= 0.8
Conflicts:	mozilla = M18
Conflicts:	mozilla = M17

%description mozilla
This enables the use of embedded Mozilla as a Nautilus component.

%package extras
Summary:	Extra goodies to use with Nautilus
Group:          User Interface/Desktop
Requires:	xpdf >= 0.90

%description extras
This is a meta-package that requires useful add-ons for Nautilus.

%package suggested
Summary:	Nautilus and a suggested set of components
Group:          User Interface/Desktop
Requires:       %name = %{PACKAGE_VERSION}
Requires:	%name-mozilla = %{PACKAGE_VERSION}
##
## FIXME: We need to deal with the fact that trilobite builds after
##        nautilus.
##
##Requires:	%name-trilobite = %{PACKAGE_VERSION}
Requires:	%name-extras = %{PACKAGE_VERSION}

%description suggested
This is a meta-package that requires packages useful for running
Nautilus, and getting multimedia to work, such as eog and mpg123.

%prep
%setup

%build
%ifarch alpha
	MYARCH_FLAGS="--host=alpha-redhat-linux"
%endif

LC_ALL=""
LINGUAS=""
LANG=""
export LC_ALL LINGUAS LANG

## Warning!  Make sure there are no spaces or tabs after the \ 
## continuation character, or else the rpm demons will eat you.
CFLAGS="$RPM_OPT_FLAGS -DENABLE_SCROLLKEEPER_SUPPORT" ./configure \
    $MYARCH_FLAGS --enable-more-warnings \
    --prefix=%{_prefix} --datadir=%{_datadir} \
    --sysconfdir=%{_sysconfdir} --includedir=%{_includedir} \
    --libdir=%{_libdir} --bindir=%{_bindir}

make -k
make check

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

make -k prefix=$RPM_BUILD_ROOT/%{_prefix} \
    sysconfdir=$RPM_BUILD_ROOT/%{_sysconfdir} \
    datadir=$RPM_BUILD_ROOT/%{_datadir} \
    includedir=$RPM_BUILD_ROOT/%{_includedir} \
    libdir=$RPM_BUILD_ROOT/%{_libdir} \
    bindir=$RPM_BUILD_ROOT/%{_bindir} install

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post
if ! grep %{_libdir} /etc/ld.so.conf > /dev/null ; then
	echo "%{_libdir}" >> /etc/ld.so.conf
fi
/sbin/ldconfig
scrollkeeper-update

%postun -p /sbin/ldconfig
scrollkeeper-update

%files

%defattr(0555, bin, bin)
%doc AUTHORS COPYING COPYING-DOCS COPYING.LIB TRADEMARK_NOTICE ChangeLog NEWS README
%{_bindir}/nautilus-clean.sh
%{_bindir}/nautilus-verify-rpm.sh
%{_bindir}/nautilus-restore-settings-to-default.sh
%{_bindir}/gnome-db2html2
%{_bindir}/gnome-info2html2
%{_bindir}/gnome-man2html2
%{_bindir}/hyperbola
%{_bindir}/nautilus
%{_bindir}/nautilus-adapter
%{_bindir}/nautilus-content-loser
%{_bindir}/nautilus-error-dialog
%{_bindir}/nautilus-hardware-view
%{_bindir}/nautilus-history-view
%{_bindir}/nautilus-image-view
# %{_bindir}/nautilus-mpg123
%{_bindir}/nautilus-music-view
%{_bindir}/nautilus-news
%{_bindir}/nautilus-notes
%{_bindir}/nautilus-sample-content-view
%{_bindir}/nautilus-sidebar-loser
%{_bindir}/nautilus-text-view
%{_bindir}/nautilus-throbber
%{_bindir}/run-nautilus
%{_bindir}/nautilus-launcher-applet
%{_bindir}/nautilus-xml-migrate
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
%{_datadir}/gnome/apps/Applications/*.desktop
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

%defattr(0555, bin, bin)
%{_libdir}/*.la
%{_libdir}/vfs/modules/*.la
%{_libdir}/*.sh
%{_bindir}/nautilus-config

%defattr(0444, bin, bin)
%{_includedir}/libnautilus/*.h

%files mozilla

%defattr(0555, bin, bin)
%{_bindir}/nautilus-mozilla-content-view

%defattr(0444, bin, bin)
%{_datadir}/oaf/Nautilus_View_mozilla.oaf

%files extras

%defattr(0444, bin, bin)
%{_datadir}/nautilus/nautilus-extras.placeholder

%files suggested

%defattr(0444, bin, bin)
%{_datadir}/nautilus/nautilus-suggested.placeholder

%changelog
* %{date} PLD Team <pld-list@pld.org.pl>
All persons listed below can be reached at <cvs_login>@pld.org.pl

$Log: nautilus.spec,v $
Revision 1.13  2001-07-21 10:16:15  dzimi

update to version 1.0.4

Revision 1.12  2001/04/14 09:59:45  kura
- release 2
- added BuildRequires: xml-i18n-tools

Revision 1.11  2001/04/08 17:48:49  misiek
corba removed

Revision 1.10  2001/04/07 17:03:56  misiek
oaf moved to main package

Revision 1.9  2001/04/07 16:50:12  misiek
missing attr

Revision 1.8  2001/04/07 16:47:03  misiek
should build ok, now

Revision 1.7  2001/04/01 22:28:38  misiek
started update to 1.0. Added almost 30 BuildRequires. %%build section
is ok; %%install may require DESTDIR patch update; %%files isn't
updated at all. Any volunteers to finish it?

Revision 1.6  2001/03/20 01:00:03  qboosh
- s/freetype2-devel/freetype-devel >= 2.0/

Revision 1.5  2000/11/19 23:38:16  michuz
- added %%post and %%postun field

Revision 1.4  2000/11/19 23:27:45  michuz
- updated to 0.5
- added devel package

Revision 1.3  2000/09/18 16:07:13  wrobell
- fixed buildrequires

Revision 1.2  2000/09/13 14:38:40  michuz
- added mozilla support (still not finished)

Revision 1.1  2000/09/06 11:05:27  michuz
- initial release (not finished yet)
