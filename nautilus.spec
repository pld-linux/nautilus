Summary:	nautilus - gnome shell and file manager
Summary(pl):	nautilus - pow³oka gnome i mened¿er plików
Name:		nautilus
Version:	0.1.0
Release:	1
License:	GPL
Group:		Utilities/File
Group(pl):	Narzêdzia/Pliki
Source0:	http://download.eazel.com/source/%{name}-%{version}.tar.gz
Patch0:		%{name}-mozpath.patch
URL:		http://nautilus.eazel.com/
BuildRequires:	ORBit-devel
BuildRequires:	w3c-libwww-devel >= 5.2.8
BuildRequires:	libghttp-devel >= 1.0.7
BuildRequires:	oaf-devel >= 0.5.1
BuildRequires:	GConf-devel >= 0.7
BuildRequires:	gnome-vfs-devel >= 0.3.1
BuildRequires:	bonobo-devel >= 0.18
BuildRequires:	gtkhtml-devel >= 0.6.1
BuildRequires:	medusa-devel >= 0.2
BuildRequires:	mozilla-devel >= 5.M17-3
BuildRequires:	gettext-devel
BuildRequires:	rpm-devel
BuildRequires:	db3-devel
BuildRequires:	binutils-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GNU Nautilus is a free software file manager and graphical shell for GNOME.

%description -l pl
GNU Nautilus jest mened¿erem plików i graficzn± pow³ok± dla GNOME.

%prep
%setup -q
%patch -p1

%build
autoconf
gettextize --force --copy
%configure

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
%{_applnkdir}/Utilities/*
