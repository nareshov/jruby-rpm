Name:    jruby
Version: 1.5.3
Release:  3.frameos
Summary:  Pure-Java Implementation of the Ruby Programming Language
Group:    Development/System 
License:  Multiple 
URL:      http://www.jruby.org 
Source0:  %{name}-bin-%{version}.tar.gz
Source1:  jruby
Source2:  jirb
Source3:  jrake
Source4:  jrdoc
Source5:  jrubyc
Source6:  jri
Source7:  jgem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: java-1.6.0-openjdk

%description
100% Pure-Java Implementation of the Ruby Programming Language

Features:
Ruby 1.8.7 Compatible
High performance
Real threading
Vast array of libraries


%prep
%setup -q

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/opt
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}/
cp %{SOURCE2}  $RPM_BUILD_ROOT/%{_bindir}/
cp %{SOURCE3} $RPM_BUILD_ROOT/%{_bindir}/
cp %{SOURCE4} $RPM_BUILD_ROOT/%{_bindir}/
cp %{SOURCE5} $RPM_BUILD_ROOT/%{_bindir}/
cp %{SOURCE6} $RPM_BUILD_ROOT/%{_bindir}/
cp %{SOURCE7} $RPM_BUILD_ROOT/%{_bindir}/
cp $RPM_BUILD_DIR/%{name}-%{version}/README $RPM_BUILD_ROOT/%{_docdir}/%{name}/
cp $RPM_BUILD_DIR/%{name}-%{version}/LICENSE.RUBY $RPM_BUILD_ROOT/%{_docdir}/%{name}/
cp $RPM_BUILD_DIR/%{name}-%{version}/COPYING $RPM_BUILD_ROOT/%{_docdir}/%{name}/
cp -r  $RPM_BUILD_DIR/%{name}-%{version} $RPM_BUILD_ROOT/opt/jruby
cp -r $RPM_BUILD_DIR/%{name}-%{version}/docs/* $RPM_BUILD_ROOT/%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}
/opt/jruby
/usr/bin

%changelog
* Fri Oct 15 2010 Sergio Rubio <rubiojr@frameos.org> 1.5.3-3
- Fixed wrapper scripts

* Fri Oct 15 2010 Sergio Rubio <rubiojr@frameos.org> 1.5.3-2
- Install jgem wrapper script

* Fri Oct 15 2010 Sergio Rubio <rubiojr@frameos.org> 1.5.3-1
- Initial release
