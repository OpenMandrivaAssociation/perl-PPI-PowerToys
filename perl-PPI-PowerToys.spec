%define upstream_name    PPI-PowerToys
%define upstream_version 0.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A handy collection of small PPI-based utilities
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/PPI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(File::Find::Rule::Perl)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(PPI::Document)
BuildRequires: perl(Probe::Perl)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Script)
BuildRequires: perl(version)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README META.yml Changes
%{_bindir}/ppi_*
%{_mandir}/man3/*
%perl_vendorlib/*


