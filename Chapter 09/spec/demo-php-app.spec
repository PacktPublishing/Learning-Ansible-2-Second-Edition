%define debug_package %{nil}
%global commit0 b49f595e023e07a8345f47a3ad62a6f50f03121e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:       demo-php-app
Version:    0
Release:    1%{?dist}
Summary:    Demo PHP application

License:    PD
URL:        https://github.com/Fale/demo-php-app
Source0:    %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

%description
This is a demo PHP application in RPM format

%prep
%autosetup -n %{name}-%{commit0}

%build

%install
mkdir -p %{buildroot}/var/www/application
ls -alh
cp index.php %{buildroot}/var/www/application

%files
%dir /var/www/application
/var/www/application/index.php

%changelog
* Tue Oct 04 2016 Fabio Alessandro Locati - 0.1
- Initial packaging
