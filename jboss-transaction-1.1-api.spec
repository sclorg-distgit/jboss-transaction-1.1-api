%global pkg_name jboss-transaction-1.1-api
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.0.1
Release:          8.9%{?dist}
Summary:          Transaction 1.1 API
License:          CDDL or GPLv2 with exceptions
Url:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-transaction-api_spec.git jboss-transaction-1.1-api
# cd jboss-transaction-1.1-api/ && git archive --format=tar --prefix=jboss-transaction-1.1-api/ jboss-transaction-api_1.1_spec-1.0.1.Final | xz > jboss-transaction-1.1-api-1.0.1.Final.tar.xz
Source0:          %{pkg_name}-%{namedversion}.tar.xz

BuildRequires:    %{?scl_prefix}jboss-specs-parent
BuildRequires:    %{?scl_prefix_java_common}javapackages-tools
BuildRequires:    %{?scl_prefix_java_common}maven-local
BuildRequires:    %{?scl_prefix}maven-compiler-plugin
BuildRequires:    %{?scl_prefix}maven-install-plugin
BuildRequires:    %{?scl_prefix}maven-jar-plugin
BuildRequires:    %{?scl_prefix}maven-javadoc-plugin
BuildRequires:    %{?scl_prefix}maven-enforcer-plugin
BuildRequires:    %{?scl_prefix}maven-dependency-plugin
BuildRequires:    %{?scl_prefix}maven-clean-plugin

BuildArch:        noarch

%description
The Java Transaction 1.1 API classes.

%package javadoc
Summary:          Javadocs for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n jboss-transaction-1.1-api

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
mvn-rpmbuild install javadoc:aggregate
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-transaction-api_1.1_spec-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{pkg_name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{pkg_name}.pom

# DEPMAP
%add_maven_depmap JPP-%{pkg_name}.pom %{pkg_name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%{?scl:EOF}

%files -f .mfiles
%doc README LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0.1-8.9
- Mass rebuild 2015-01-13

* Wed Jan 07 2015 Michal Srb <msrb@redhat.com> - 1.0.1-8.8
- Migrate to .mfiles

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.0.1-8.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-8.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-8.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-8.4
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-8.3
- Remove requires on java

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 1.0.1-8.2
- SCL-ize BR/R

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.1-8
- Mass rebuild 2013-12-27

* Fri Dec 13 2013 Ade Lee <alee@redhat.com> 1.0.1-7
- Fix spec file dist tag for rpmlint

* Wed Nov 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-6
- Remove unneeded BR: maven-plugin-cobertura

* Thu May 9 2013 Ade Lee <alee@redhat.com> 1.0.1-5
- Resolves #961465 - Removed unneeded maven-checkstyle-plugin BR

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Nov 15 2012 Ade Lee <alee@redhat.com> 1.0.1-2
- Removed maven-eclipse-plugin-dependency
- Added maven-clean-plugin

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Upstream release 1.0.1.Final
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.2.20120309git3970b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-0.1.20120309git3970b8
- Packaging after license cleanup upstream

* Mon Oct 24 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-2
- Fixed apidocs issue

* Thu Aug 11 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging
