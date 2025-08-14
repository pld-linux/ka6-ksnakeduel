#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.08.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		ksnakeduel
Summary:	ksnakeduel
Name:		ka6-%{kaname}
Version:	25.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	aaaa1abfd2297dd1384af78070fe2aa0
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka6-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcompletion-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kguiaddons-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
BuildRequires:	zlib-devel
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSnakeDuel is a simple Tron-Clone You can play KSnakeDuel against the
computer or a friend. The aim of the game is to live longer than your
opponent. To do that, avoid running into a wall, your own tail and
that of your opponent.

%description -l pl.UTF-8
KSnakeDuel jest prostym klonem Trona. Możesz grać w KSnakeDuela
przeciwko komputerowi lub przyjacielowi. Celem gry jest przeżyć
dłużej niż przeciwnik. Aby tego dokonać, unikaj ścian, własnego ogona
jak i ogona oponenta.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksnakeduel
%{_desktopdir}/org.kde.ksnakeduel.desktop
%{_datadir}/config.kcfg/ksnakeduel.kcfg
%{_iconsdir}/hicolor/*x*/apps/ksnakeduel.png
%{_datadir}/ksnakeduel
%{_datadir}/metainfo/org.kde.ksnakeduel.appdata.xml
%{_datadir}/qlogging-categories6/ksnakeduel.categories
%{_datadir}/knsrcfiles/ksnakeduel.knsrc
