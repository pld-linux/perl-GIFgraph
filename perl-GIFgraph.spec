%include	/usr/lib/rpm/macros.perl
Summary:	GIFgraph - graph plotting module
Summary(pl):	GIFgraph - modu³ do rysowania wykresów
Name:		perl-GIFgraph
Version:	1.20
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/GIFgraph/GIFgraph-%{version}.tar.gz
# Source0-md5:	b4171f7d88c01acb0df5c5d515b24714
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	ImageMagick-perl
BuildRequires:	perl-devel >= 5.6.1
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install samples/*.{gif,txt,dat,pl} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/GIFgraph.pm
%{perl_vendorlib}/GIFgraph
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/*.[gtd]*
