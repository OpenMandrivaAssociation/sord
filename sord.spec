%define debug_package %nil

Name:           sord
Version:        0.12.0
Release:        2
Summary:        Lightweight C library for storing RDF data in memory

%define lib_major       0
%define lib_name        %mklibname %{name} %{lib_major}
%define lib_name_devel  %mklibname %{name} -d

Source0:         http://download.drobilla.net/%{name}-%{version}.tar.bz2
URL:            http://drobilla.net/software/%{name}/
License:        MIT-like
Group:          System/Libraries

BuildRequires:  waf, pkgconfig
BuildRequires:  glib2-devel
BuildRequires:  serd-devel

%description
Lightweight C library for storing RDF data in memory.

%files
%doc COPYING README
%doc %{_mandir}/man1/sordi.*
%doc %{_mandir}/man1/sord_*
%{_bindir}/sordi
%{_bindir}/sord_validate


#-----------------------------------
%package -n %{lib_name}

Summary:        Lightweight RDF syntax library
Group:          System/Libraries

%description -n %{lib_name}
Lightweight C library for storing RDF data in memory.


%files -n %{lib_name}
%{_libdir}/lib%{name}-%{lib_major}.so.*

#-----------------------------------
%package -n %{lib_name_devel}
Summary:        Headers for the sord RDF storage library
Group:          System/Libraries
Requires:       %{lib_name} = %{version}-%{release}
Requires:       pkgconfig
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
Development files needed to build applications against sord.

%files -n %{lib_name_devel}
%{_libdir}/lib%{name}-%{lib_major}.so
%dir %{_includedir}/%{name}-%{lib_major}/%{name}
%{_includedir}/%{name}-%{lib_major}/%{name}/*.h
%{_includedir}/%{name}-%{lib_major}/%{name}/*.hpp
%{_libdir}/pkgconfig/%{name}-%{lib_major}.pc

#-----------------------------------
%prep
%setup -q

%build
./waf configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir}
./waf

%install
./waf install --destdir=%{buildroot}

%changelog
* Wed Aug 29 2012 Frank Kober <emuse@mandriva.org> 0.10.0-2mdv2012.0
+ Revision: 815972
- new version 0.10.0

* Mon Apr 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.8.0-1
+ Revision: 792823
- unpackaged fil
- version update 0.8.0

* Sun Oct 23 2011 Frank Kober <emuse@mandriva.org> 0.5.0-1
+ Revision: 705725
- new version 0.5.0

* Sat Jun 25 2011 Frank Kober <emuse@mandriva.org> 0.4.2-1
+ Revision: 687128
- imported package sord

