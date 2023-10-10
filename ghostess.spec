Name:           ghostess
Summary:        Simple DSSI host with GUI capability
Version:        20210101
Release:        1

Source:         http://smbolton.com/linux/%{name}-%{version}.tar.bz2
URL:            http://smbolton.com/linux.html
License:        GPLv2
Group:          Sound

BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  ladspa-devel

%description
Ghostess is a simple DSSI host with support for the plugin graphical
user interfaces. It can host several plugins, which can be attributed
to a dedicated MIDI channel. Refer to the README file for a brief
introduction and a usage example.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS
%{_bindir}/%{name}
%{_bindir}/%{name}_universal_gui
%{_mandir}/man1/ghostess.1.*


%changelog
* Fri Apr 27 2012 Frank Kober <emuse@mandriva.org> 20120105-2
+ Revision: 793822
- rebuild, spec cleanup

* Thu Feb 16 2012 Frank Kober <emuse@mandriva.org> 20120105-1
+ Revision: 775394
- new version 20120105

* Mon Sep 19 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 20100923-2
+ Revision: 700419
- do not restrict manpages to lzma

* Sat Sep 25 2010 Frank Kober <emuse@mandriva.org> 20100923-1mdv2011.0
+ Revision: 581021
- new version 20100923
  o drop patch0 (fixed upstream)
  o install manpage

* Fri Apr 16 2010 Frank Kober <emuse@mandriva.org> 20100326-1mdv2010.1
+ Revision: 535352
- use configure2_5x instead of autoreconf, fix lost BR
- new version 20100326

* Mon Dec 21 2009 Frank Kober <emuse@mandriva.org> 20081213-1mdv2010.1
+ Revision: 480892
- Add missing BR for gtk2
- Update rpm group tag
- import ghostess


* Mon Dec 18 2009 Frank Kober <emuse@mandriva.org> 20081213-1mdv2010.0
- import ghostess
