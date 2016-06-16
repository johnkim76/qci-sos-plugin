Summary: QCI SOS Plugin 
Name:    qci-sos-plugin
Version: 1.0.0
Release: 0%{dist}
Group:   Applications/Internet 
License: Distributable
URL: https://github.com/johnkim76/qci-sos-plugin
Source0: qci.py

Requires: python >= 2.3
Requires: foreman >= 1.7.0

BuildArch: noarch

%description
QCI SOS Plugin

%prep

%build

%install
install -d -m 755 %{buildroot}%{python_sitelib}/sos/plugins/
cp -a %{SOURCE0} %{buildroot}%{python_sitelib}/sos/plugins/

%clean
%{__rm} -rf %{buildroot}

%files
%{python_sitelib}/sos/plugins/%{SOURCE0}

%changelog