Summary:	nautilus - gnome shell and file manager
Summary(pl):	nautilus - pow³oka gnome i mened¿er plików
Name:		nautilus
Version:	0.5
Release:	1
License:	GPL
Group:		Utilities/File
Group(pl):	Narzêdzia/Pliki
Source0:	http://download.eazel.com/source/%{name}-%{version}.tar.gz
Patch0:		%{name}-bonobo.patch
URL:		http://nautilus.eazel.com/
BuildRequires:	ORBit-devel
BuildRequires:	w3c-libwww-devel >= 5.2.8
BuildRequires:	libghttp-devel >= 1.0.7
BuildRequires:	oaf-devel >= 0.6.0
BuildRequires:	GConf-devel >= 0.11
BuildRequires:	gnome-vfs-devel >= 0.4.2
BuildRequires:	libunicode-devel >= 0.4
BuildRequires:	bonobo-devel >= 0.28
BuildRequires:	medusa-devel >= 0.2.2
BuildRequires:	mozilla-devel >= 0.0.M18
BuildRequires:	gettext-devel
BuildRequires:	rpm-devel
BuildRequires:	db1-devel
BuildRequires:	db3-devel
BuildRequires:	freetype2-devel >= 2.0
BuildRequires:	binutils-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GNU Nautilus is a free software file manager and graphical shell for GNOME.

%description -l pl
GNU Nautilus jest mened¿erem plików i graficzn± pow³ok± dla GNOME.

%package devel
Summary:	Libraries and header files for developing
Summary(pl):	Biblioteki i pliki nag³ówkowe
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries and header files needed for developing.

%description devel -l pl
Biblioteki i pliki nag³ówkowe potrzebne do programowania.

%prep
%setup -q
%patch0 -p1

%build
gettextize --force --copy
%configure
#	--with-mozilla-include-place=%{_includedir}/mozilla \
#	--with-mozilla-lib-place=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Utilities

%find_lang %{name}

gzip -9nf AUTHORS ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%{_sysconfdir}/vfs/modules/*
%attr(0755,root,root) %{_bindir}/*
%attr(0755,root,root) %{_libdir}/vfs/modules/*
%attr(0755,root,root) %{_libdir}/lib*.so.*.*
%{_applnkdir}/Utilities/*
%{_datadir}/gnome/help/%{name}
%{_datadir}/gnome/ui/*
%{_datadir}/hyperbola
%{_datadir}/%{name}
%{_datadir}/oaf/*
%{_pixmapsdir}/*.png
%{_pixmapsdir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/libnautilus
%{_libdir}/*.la
%{_libdir}/*.so
