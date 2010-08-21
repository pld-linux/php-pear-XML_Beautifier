%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Beautifier
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - class to format XML documents
Summary(pl.UTF-8):	%{_pearname} - klasa do formatowania dokumentów XML
Name:		php-pear-%{_pearname}
Version:	1.2.0
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	32e5fbe5a4fb499c3a472c0d1a3aad61
URL:		http://pear.php.net/package/XML_Beautifier/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-XML_Parser >= 1.0
Requires:	php-pear-XML_Util >= 0.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_Beautifier will add indentation and linebreaks to you XML files,
replace all entities, format your comments and makes your document
easier to read. You can influence the way your document is beautified
with several options.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
XML_Beautifier dodaje wcięcia i znaki końca linii do plików XML,
zastępuje wszelkie encje, przeformatowuje komentarze i sprawia, że
dokument jest łatwiejszy do czytania. Za pomocą wielu opcji można
wpłynąć na sposób, w jaki dokument będzie upiększony.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Renderer
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Renderer/*.php
