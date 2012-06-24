#
# Conditional build:
%bcond_with	tests		# perform "make test" (last will fail, bug in test script)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Filter-Dispatcher
Summary:	XML::Filter::Dispatcher - path based event dispatching with DOM support
Summary(pl):	XML::Filter::Dispatcher - koordynacja zdarze� w oparciu o �cie�k� ze wsparciem dla DOM
Name:		perl-XML-Filter-Dispatcher
Version:	0.52
Release:	1
# GPL||Artistic and same as perl for XML::Filter::Dispatcher::Parser
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1ffc34ea2f56a1afaba23702de1ab15e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-GraphViz
BuildRequires:	perl-Parse-Yapp
BuildRequires:	perl-XML-NamespaceSupport
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-XML-SAX-Machines
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WARNING: Beta code alert.

A SAX2 filter that dispatches SAX events based on "EventPath" patterns
as the SAX events arrive. The SAX events are not buffered or
converted to an in-memory document representation like a DOM tree.
This provides for low lag operation because the actions associated
with each pattern are executed as soon as possible, usually in an
element's start_element() event method.

This differs from traditional XML pattern matching tools like XPath
and XSLT (which is XPath-based) which require the entire document to
be built in memory (as a "DOM tree") before queries can be executed.
In SAX terms, this means that they have to build a DOM tree from SAX
events and delay pattern matching until the end_document() event
method is called.

%description -l pl
UWAGA: kod beta.

Filtr SAX2 koordynuje zdarzenia SAX oparte na wzorcach "EventPath" w
miar� nap�ywu zdarze� SAX. Zdarzenia SAX nie s� buforowane ani
konwertowane do reprezentacji dokument�w w pami�ci w rodzaju drzewa
DOM. Daje to dzia�anie z ma�ymi op�nieniami, poniewa� akcje powi�zane
z ka�dym wzorcem s� wykonywane tak szybko jak to mo�liwe, zazwyczaj
w metodzie zdarzenia elementu start_element().

R�ni si� to od tradycyjnych narz�dzi dopasowuj�cych wzorce XML jak
XPath czy XSLT (kt�re jest oparte na XPath), wymagaj�cych zbudowania
w pami�ci ca�ego dokumentu (jako "drzewa DOM") przed wykonywaniem
zapyta�. W terminologii SAX oznacza to, �e musz� zbudowa� drzewo DOM
ze zdarze� SAX i op�ni� dopasowywanie wzorc�w do wykonania metody
zdarzenia end_document().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/XML/*/*
%{_mandir}/man3/*
%{_mandir}/man1/*
