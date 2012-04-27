Name:           ghostess
Summary:        Simple DSSI host with GUI capability
Version:        20120105
Release:        2

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
