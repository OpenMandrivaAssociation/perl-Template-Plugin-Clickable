%define upstream_name    Template-Plugin-Clickable
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Make URLs clickable in HTML 
License:    Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
Buildrequires:  perl(Template)
Buildrequires:  perl(URI::Find)
Buildrequires:  perl(UNIVERSAL::require)
buildArch:      noarch
buildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Template::Plugin::Clickable is a plugin for TT, which allows you to filter
HTMLs clickable.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
