%define name    ghostess
%define version 20100326
%define release %mkrel 1 

Name:           %{name} 
Summary:        Simple DSSI host with GUI capability
Version:        %{version} 
Release:        %{release}

Source:         http://smbolton.com/linux/%{name}-%{version}.tar.bz2
Patch0:         ghostess.strfmt.patch.bz2
URL:            http://smbolton.com/linux.html
License:        GPLv2
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
BuildRequires:  dssi-devel gtk+-devel liblo-devel alsa-lib-devel
BuildRequires:  ladspa-devel jackit-devel gtk2-devel

%description
Ghostess is a simple DSSI host with support for the plugin graphical
user interfaces. It can host several plugins, which can be attributed
to a dedicated MIDI channel. Refer to the README file for a brief 
introduction and a usage example.

%prep 
%setup -q  
%patch0 -p0

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


%changelog
* Mon Dec 18 2009 Frank Kober <emuse@mandriva.org> 20081213-1mdv2010.0
- import ghostess
