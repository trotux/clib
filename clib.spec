Name:           clib
Version:        0.3
Release:        1%{?dist}
Summary:        Development files for the clib library

Group:          Development/Libraries
License:        2-clause BSD
URL:            http://github.com/tonnerre/clib/
Source0:        clib-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
clib is a development library which provides the end user with hashes,
arrays and other features that are very useful for programming in the
C programming language.

%package        devel
Summary:        Development files for the clib library
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Tue Feb 19 2012 - tonnerre@ancient-solutions.com
- Release of version 0.3.
- Addition of socket functions (c_str2addrinfo(), etc.).
- Big bug fixes for the array implementation.

* Wed Jul 29 2009 - tonnerre.lombard@sygroup.ch
- Bump revision after release of version 0.2.
- Added destructors to the array API to match the hash API.

* Tue Jul 28 2009 - tonnerre.lombard@sygroup.ch
- Added function to convert host:port strings to socket addresses for
  connect, bind etc.

* Tue Jul 21 2009 - tonnerre.lombard@sygroup.ch
- Initial release for RedHat
- Corrected return types for default hash functions
- Fixed array implementation
