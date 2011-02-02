Summary:	BillReminder - a desktop bill reminder for GNOME
Name:		billreminder
Version:	0.3.2
Release:	4
License:	BSD
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/billreminder/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	dddf919af92bc778d823b92f63e50dd9
URL:		http://billreminder.gnulinuxbrasil.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	python-dbus
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pygobject
BuildRequires:	python-sqlite >= 2.3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
%pyrequires_eq	python-modules
Requires:	python-dbus
Requires:	python-gnome
Requires:	python-pygtk-gtk
Requires:	python-sqlite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A desktop bill reminder for GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/hicolor/20x20

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%gconf_schema_install billreminder.schemas

%preun
%gconf_schema_uninstall billreminder.schemas

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README TODO
%attr(755,root,root) %{_bindir}/billreminder
%attr(755,root,root) %{_bindir}/billreminderd
/etc/xdg/autostart/billreminderd.desktop
%dir %{py_sitescriptdir}/billreminder
%{py_sitescriptdir}/billreminder/*.py[co]
%dir %{py_sitescriptdir}/billreminder/daemon
%{py_sitescriptdir}/billreminder/daemon/*.py[co]
%dir %{py_sitescriptdir}/billreminder/db
%{py_sitescriptdir}/billreminder/db/*.py[co]
%dir %{py_sitescriptdir}/billreminder/gui
%{py_sitescriptdir}/billreminder/gui/*.py[co]
%dir %{py_sitescriptdir}/billreminder/gui/widgets
%{py_sitescriptdir}/billreminder/gui/widgets/*.py[co]
%dir %{py_sitescriptdir}/billreminder/lib
%{py_sitescriptdir}/billreminder/lib/*.py[co]
%{_sysconfdir}/gconf/schemas/billreminder.schemas
%{_datadir}/dbus-1/services/billreminder.service
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*.1*
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_pixmapsdir}/billreminder.png
