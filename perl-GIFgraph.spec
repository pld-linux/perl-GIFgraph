%include	/usr/lib/rpm/macros.perl
Summary:	GIFgraph perl module
Summary(pl):	Modu³ perla GIFgraph
Name:		perl-GIFgraph
Version:	1.20
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/GIFgraph/GIFgraph-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
%{__perl} Makefile.PL
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
%{perl_sitelib}/GIFgraph.pm
%{perl_sitelib}/GIFgraph
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/*.[gtd]*
