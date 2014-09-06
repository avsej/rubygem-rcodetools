%global gem_name rcodetools

Summary: Collection of Ruby code manipulation tools
Name: rubygem-%{gem_name}
Version: 0.8.5.0
Release: 1%{?dist}
Group: Development/Languages
License: Ruby
URL: https://rubygems.org/gems/rcodetools
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: ruby-devel
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
rcodetools is a collection of Ruby code manipulation tools. It
includes xmpfilter and editor-independent Ruby development helper
tools, as well as emacs and vim interfaces.

Currently, rcodetools comprises:

* xmpfilter: Automagic Test::Unit assertions/RSpec expectations and
  code annotations
* rct-complete: Accurate method/class/constant etc. completions
* rct-doc: Document browsing and code navigator
* rct-meth-args: Precise method info (meta-prog. aware) and TAGS
  generation
* rct-fork: Pre-load heavy library(Rails etc) and speed up
  rct-complete/rct-doc (server)
* rct-fork-client: Run Ruby programs from state the rct-fork server
  has
* ruby-toggle-file: Toggle implementation file and test file
* rbtest: Embedded Test::Unit for small scripts

%package doc
Summary: Documentation for %{name}
Group: Documentation

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_dir}/bin
for tool in \
    rbtest \
    rct-complete \
    rct-doc \
    rct-fork \
    rct-fork-client \
    rct-meth-args \
    ruby-toggle-file \
    xmpfilter
do
    chmod a+x %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/bin/${tool}
    cp -a %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/bin/${tool} %{buildroot}%{gem_dir}/bin
done
%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gem_dir}/bin/xmpfilter
%{gem_dir}/bin/rbtest
%{gem_dir}/bin/rct-complete
%{gem_dir}/bin/rct-doc
%{gem_dir}/bin/rct-fork
%{gem_dir}/bin/rct-fork-client
%{gem_dir}/bin/rct-meth-args
%{gem_dir}/bin/ruby-toggle-file
%{gem_dir}/bin/xmpfilter
%{gem_dir}/gems/%{gem_name}-%{version}/
%{gem_cache}
%{gem_spec}

%files doc

%defattr(-, root, root, -)
%{gem_docdir}

%changelog
* Sat Sep  6 2014 Sergey Avseyev <sergey.avseyev@gmail.com> - 0.8.5.0-1
- Initial package
