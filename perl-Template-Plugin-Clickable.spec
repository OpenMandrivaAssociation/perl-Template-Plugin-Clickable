%define module  Template-Plugin-Clickable
%define name    perl-%{module}
%define version 0.06
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Make URLs clickable in HTML 
License:        Artistic
group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Template/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
Buildrequires:  perl(Template)
Buildrequires:  perl(URI::Find)
Buildrequires:  perl(UNIVERSAL::require)
buildArch:      noarch
buildRoot:      %{_tmppath}/%{name}-%{version}

%description
Template::Plugin::Clickable is a plugin for TT, which allows you to filter
HTMLs clickable.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Template
%{_mandir}/*/*


