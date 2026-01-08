#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:           arianna
Version:        25.12.1
Release:        %{?git:0.%{git}.}1
Summary:        Ebook reader and library management app
License:        GPL-3.0-only
URL:            https://apps.kde.org/arianna/
%if 0%{?git}
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/arianna/-/archive/%{gitbranch}/arianna-%{gitbranchd}.tar.bz2#/arianna-%{git}.tar.bz2
%else
Source0:        https://invent.kde.org/plasma-mobile/%{name}/-/archive/master/%{name}-master.tar.bz2
%endif
%else
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/arianna/-/archive/%{gitbranch}/arianna-%{gitbranchd}.tar.bz2#/arianna-%{git}.tar.bz2
%else
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/arianna-%{version}.tar.xz
%endif
%endif
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Baloo)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6ColorScheme)
BuildRequires:	cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6KirigamiAddons) >= 0.8
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6WebEngineQuick)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:	cmake(Qt6WebChannel)
BuildRequires:	cmake(Qt6HttpServer)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(KF6QuickCharts)
Requires:       kirigami-addons
Requires:       kf6-kirigami
Requires:       kf6-kquickcharts
Requires:       qt6-qtbase-sql-sqlite
Requires:       %mklibname Qt6QuickControls2
Requires:       %mklibname Qt6WebChannel

%rename plasma6-arianna

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
An ebook reader and library management app supporting ".epub" files. Arianna
discovers your books automatically, and sorts them by categories, genres and
authors.

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_datadir}/applications/org.kde.arianna.desktop
%{_datadir}/metainfo/org.kde.arianna.appdata.xml
%{_bindir}/arianna
%{_datadir}/qlogging-categories6/arianna.categories
%{_datadir}/icons/hicolor/scalable/apps/org.kde.arianna.svg
