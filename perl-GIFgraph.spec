%include	/usr/lib/rpm/macros.perl
Summary:	GIFgraph perl module
Summary(pl):	Modu³ perla GIFgraph
Name:		perl-GIFgraph
Version:	1.20
Release:	1
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/GIFgraph/GIFgraph-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-17
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-GD
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GIFgraph is a module to create and display GIF output for a graph. 

%description -l pl
GIFgraph jest modu³em do tworzenia i wy¶wietlania wykresów i grafów
w formacie GIF.

%prep
%setup -q -n GIFgraph-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}
make install DESTDIR=$RPM_BUILD_ROOT

install samples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/GIFgraph
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        CHANGES README BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README,BUGS}.gz

%{perl_sitelib}/GIFgraph.pm
%{perl_sitelib}/GIFgraph
%{perl_sitearch}/auto/GIFgraph

%{_mandir}/man3/*
/usr/src/examples/%{name}-%{version}
