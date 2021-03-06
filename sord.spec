%define debug_package %nil

Name:           sord
Version:	0.16.8
Release:	1
Summary:        Lightweight C library for storing RDF data in memory

%define lib_major       0
%define lib_name        %mklibname %{name} %{lib_major}
%define lib_name_devel  %mklibname %{name} -d

Source0:         http://download.drobilla.net/%{name}-%{version}.tar.bz2
URL:            http://drobilla.net/software/%{name}/
License:        MIT-like
Group:          System/Libraries

BuildRequires:  waf, pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  serd-devel

%description
Lightweight C library for storing RDF data in memory.

%files
%doc COPYING
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
python ./waf configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir} CC=%{__cc}
python ./waf

%install
python ./waf install --destdir=%{buildroot}
