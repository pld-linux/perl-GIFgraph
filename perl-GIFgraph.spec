%include	/usr/lib/rpm/macros.perl
Summary:	GIFgraph perl module
Summary(pl):	Modu³ perla GIFgraph
Name:		perl-GIFgraph
Version:	1.20
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/GIFgraph/GIFgraph-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-17
BuildRequires:	ImageMagick-perl
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-GD
BuildRequires:	perl-GD-Graph
BuildRequires:	ImageMagick-perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GIFgraph is a module to create and display GIF output for a graph.

%description -l pl
GIFgraph jest modu³em do tworzenia i wy¶wietlania wykresów i grafów w
formacie GIF.

%prep
%setup -q -n GIFgraph-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/GIFgraph.pm
%{perl_sitelib}/GIFgraph
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
