%define upstream_name    Config-Model-Backend-Augeas
%define upstream_version 0.109

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Read and write config data through Augeas
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

#BuildRequires: perl(Config::Model)
#BuildRequires: perl(Config::Augeas)
BuildRequires: perl(Module::Build)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This class provides a way to load or store configuration data through Config::Augeas. This way, the structure and commments of the original configuration file will preserved.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_mandir}/man3/*
%{perl_vendorlib}/Config/Model/Backend/Augeas.pm
