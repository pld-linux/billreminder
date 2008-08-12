Summary:	BillReminder - a desktop bill reminder for GNOME
Name:		billreminder
Version:	0.3.1
Release:	1
License:	Other
Group:		X11/Applications
Source0:	http://billreminder.googlecode.com/files/%{name}-%{version}-1.tar.bz2
# Source0-md5:	c023fdc33c8eea05d1ff59d282efa431
URL:		http://billreminder.gnulinuxbrasil.org/
BuildRequires:	GConf2-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-gnome-devel >= 2.6.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.5
BuildRequires:	python-gnome-desktop
BuildRequires:	python-gnome-extras-gtkspell
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
%pyrequires_eq	python-modules
Requires:	python-gnome-extras-gtkspell
Requires:	python-gnome-desktop-print
Requires:	python-gnome-ui >= 2.12.2-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A desktop bill reminder for GNOME.

%prep
%setup -q
mv po/{no,nb}.po
rm -rf po/no_NB.po
sed -i 's/no_NB//g;s/no/nb/g' po/LINGUAS
rm src/lib/sysvars.py

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%{configure}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/billreminder/*.py
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/billreminder/daemon/*.py
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/billreminder/db/*.py
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/billreminder/gui/*.py
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/billreminder/gui/widgets/*.py
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/billreminder/lib/*.py
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/hicolor/20x20

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
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
%{_datadir}/dbus-1/services/billreminder.service
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*.1*
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_pixmapsdir}/billreminder.png
