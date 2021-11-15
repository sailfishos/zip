Name:       zip
Summary:    A file compression and packaging utility compatible with PKZIP
Version:    3.0+git1
Release:    1
License:    BSD
URL:        http://www.info-zip.org/Zip.html
Source0:    zip30.tar.gz
Patch0:     zip-3.0-exec-shield.patch
Patch1:     zip-3.0-currdir.patch
Patch2:     zip-3.0-time.patch


%description
The zip program is a compression and file packaging utility.  Zip is
analogous to a combination of the UNIX tar and compress commands and
is compatible with PKZIP (a compression and file packaging utility for
MS-DOS systems).

Install the zip package if you need to compress files using the zip
program.


%prep
%autosetup -p1 -n %{name}30


%build
make -f unix/Makefile prefix=%{_prefix} "CFLAGS_NOOPT=-I. -DUNIX $RPM_OPT_FLAGS" generic_gcc  %{?_smp_mflags}

%install
rm -rf %{buildroot}

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BULD_ROOT%{_mandir}/man1

make -f unix/Makefile prefix=$RPM_BUILD_ROOT%{_prefix} MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 install


%files
%defattr(-,root,root,-)
%license LICENSE
%doc README CHANGES TODO WHATSNEW WHERE README.CR
%doc proginfo/algorith.txt
%{_bindir}/zipnote
%{_bindir}/zipsplit
%{_bindir}/zip
%{_bindir}/zipcloak
%doc %{_mandir}/man1/zip.1*
%doc %{_mandir}/man1/zipcloak.1*
%doc %{_mandir}/man1/zipnote.1*
%doc %{_mandir}/man1/zipsplit.1*
