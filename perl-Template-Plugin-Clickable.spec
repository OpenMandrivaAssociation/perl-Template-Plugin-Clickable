%define upstream_name    Template-Plugin-Clickable
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Make URLs clickable in HTML 
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Template)
BuildRequires:	perl(URI::Find)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description
Template::Plugin::Clickable is a plugin for TT, which allows you to filter
HTMLs clickable.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Template
%{_mandir}/*/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 405532
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.06-4mdv2009.0
+ Revision: 258462
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.06-3mdv2009.0
+ Revision: 246502
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.06-1mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2007.1
+ Revision: 138894
- fix build dependencies
- Imported perl-Template-Plugin-Clickable-0.06-1mdv2007.1 into SVN repository.

* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2007.1
- first mdv release

