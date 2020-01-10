Name: hunspell-el
Summary: Greek hunspell dictionaries
Epoch: 1
Version: 0.8
Release: 7%{?dist}
Source: http://ispell.math.upatras.gr/files/ooffice/el_GR-%{version}.zip
Group: Applications/Text
URL: http://ispell.math.upatras.gr/?section=oofficespell&subsection=howto
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Greek hunspell dictionaries.

%prep
%setup -q -c -n hunspell-el

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
el_GR_aliases="el_CY"
for lang in $el_GR_aliases; do
        ln -s el_GR.aff $lang.aff
        ln -s el_GR.dic $lang.dic
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_el_GR.txt
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:0.8-7
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 05 2012 Caolán McNamara <caolanm@redhat.com> - 1:0.8-5
- clarify exact MPL version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Caolán McNamara <caolanm@redhat.com> - 1:0.8-1
- latest version

* Wed Jun 09 2010 Caolán McNamara <caolanm@redhat.com> - 1:0.7-5
- Resolves: rhbz#602263 clarify licence

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Caolán McNamara <caolanm@redhat.com> - 1:0.7-3
- extend coverage

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 20 2007 Caolán McNamara <caolanm@redhat.com> - 1:0.7-1
- latest upstream version
- clarify license version

* Thu Dec 07 2006 Caolán McNamara <caolanm@redhat.com> - 0.20041220-1
- initial version
