%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Beautifier
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - class to format XML documents
Summary(pl):	%{_pearname} - klasa do formatowania dokumentów XML
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d121758edb840d9107debb26bb5837d7
URL:		http://pear.php.net/package/XML_Beautifier/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-common >= 3:4.2.0
Requires:	php-pear-XML_Util >= 0.5
Requires:	php-pear-XML_Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_Beautifier will add indentation and linebreaks to you XML files,
replace all entities, format your comments and makes your document
easier to read. You can influence the way your document is beautified
with several options. 

In PEAR status of this package is: %{_status}.

%description -l pl
XML_Beautifier dodaje wciêcia i znaki koñca linii do plików XML,
zastêpuje wszelkie encje, przeformatowuje komentarze i sprawia, ¿e
dokument jest ³atwiejszy do czytania. Za pomoc± wielu opcji mo¿na
wp³yn±æ na sposób, w jaki dokument bêdzie upiêkszony.

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
