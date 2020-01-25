%define		_status		stable
%define		_pearname	XML_Beautifier
Summary:	%{_pearname} - class to format XML documents
Summary(pl.UTF-8):	%{_pearname} - klasa do formatowania dokumentów XML
Name:		php-pear-%{_pearname}
Version:	1.2.2
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a5f57c749a09a1b598f0284c95f86e68
URL:		http://pear.php.net/package/XML_Beautifier/
BuildRequires:	php-pear-PEAR >= 1:1.3.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
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
%{php_pear_dir}/XML/Beautifier.php
%{php_pear_dir}/XML/Beautifier
