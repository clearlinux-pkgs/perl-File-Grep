#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-File-Grep
Version  : 0.02
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/M/MN/MNEYLON/File-Grep-0.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MN/MNEYLON/File-Grep-0.02.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-grep-perl/libfile-grep-perl_0.02-1.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-File-Grep-license = %{version}-%{release}
Requires: perl-File-Grep-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
File/Grep version $Revision: 0.02 $
================================
File::Grep provides similar functionality as perl's builtin grep, map,
and foreach commands, but iterating over a passed filelist instead of
arrays.  While trivial, this module can provide a quick dropin when
such functionality is needed.

%package dev
Summary: dev components for the perl-File-Grep package.
Group: Development
Provides: perl-File-Grep-devel = %{version}-%{release}
Requires: perl-File-Grep = %{version}-%{release}

%description dev
dev components for the perl-File-Grep package.


%package license
Summary: license components for the perl-File-Grep package.
Group: Default

%description license
license components for the perl-File-Grep package.


%package perl
Summary: perl components for the perl-File-Grep package.
Group: Default
Requires: perl-File-Grep = %{version}-%{release}

%description perl
perl components for the perl-File-Grep package.


%prep
%setup -q -n File-Grep-0.02
cd %{_builddir}
tar xf %{_sourcedir}/libfile-grep-perl_0.02-1.debian.tar.xz
cd %{_builddir}/File-Grep-0.02
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-Grep-0.02/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Grep
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-Grep/c434903250cad6fd117db3f486c290796b200da6 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Grep.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Grep/c434903250cad6fd117db3f486c290796b200da6

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
