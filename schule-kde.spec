Name:         schule-kde
Summary:      KDE installation files and menu for a school
BuildArch:    noarch
Version:      5.18
Release:      2
License:      GPL
Group:        application
Source:       %{name}-%{version}.tar.gz
Source1:      %{name}-himmelsthuer.menu
Source2:      %{name}-sas.menu
Source61:     %{name}-himmelsthuer-netbook.menu
Source62:     %{name}-sas-netbook.menu
Source7:      schulserver-autostart.desktop
Source8:      %{name}-UhrzugriffErlauben
Source9:      %{name}-akonadiserverrc
Source13:     schule.sh
Source14:     schule.csh
Source20:     klassenarbeit.service
Source21:     klassenarbeitAnAus
Source22:     01_gymhim
Source23:     resumeAus.service
Source24:     resumeAus
Source25:     01_sas
Source26:     %{name}-systemd-klassenarbeit.conf
Packager:     fschuett
Distribution: openSUSE Linux
Prefix:       /usr
Url:          http://www.gymnasium-himmelsthuer.de
BuildRequires:     desktop-file-utils shared-mime-info kdebase4-runtime plasma5-workspace-branding-openSUSE
# menu entry build requirements
BuildRequires: ark
BuildRequires: audacity
BuildRequires: avidemux-qt
BuildRequires: blender
BuildRequires: calibre
BuildRequires: CinqueMinuti
BuildRequires: geogebra5
BuildRequires: ghmessen
BuildRequires: gimp
BuildRequires: gwenview5
BuildRequires: imagej
BuildRequires: inkscape
BuildRequires: k3b
BuildRequires: kalgebra
BuildRequires: kalzium
BuildRequires: kate
BuildRequires: kbruch
BuildRequires: kcalc
BuildRequires: kdenlive
BuildRequires: k4dirstat
BuildRequires: kgeography
BuildRequires: kmag
BuildRequires: konqueror
BuildRequires: konsole
BuildRequires: ktechlab
BuildRequires: ktouch
BuildRequires: kwrite
BuildRequires: lejos
BuildRequires: libreoffice-base
BuildRequires: libreoffice-calc
BuildRequires: libreoffice-draw
BuildRequires: libreoffice-impress
BuildRequires: libreoffice-math
BuildRequires: libreoffice-writer
BuildRequires: marble
BuildRequires: MozillaFirefox
BuildRequires: musescore
BuildRequires: musikus
BuildRequires: netbeans
BuildRequires: okteta
BuildRequires: okular
BuildRequires: osp_datatool
BuildRequires: osp_tracker
BuildRequires: parley
BuildRequires: qsynth
BuildRequires: rosegarden
BuildRequires: scribus
BuildRequires: smart-notebook
BuildRequires: solfege
BuildRequires: spectacle
BuildRequires: stellarium
BuildRequires: tuxtype
BuildRequires: umbrello
BuildRequires: vlc
BuildRequires: vym
BuildRequires: wine

Requires:     polkit-default-privs kdebase4-runtime plasma5-workspace-branding-openSUSE desktop-file-utils shared-mime-info systemd
# menue entry requirements
Requires: ark
Requires: audacity
Requires: avidemux-qt
Requires: blender
Requires: calibre
Requires: CinqueMinuti
Requires: geogebra5
Requires: ghmessen
Requires: gimp
Requires: gwenview5
Requires: imagej
Requires: imagej-plugins-astronomy
Requires: inkscape
Requires: k3b
Requires: kalgebra
Requires: kalzium
Requires: kate
Requires: kbruch
Requires: kcalc
Requires: kdenlive
Requires: k4dirstat
Requires: kgeography
Requires: kmag
Requires: konqueror
Requires: konsole
Requires: ktechlab
Requires: ktouch
Requires: kwrite
Requires: lejos
Requires: libreoffice-base
Requires: libreoffice-calc
Requires: libreoffice-draw
Requires: libreoffice-impress
Requires: libreoffice-math
Requires: libreoffice-writer
Requires: marble
Requires: MozillaFirefox
Requires: musescore
Requires: musikus
Requires: netbeans
Requires: OpenBoard
Requires: okteta
Requires: okular
Requires: osp_datatool
Requires: osp_tracker
Requires: parley
Requires: qsynth fluidsynth GeneralUser
Requires: rosegarden wavpack qjackctl flac
Requires: scribus
Requires: solfege
Requires: spectacle
Requires: stellarium
Requires: tuxtype
Requires: umbrello
Requires: vlc
Requires: vym
Requires: wine

%description
kde installation files for a school. It provides a enhanced desktop.

%package gymhim
Summary:      kde Installation für das Gymnasium Himmelsthür
BuildArch:    noarch
Requires:     schule-kde
Conflicts:    schule-kde-gymhim-netbook schule-kde-sas schule-kde-sas-netbook

%description gymhim
KDE Installationsdateien für das Gymnasium Himmelsthür. Es enthält ein Menü
und einige Desktop-Symbole.

%package gymhim-netbook
Summary:      kde Installation für das Gymnasium Himmelsthür auf einem Netbook
BuildArch:    noarch
Requires:     schule-kde
Conflicts:    schule-kde-gymhim schule-kde-sas schule-kde-sas-netbook

%description gymhim-netbook
KDE Installationsdateien für das Gymnasium Himmelsthür auf einem Netbook. Es
enthält ein Sal-Menü und einige Desktop-Symbole.

%package sas
Summary:      kde Installation für die Sankt-Ansgar-Schule
BuildArch:    noarch
Requires:     schule-kde
BuildRequires: schule-wine-derive
Conflicts:    schule-kde-gymhim schule-kde-gymhim-netbook schule-kde-sas-netbook

%description sas
KDE Installationsdateien für die Sankt-Ansgar-Schule. Es enthält ein Menü
und einige Desktop-Symbole.

%package sas-netbook
Summary:      kde Installation für die Sankt-Ansgar-Schule auf einem Netbook
BuildArch:    noarch
Requires:     schule-kde
Conflicts:    schule-kde-gymhim schule-kde-gymhim-netbook schule-kde-sas

%description sas-netbook
KDE Installationsdateien für die Sankt-Ansgar-Schule auf einem Netbook. Es
enthält ein Sal-Menü und einige Desktop-Symbole.

%prep
%setup -q -n schule-kde

%build
# 
# create necessary desktop files
mkdir -p share/applications/himmelsthuer
mkdir -p share/applications/sas
# build desktop entries SCHULE VERZEICHNIS KATEGORIE
build_desktop_entries(){
local SCHULE="$1"
local VERZEICHNIS="$2"
local KATEGORIE="$3"
if test -z "${SCHULE}" -o -z "${VERZEICHNIS}" -o -z "${KATEGORIE}"; then
    echo "build_desktop_entries fehlgeschlagen! SCHULE(${SCHULE}) VERZEICHNIS(${VERZEICHNIS}) KATEGORIE(${KATEGORIE})"
    return
fi
while IFS=":" read name categoriesline; do
    file=`find /usr/share/applications /usr/share/mimelnk \
      -name 'himmelsthuer' -prune -o -name 'sas' -prune -o -type f -name $name -print |sed 1q`;
    if [ -z "$file" ]; then
	echo ">>>>%{name} Build error: ${name}|${categoriesline} nicht gefunden. Abhängigkeiten prüfen!<<<<" >>errors.log
	exit 1;
    fi
    neu=`echo $categoriesline|cut -d\= -f2`
    if grep -q "^Categories=" ${file}; then
	alt=`grep "^Categories=" ${file}`
	for c in `echo $neu | tr "[;]" "[ ]"`; do
	    if ! echo "${alt}"| grep -q "${c}"; then
		alt="${alt}${c};"
	    fi
	done;
	categoriesline=${alt}
    else
	alt=
    fi
    f=`basename ${file}`
    cp ${file} share/applications/${SCHULE}
    if [ -z "$alt" ]; then
    	echo "${categoriesline}${KATEGORIE};" >>share/applications/${SCHULE}/${f}
    else
    	sed -e "s|^Categories=.*|${categoriesline}${KATEGORIE};|" -i share/applications/${SCHULE}/${f}
    fi
done<${VERZEICHNIS}
}
# build entries
build_desktop_entries himmelsthuer schule-programme X-Himmelsthür
build_desktop_entries sas schule-programme X-SanktAnsgar
build_desktop_entries himmelsthuer himmelsthuer-programme X-Himmelsthür
build_desktop_entries sas sas-programme X-SanktAnsgar
# correct errors in desktop files
patch -p1 <%{name}-desktop-file.patch

%install
mkdir -p %{buildroot}/etc/polkit-default-privs.d

mkdir -p %{buildroot}%{prefix}/bin
cp -aR  bin/* %{buildroot}%{prefix}/bin

mkdir -p %{buildroot}/etc/xdg/plasma-workspace/env
mkdir -p %{buildroot}/etc/xdg/defaults
cp -aR config/* %{buildroot}/etc/xdg/defaults

mkdir -p %{buildroot}%{_datadir}
pushd share
for d in `echo "desktop-directories icons knotifications5 mime pixmaps plasma wallpapers"`; do
    mkdir -p %{buildroot}%{_datadir}/${d}/
    cp -aR  ${d}/* %{buildroot}%{_datadir}/${d}/
done;
popd

mkdir -p %{buildroot}%{_datadir}/%{name}/plasma-updates
cp -aR plasma-updates/* %{buildroot}%{_datadir}/%{name}/plasma-updates

mkdir -p %{buildroot}%{_datadir}/applications/himmelsthuer
pushd share/applications/himmelsthuer
for f in `ls`; do
    desktop-file-install --dir=%{buildroot}%{_datadir}/applications/himmelsthuer/ ${f}
done;
popd

mkdir -p %{buildroot}%{_datadir}/applications/sas
pushd share/applications/sas
for f in `ls`; do
    desktop-file-install --dir=%{buildroot}%{_datadir}/applications/sas/ ${f}
done;
popd
install -D -m 644 -o root -g root logind.conf.d/99-ignore-keys.conf %{buildroot}/etc/systemd/logind.conf.d/99-ignore-keys.conf

#Sources
for school in himmelsthuer sas; do
  install -D -m 644 -o root -g root %{name}-${school}.menu %{buildroot}%{_datadir}/schule-kde/%{name}-${school}.menu
  install -D -m 644 -o root -g root %{name}-${school}-netbook.menu %{buildroot}%{_datadir}/schule-kde/%{name}-${school}-netbook.menu
done

install -D -m 644 -o root -g root schulserver-autostart.desktop %{buildroot}/etc/xdg/autostart/schulserver-autostart.desktop
install -D -m 644 -o root -g root %{name}-UhrzugriffErlauben %{buildroot}/etc/polkit-default-privs.d/UhrzugriffErlauben
install -D -m 644 -o root -g root %{name}-akonadiserverrc %{buildroot}/etc/xdg/akonadi/akonadiserverrc
install -D -m 644 -o root -g root schule.sh %{buildroot}%{_sysconfdir}/profile.d/schule.sh
install -D -m 644 -o root -g root schule.csh %{buildroot}%{_sysconfdir}/profile.d/schule.csh
install -D -m 644 -o root -g root klassenarbeit.service %{buildroot}/etc/systemd/system/klassenarbeit.service
install -D -m 700 -o root -g root klassenarbeitAnAus %{buildroot}/sbin/klassenarbeitAnAus
install -D -m 755 -o root -g root 01_gymhim %{buildroot}/etc/grub.d/01_gymhim
install -D -m 755 -o root -g root 01_sas %{buildroot}/etc/grub.d/01_sas
install -D -m 644 -o root -g root resumeAus.service %{buildroot}/etc/systemd/system/resumeAus.service
install -D -m 700 -o root -g root resumeAus %{buildroot}/sbin/resumeAus
install -D -m 755 -o root -g root %{name}-systemd-klassenarbeit.conf %{buildroot}/etc/systemd/system/display-manager.service.d/klassenarbeit.conf

%post -f schule-kde.post

%post gymhim -f gymhim.post

%post gymhim-netbook -f gymhim-netbook.post

%post sas -f sas.post

%post sas-netbook -f sas-netbook.post

%preun gymhim -f gymhim.preun

%preun gymhim-netbook -f gymhim-netbook.preun

%preun sas -f sas.preun

%preun sas-netbook -f sas-netbook.preun

%postun
/usr/bin/update-mime-database /usr/share/mime
/usr/bin/update-desktop-database

%postun gymhim-netbook
[ -x /sbin/set_polkit_default_privs ] && /sbin/set_polkit_default_privs
systemctl daemon-reload

%postun sas-netbook
[ -x /sbin/set_polkit_default_privs ] && /sbin/set_polkit_default_privs
systemctl daemon-reload

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,0755)
%config /etc/xdg/akonadi/akonadiserverrc
/usr/share/knotifications5/schulserver.notifyrc
/usr/share/mime/packages/wine.xml
/usr/share/icons/himmelsthuer.png
/usr/share/icons/sas.png
/usr/share/icons/wine.png
/usr/share/plasma/desktoptheme/klassenarbeit
/usr/share/pixmaps
/usr/share/wallpapers/logo_gymhim_wallpaper.png
/usr/share/wallpapers/logo_gymhim_wallpaper.xcf
/usr/share/wallpapers/logo_gymhim_wallpaper_netbook.xcf
/usr/share/wallpapers/logo_sas_wallpaper.png
/usr/share/wallpapers/logo_sas_wallpaper.xcf
/usr/share/wallpapers/logo_klassenarbeit.png
/usr/share/wallpapers/logo_klassenarbeit.xcf
/usr/share/wallpapers/logo_gymhim_wallpaper_netbook.png
/usr/share/wallpapers/logo_sas_wallpaper_netbook.png
/usr/share/applications/himmelsthuer
/usr/share/applications/sas
%dir /usr/share/%{name}
%dir /usr/share/%{name}/plasma-updates
/usr/share/%{name}/plasma-updates/all
%defattr(755,root,root,0755) 
/usr/bin/winestartfile
/usr/bin/schulserver-notification-gymhim
/usr/bin/schulserver-notification-sas
/usr/bin/knotify.py
/usr/bin/restart-plasma
/usr/bin/reset.sh
/usr/bin/reset-netbook.sh
/usr/bin/kde_reset.sh
/usr/bin/kde_netbook_reset.sh
/usr/bin/firefox_reset.sh
/usr/bin/netbeans_reset.sh
/usr/bin/office_reset.sh
/usr/bin/smartnotebook_reset.sh
/usr/bin/smartnotebook_netbook_reset.sh
/usr/bin/wine_reset.sh

%files gymhim
%defattr(644,root,root,0755)
/etc/xdg/autostart/schulserver-autostart.desktop
/etc/profile.d/schule.sh
/etc/profile.d/schule.csh
/usr/share/desktop-directories/himmelsthuer.directory
%attr(755,root,root) /etc/xdg/defaults/startkde.gymhim.sh
/etc/xdg/defaults/gymhim/OSS.desktop
/etc/xdg/defaults/gymhim/Dokuwiki.desktop
/etc/xdg/defaults/gymhim/Moodle.desktop
/etc/xdg/defaults/gymhim/firefox.desktop
/etc/xdg/defaults/gymhim/vlc.desktop
/etc/xdg/defaults/gymhim/Reset.desktop
/etc/xdg/defaults/gymhim/OSS-Admin.desktop
/etc/xdg/defaults/gymhim/Webmail.desktop
/etc/xdg/defaults/gymhim/k4dirstat.desktop
/etc/xdg/defaults/gymhim/ch.openboard.OpenBoard.desktop
/etc/xdg/defaults/gymhim/CinqueMinuti.desktop
/etc/xdg/defaults/gymhim/geogebra.desktop
/etc/xdg/defaults/gymhim/gimp.desktop
/etc/xdg/defaults/gymhim/org.kde.dolphin.desktop
/etc/xdg/defaults/gymhim/org.kde.kcalc.desktop
/etc/xdg/defaults/gymhim/org.kde.konsole.desktop
/etc/xdg/defaults/gymhim/org.kde.spectacle.desktop
/etc/xdg/defaults/gymhim/org.kde.kwrite.desktop
/etc/xdg/defaults/gymhim/org.kde.parley.desktop
/etc/xdg/defaults/gymhim/smarttech-notebook.desktop
/usr/share/schule-kde/schule-kde-himmelsthuer.menu
/usr/share/%{name}/plasma-updates/gymhim

%files gymhim-netbook
%defattr(644,root,root,0755)
%config /etc/polkit-default-privs.d/UhrzugriffErlauben
/usr/share/desktop-directories/himmelsthuer.directory
/etc/systemd/system/klassenarbeit.service
/etc/systemd/system/resumeAus.service
/etc/systemd/system/display-manager.service.d/klassenarbeit.conf
%dir /etc/systemd/logind.conf.d
/etc/systemd/logind.conf.d/99-ignore-keys.conf
%attr(755,root,root) /etc/xdg/defaults/startkde.gymhim.sh
/usr/share/desktop-directories/himmelsthuer-*.directory
/usr/share/icons/himmelsthuer-*.png
/etc/xdg/defaults/gymhim/OSS.desktop
/etc/xdg/defaults/gymhim/Dokuwiki.desktop
/etc/xdg/defaults/gymhim/Moodle.desktop
/etc/xdg/defaults/gymhim/firefox.desktop
/etc/xdg/defaults/gymhim/vlc.desktop
/etc/xdg/defaults/gymhim/Reset-Netbook.desktop
/etc/xdg/defaults/gymhim/OSS-Admin.desktop
/etc/xdg/defaults/gymhim/Webmail.desktop
/etc/xdg/defaults/gymhim/k4dirstat.desktop
/etc/xdg/defaults/gymhim/ch.openboard.OpenBoard.desktop
/etc/xdg/defaults/gymhim/CinqueMinuti.desktop
/etc/xdg/defaults/gymhim/geogebra.desktop
/etc/xdg/defaults/gymhim/gimp.desktop
/etc/xdg/defaults/gymhim/org.kde.dolphin.desktop
/etc/xdg/defaults/gymhim/org.kde.kcalc.desktop
/etc/xdg/defaults/gymhim/org.kde.konsole.desktop
/etc/xdg/defaults/gymhim/org.kde.spectacle.desktop
/etc/xdg/defaults/gymhim/org.kde.kwrite.desktop
/etc/xdg/defaults/gymhim/org.kde.parley.desktop
/etc/xdg/defaults/gymhim/smarttech-notebook.desktop
/etc/xdg/defaults/gymhim/xrandr-clone.desktop
/etc/xdg/defaults/gymhim/xrandr-extend.desktop
/usr/share/schule-kde/schule-kde-himmelsthuer-netbook.menu
%attr(700,root,root) /sbin/klassenarbeitAnAus
%attr(700,root,root) /sbin/resumeAus
%attr(755,root,root) /etc/grub.d/01_gymhim
/usr/share/%{name}/plasma-updates/gymhim-netbook
/usr/share/%{name}/plasma-updates/klassenarbeit

%files sas
%defattr(644,root,root,0755)
/etc/xdg/autostart/schulserver-autostart.desktop
/etc/profile.d/schule.sh
/etc/profile.d/schule.csh
/usr/share/desktop-directories/sas.directory
%attr(755,root,root) /etc/xdg/defaults/startkde.sas.sh
/etc/xdg/defaults/sas/Ausgabe_vereinheitlichen.desktop
/etc/xdg/defaults/sas/mimio-notebook.desktop
/etc/xdg/defaults/sas/Dokuwiki.desktop
/etc/xdg/defaults/sas/Moodle.desktop
/etc/xdg/defaults/sas/firefox.desktop
/etc/xdg/defaults/sas/vlc.desktop
/etc/xdg/defaults/sas/Reset.desktop
/etc/xdg/defaults/sas/OSS-Admin.desktop
/etc/xdg/defaults/sas/Webmail.desktop
/etc/xdg/defaults/sas/k4dirstat.desktop
/etc/xdg/defaults/sas/ch.openboard.OpenBoard.desktop
/etc/xdg/defaults/sas/CinqueMinuti.desktop
/etc/xdg/defaults/sas/geogebra.desktop
/etc/xdg/defaults/sas/gimp.desktop
/etc/xdg/defaults/sas/org.kde.dolphin.desktop
/etc/xdg/defaults/sas/org.kde.kcalc.desktop
/etc/xdg/defaults/sas/org.kde.konsole.desktop
/etc/xdg/defaults/sas/org.kde.spectacle.desktop
/etc/xdg/defaults/sas/org.kde.kwrite.desktop
/etc/xdg/defaults/sas/org.kde.parley.desktop
/etc/xdg/defaults/sas/smarttech-notebook.desktop
/usr/share/schule-kde/schule-kde-sas.menu
/usr/share/%{name}/plasma-updates/sas
/usr/share/wallpapers/SAS_Canvas
/usr/share/wallpapers/SAS_Chalk
/usr/share/wallpapers/SAS_Glow
/usr/share/wallpapers/SAS_Ground

%files sas-netbook
%defattr(644,root,root,0755)
%config /etc/polkit-default-privs.d/UhrzugriffErlauben
/usr/share/desktop-directories/sas.directory
/etc/systemd/system/klassenarbeit.service
/etc/systemd/system/resumeAus.service
/etc/systemd/system/display-manager.service.d/klassenarbeit.conf
%dir /etc/systemd/logind.conf.d
/etc/systemd/logind.conf.d/99-ignore-keys.conf
%attr(755,root,root) /etc/xdg/defaults/startkde.sas.sh
/usr/share/desktop-directories/sas-*.directory
/usr/share/icons/sas-*.png
/etc/xdg/defaults/sas/Ausgabe_vereinheitlichen.desktop
/etc/xdg/defaults/sas/mimio-notebook.desktop
/etc/xdg/defaults/sas/Dokuwiki.desktop
/etc/xdg/defaults/sas/Moodle.desktop
/etc/xdg/defaults/sas/firefox.desktop
/etc/xdg/defaults/sas/vlc.desktop
/etc/xdg/defaults/sas/Reset-Netbook.desktop
/etc/xdg/defaults/sas/OSS-Admin.desktop
/etc/xdg/defaults/sas/Webmail.desktop
/etc/xdg/defaults/sas/k4dirstat.desktop
/etc/xdg/defaults/sas/ch.openboard.OpenBoard.desktop
/etc/xdg/defaults/sas/CinqueMinuti.desktop
/etc/xdg/defaults/sas/geogebra.desktop
/etc/xdg/defaults/sas/gimp.desktop
/etc/xdg/defaults/sas/org.kde.dolphin.desktop
/etc/xdg/defaults/sas/org.kde.kcalc.desktop
/etc/xdg/defaults/sas/org.kde.konsole.desktop
/etc/xdg/defaults/sas/org.kde.spectacle.desktop
/etc/xdg/defaults/sas/org.kde.kwrite.desktop
/etc/xdg/defaults/sas/org.kde.parley.desktop
/etc/xdg/defaults/sas/smarttech-notebook.desktop
/etc/xdg/defaults/sas/xrandr-clone.desktop
/etc/xdg/defaults/sas/xrandr-extend.desktop
/usr/share/schule-kde/schule-kde-sas-netbook.menu
%attr(700,root,root) /sbin/klassenarbeitAnAus
%attr(700,root,root) /sbin/resumeAus
%attr(755,root,root) /etc/grub.d/01_sas
/usr/share/%{name}/plasma-updates/sas-netbook
/usr/share/%{name}/plasma-updates/klassenarbeit

%changelog
