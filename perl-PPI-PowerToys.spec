%define upstream_name    PPI-PowerToys
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A handy collection of small PPI-based utilities
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/PPI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(File::Find::Rule::Perl)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(IPC::Run3)
BuildRequires:	perl(PPI::Document)
BuildRequires:	perl(Probe::Perl)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Script)
BuildRequires: 	perl(version)

BuildArch:	noarch

%description
The PPI PowerToys are a small collection of utilities for working with Perl
files, modules and distributions.

To kick off the collection, he's added a very simple and raw version of one
of his own little tools.

ppi_version
      > ppi_version show
      > ppi_version change 0.01 0.02

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc LICENSE README META.yml Changes
%{_bindir}/ppi_*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.140.0-2mdv2011.0
+ Revision: 655156
- rebuild for updated spec-helper

* Thu Feb 11 2010 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 504101
- import perl-PPI-PowerToys


* Thu Feb 11 2010 cpan2dist 0.14-1mdv
- initial mdv release, generated with cpan2dist
