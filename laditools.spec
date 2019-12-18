%global commit 2946670cbc89f56f2e98675fa1815952665684c8
%global shortcommit0 %(c=%{commit}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:          laditools
Summary:       Set of tools to control and monitor LADI system
Version:       1.1.0
Release:       7%{?gver}%{dist}
License:       GPLv3+
URL:           https://github.com/alessio/laditools
Source0:       https://github.com/alessio/laditools/archive/%{commit}/%{name}-%{version}-%{shortcommit0}.tar.gz

BuildArch:     noarch

BuildRequires: /usr/bin/rsvg-convert
BuildRequires: python2-devel
BuildRequires: intltool
BuildRequires: python2-distutils-extra
BuildRequires: librsvg2
BuildRequires: desktop-file-utils

BuildRequires: python2-pip

Requires:      a2jmidid
Requires:      hicolor-icon-theme
Requires:      jack-audio-connection-kit-dbus
# Thanks to deprecations in python2, various modules will be died, A bundle with pip; why not?
Requires:      python2-enum34
Requires:      python2-pyxdg


%description
LADITools is a set of tools aiming to achieve the goals of the LADI 
project to improve desktop integration and user workflow of Linux 
audio system based on JACK and ladish. Those tools take advantage of 
the D-Bus interfaces recently added to JACK and ladish to ease the 
configuration and use of those two great softwares.

#----------

%package -n     python2-enum34
Version:	1.1.6
Summary:        Python 3.4 Enum backported
Url:		https://pypi.python.org/pypi/enum34

%description -n python2-enum34
An enumeration is a set of symbolic names (members) bound to unique, constant 
values. Within an enumeration, the members can be compared by identity, and the 
enumeration itself can be iterated over.

#----------

%package -n     python2-pyxdg
Version:	0.26
Summary:        Python library to access freedesktop.org standards
Url:		https://freedesktop.org/Software/pyxdg
Provides:	python2-xdg = %{version}

%description -n python2-pyxdg
PyXDG is a python library to access freedesktop.org standards.

#----------

%prep
%autosetup -n %{name}-%{commit}

%build

# Python2 fixes (nop, python3 isn't ready)
find -depth -type f -writable -name "*.py" -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{__python2}=' {} +

%install
%{__python2} setup.py install --prefix=%{buildroot}%{_prefix}
%find_lang %{name}

for i in `ls %{buildroot}%{_datadir}/applications/*.desktop` ; do \
    desktop-file-validate $i;
done;


python2 -m pip install --user enum34 pyxdg
pushd $HOME
cp -rf .local/lib/python2.7/site-packages/* %{buildroot}/%{python2_sitelib}/
popd


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/g15ladi
%{_bindir}/ladi-control-center
%{_bindir}/ladi-player
%{_bindir}/ladi-system-tray
%{_bindir}/ladi-system-log
%{_bindir}/wmladi
%{python2_sitelib}/laditools/
%{python2_sitelib}/laditools-*.egg-info
%{_datadir}/applications/ladi-system-tray.desktop
%{_datadir}/applications/ladi-control-center.desktop
%{_datadir}/applications/ladi-system-log.desktop
%{_datadir}/applications/ladi-player.desktop
%{_datadir}/laditools/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/status/*
%{_mandir}/man1/%{name}.1.*

# Thanks to deprecations in python2, various modules will be died A bundle with pip; why not?

%files -n python2-enum34
%{python2_sitelib}/enum/LICENSE
%{python2_sitelib}/enum/README
%{python2_sitelib}/enum/__init__.py
%{python2_sitelib}/enum/__init__.pyc
%{python2_sitelib}/enum/__init__.pyo
%{python2_sitelib}/enum34-1.1.6.dist-info/DESCRIPTION.rst
%{python2_sitelib}/enum34-1.1.6.dist-info/INSTALLER
%{python2_sitelib}/enum34-1.1.6.dist-info/METADATA
%{python2_sitelib}/enum34-1.1.6.dist-info/RECORD
%{python2_sitelib}/enum34-1.1.6.dist-info/WHEEL
%{python2_sitelib}/enum34-1.1.6.dist-info/metadata.json
%{python2_sitelib}/enum34-1.1.6.dist-info/top_level.txt

%files -n python2-pyxdg
%{python2_sitelib}/pyxdg-0.26.dist-info/DESCRIPTION.rst
%{python2_sitelib}/pyxdg-0.26.dist-info/INSTALLER
%{python2_sitelib}/pyxdg-0.26.dist-info/METADATA
%{python2_sitelib}/pyxdg-0.26.dist-info/RECORD
%{python2_sitelib}/pyxdg-0.26.dist-info/WHEEL
%{python2_sitelib}/pyxdg-0.26.dist-info/metadata.json
%{python2_sitelib}/pyxdg-0.26.dist-info/top_level.txt
%{python2_sitelib}/xdg/BaseDirectory.py
%{python2_sitelib}/xdg/BaseDirectory.pyc
%{python2_sitelib}/xdg/BaseDirectory.pyo
%{python2_sitelib}/xdg/Config.py
%{python2_sitelib}/xdg/Config.pyc
%{python2_sitelib}/xdg/Config.pyo
%{python2_sitelib}/xdg/DesktopEntry.py
%{python2_sitelib}/xdg/DesktopEntry.pyc
%{python2_sitelib}/xdg/DesktopEntry.pyo
%{python2_sitelib}/xdg/Exceptions.py
%{python2_sitelib}/xdg/Exceptions.pyc
%{python2_sitelib}/xdg/Exceptions.pyo
%{python2_sitelib}/xdg/IconTheme.py
%{python2_sitelib}/xdg/IconTheme.pyc
%{python2_sitelib}/xdg/IconTheme.pyo
%{python2_sitelib}/xdg/IniFile.py
%{python2_sitelib}/xdg/IniFile.pyc
%{python2_sitelib}/xdg/IniFile.pyo
%{python2_sitelib}/xdg/Locale.py
%{python2_sitelib}/xdg/Locale.pyc
%{python2_sitelib}/xdg/Locale.pyo
%{python2_sitelib}/xdg/Menu.py
%{python2_sitelib}/xdg/Menu.pyc
%{python2_sitelib}/xdg/Menu.pyo
%{python2_sitelib}/xdg/MenuEditor.py
%{python2_sitelib}/xdg/MenuEditor.pyc
%{python2_sitelib}/xdg/MenuEditor.pyo
%{python2_sitelib}/xdg/Mime.py
%{python2_sitelib}/xdg/Mime.pyc
%{python2_sitelib}/xdg/Mime.pyo
%{python2_sitelib}/xdg/RecentFiles.py
%{python2_sitelib}/xdg/RecentFiles.pyc
%{python2_sitelib}/xdg/RecentFiles.pyo
%{python2_sitelib}/xdg/__init__.py
%{python2_sitelib}/xdg/__init__.pyc
%{python2_sitelib}/xdg/__init__.pyo
%{python2_sitelib}/xdg/util.py
%{python2_sitelib}/xdg/util.pyc
%{python2_sitelib}/xdg/util.pyo


%changelog

* Tue Dec 10 2019 David Va <davidva AT tuta DOT io> - 1.1.0-7-git2946670
- sub-packages enabled

* Tue Dec 10 2019 David Va <davidva AT tuta DOT io> - 1.1.0-5-git2946670
- Updated to current commit
- Spec cleaned

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3.20160307git97b8cf3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May  6 2019 Orion Poplawski <orion@nwra.com> - 1.1.0-2.20160307git97b8cf3
- Add requires python2-pyxdg (bugz#1599929)

* Mon May  6 2019 Orion Poplawski <orion@nwra.com> - 1.1.0-1.20160307git97b8cf3
- Update to latest git (bugz#1675246)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.1-16
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-15
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0.1-8
- Add BR: /usr/bin/rsvg-convert (Fix FTBFS RHBZ #992030).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 14 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.1-5
- Correct license 

* Sun Oct 14 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.1-4
- Add python build requires

* Sun Oct 14 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.1-3
- Add mising desktop-file-utils and python-enum

* Sun Jun 03 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.1-2
- Add requires and scriptlets

* Sat Jun 02 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.1-1
- initial build
