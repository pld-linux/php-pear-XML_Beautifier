%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       Beautifier
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - class to format XML documents
Summary(pl):	%{_pearname} - klasa do formatowania dokumentów XML
Name:		php-pear-%{_pearname}
Version:	0.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a7a18b3870614df37bc4388982a789e9
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_Beautifier will add indentation and linebreaks to you XML files,
replace all entities, format your comments and makes your document
easier to read. You can influence the way your document is beautified
with several options. 

This class has in PEAR status: %{_status}.

%description -l pl
XML_Beautifier doda wciêcia i znaki koñca linii do Twoich plików XML,
zast±pi wszelkie encje, przeformatuje komentarze i sprawi, ¿e Twój
dokument bêdzie ³atwiejszy do czytania. Za pomoc± wielu opcji mo¿esz
wp³yn±æ na sposób, w jaki Twój dokument bêdzie upiêkszony.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
