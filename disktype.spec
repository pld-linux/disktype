Summary:	Disktype - detect the content format of a disk or disk image
Summary(pl):	Disktype - narz�dzie do wykrywania formatu dysku lub jego obrazu
Name:		disktype
Version:	8
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	47cf84b2474dd354cdbe56bf02bb50ab
URL:		http://disktype.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of disktype is to detect the content format of a disk or
disk image. It knows about common file systems, partition tables, and
boot codes.

%description -l pl
disktype s�u�y do wykrywania formatu dysku lub jego obrazu. Zna
podstawowe systemy plik�w, tablice partycji oraz kody startowe.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D disktype $RPM_BUILD_ROOT%{_bindir}/disktype

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README TODO
%attr(755,root,root) %{_bindir}/*
