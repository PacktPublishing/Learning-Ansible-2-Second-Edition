%global commit0 7c288b9d80a6ef525c0cca8a744b32e018eaa386
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           hello-world
Version:        1.0
Release:        1%{?dist}
Summary:        Hello World example implemented in C

License:        GPLv3+
URL:            https://github.com/Fale/hello-world
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
The description for our Hello World Example implemented in C

%prep
%autosetup -n %{name}-%{commit0}

%build
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%{_bindir}/hello

%changelog
* Tue Oct 11 2016 Fabio Alessandro Locati - 1.0-1
- Initial packaging
