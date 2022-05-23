#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Template
%define	pnam	Plugin-Autoformat
Summary:	Template::Plugin::Autoformat - Interface to Text::Autoformat module
Summary(pl.UTF-8):	Template::Plugin::Autoformat - Interfejs do modułu Text::Autoformat
Name:		perl-Template-Plugin-Autoformat
Version:	2.77
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Template/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ecfceb3b8f0f68ff105b3c363c5cee14
URL:		https://metacpan.org/dist/Template-Plugin-Autoformat
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Template-Toolkit >= 2.20
BuildRequires:	perl-Text-Autoformat >= 1.13
%endif
Provides:	perl-Template-Toolkit-Plugin-Autoformat = %{version}
Obsoletes:	perl-Template-Toolkit-Plugin-Autoformat < 2.22
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Template Toolkit plugin module is an interface to Damian
Conway's Text::Autoformat Perl module which provides advanced text
wrapping and formatting.

%description -l pl.UTF-8
Ten moduł wtyczki do Template Toolkitu jest interfgejsem do modułu
Perla Damiana Conwaya, zapewniającego zaawansowane zawijanie i
formatowanie tekstu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/Template/Plugin/Autoformat.pm
%{_mandir}/man3/Template::Plugin::Autoformat.3pm*
