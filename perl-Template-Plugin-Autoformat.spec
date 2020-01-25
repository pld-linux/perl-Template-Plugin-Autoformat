#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Template
%define	pnam	Plugin-Autoformat
Summary:	Template::Plugin::Autoformat - Interface to Text::Autoformat module
Summary(pl.UTF-8):	Template::Plugin::Autoformat - Interfejs do modułu Text::Autoformat
Name:		perl-Template-Plugin-Autoformat
Version:	2.71
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Template/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cb3d9224a0b4022cba7fd3f42d308bfa
URL:		http://search.cpan.org/dist/Template-Plugin-Autoformat/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Template-Toolkit >= 2.2
BuildRequires:	perl-Text-Autoformat >= 1.13
%endif
BuildArch:	noarch
Provides:	perl-Template-Toolkit-Plugin-Autoformat
Obsoletes:	perl-Template-Toolkit-Plugin-Autoformat
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Template Toolkit plugin module is an interface to Damian
Conway's Text::Autoformat Perl module which provides advanced text wrapping
and formatting.

Configuration options may be passed to the plugin constructor via the 
USE directive.

    [% USE autoformat(right => 30) %]

The autoformat subroutine can then be called, passing in text items which 
will be wrapped and formatted according to the current configuration.

    [% autoformat('The cat sat on the mat') %]

# %description -l pl.UTF-8
# TODO

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
%doc README
%{perl_vendorlib}/Template/Plugin/*.pm
%{_mandir}/man3/*
