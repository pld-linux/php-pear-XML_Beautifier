%include	/usr/lib/rpm/macros.php
%include	/usr/lib/rpm/macros.pear
%define		_class		XML
%define		_subclass	Beautifier
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - class to format XML documents
Summary(pl):	%{_pearname} - klasa do formatowania dokument�w XML
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	2.3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d121758edb840d9107debb26bb5837d7
URL:		http://pear.php.net/package/XML_Beautifier/
BuildRequires:	php-pear-build
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_Beautifier will add indentation and linebreaks to you XML files,
replace all entities, format your comments and makes your document
easier to read. You can influence the way your document is beautified
with several options. 

In PEAR status of this package is: %{_status}.

%description -l pl
XML_Beautifier dodaje wci�cia i znaki ko�ca linii do plik�w XML,
zast�puje wszelkie encje, przeformatowuje komentarze i sprawia, �e
dokument jest �atwiejszy do czytania. Za pomoc� wielu opcji mo�na
wp�yn�� na spos�b, w jaki dokument b�dzie upi�kszony.

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
