Name:         schule-kde
Summary:      KDE installation files and menu for a school
BuildArch:    noarch
Version:      5.18
Release:      1
License:      GPL
Group:        application
Source:       %{name}-%{version}.tar.gz
Source1:      %{name}-himmelsthuer.menu
Source2:      %{name}-sas.menu
Source5:      schule-programme
Source51:     himmelsthuer-programme
Source52:     sas-programme
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
Patch1:       %{name}-desktop-file.patch
Packager:     fschuett
Distribution: openSUSE Linux
Prefix:       /usr
Url:          http://www.gymnasium-himmelsthuer.de
Provides:     schule-kde4
Obsoletes:    schule-kde4
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
BuildRequires: netbeans_de
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
Requires: netbeans_de
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
Provides:     schule-kde-gymhim gymhim-kde schule-kde4-gymhim
Obsoletes:    schule-kde4-gymhim
Requires:     schule-kde

%description gymhim
KDE Installationsdateien für das Gymnasium Himmelsthür. Es enthält ein Menü
und einige Desktop-Symbole.

%package gymhim-netbook
Summary:      kde Installation für das Gymnasium Himmelsthür auf einem Netbook
BuildArch:    noarch
Provides:     schule-kde-gymhim schule-kde4-gymhim schule-kde-gymhim-netbook schule-kde4-gymhim-netbook
Obsoletes:    schule-kde4-gymhim-netbook
Requires:     schule-kde

%description gymhim-netbook
KDE Installationsdateien für das Gymnasium Himmelsthür auf einem Netbook. Es
enthält ein Sal-Menü und einige Desktop-Symbole.

%package sas
Summary:      kde Installation für die Sankt-Ansgar-Schule
BuildArch:    noarch
Provides:     schule-kde-sas schule-kde4-sas
Obsoletes:    schule-kde4-sas
Requires:     schule-kde
BuildRequires: schule-wine-derive

%description sas
KDE Installationsdateien für die Sankt-Ansgar-Schule. Es enthält ein Menü
und einige Desktop-Symbole.

%package sas-netbook
Summary:      kde Installation für die Sankt-Ansgar-Schule auf einem Netbook
BuildArch:    noarch
Provides:     schule-kde-sas schule-kde-sas-netbook schule-kde4-sas schule-kde4-sas-netbook
Obsoletes:    schule-kde4-sas-netbook
Requires:     schule-kde

%description sas-netbook
KDE Installationsdateien für die Sankt-Ansgar-Schule auf einem Netbook. Es
enthält ein Sal-Menü und einige Desktop-Symbole.

%prep
%setup -q

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
build_desktop_entries himmelsthuer %{SOURCE5} X-Himmelsthür
build_desktop_entries sas %{SOURCE5} X-SanktAnsgar
build_desktop_entries himmelsthuer %{SOURCE51} X-Himmelsthür
build_desktop_entries sas %{SOURCE52} X-SanktAnsgar
# correct errors in desktop files
patch -p1 <%{PATCH1}

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
install -D -m 644 -o root -g root %{SOURCE1} %{buildroot}%{_datadir}/schule-kde/%{name}-himmelsthuer.menu
install -D -m 644 -o root -g root %{SOURCE61} %{buildroot}%{_datadir}/schule-kde/%{name}-himmelsthuer-netbook.menu
install -D -m 644 -o root -g root %{SOURCE2} %{buildroot}%{_datadir}/schule-kde/%{name}-sas.menu
install -D -m 644 -o root -g root %{SOURCE62} %{buildroot}%{_datadir}/schule-kde/%{name}-sas-netbook.menu
install -D -m 644 -o root -g root %{SOURCE7} %{buildroot}/etc/xdg/autostart/schulserver-autostart.desktop
install -D -m 644 -o root -g root %{SOURCE8} %{buildroot}/etc/polkit-default-privs.d/UhrzugriffErlauben
install -D -m 644 -o root -g root %{SOURCE9} %{buildroot}/etc/xdg/akonadi/akonadiserverrc
install -D -m 644 -o root -g root %{SOURCE13} %{buildroot}%{_sysconfdir}/profile.d/schule.sh
install -D -m 644 -o root -g root %{SOURCE14} %{buildroot}%{_sysconfdir}/profile.d/schule.csh
install -D -m 644 -o root -g root %{SOURCE20} %{buildroot}/etc/systemd/system/klassenarbeit.service
install -D -m 700 -o root -g root %{SOURCE21} %{buildroot}/sbin/klassenarbeitAnAus
install -D -m 755 -o root -g root %{SOURCE22} %{buildroot}/etc/grub.d/01_gymhim
install -D -m 755 -o root -g root %{SOURCE25} %{buildroot}/etc/grub.d/01_sas
install -D -m 644 -o root -g root %{SOURCE23} %{buildroot}/etc/systemd/system/resumeAus.service
install -D -m 700 -o root -g root %{SOURCE24} %{buildroot}/sbin/resumeAus
install -D -m 755 -o root -g root %{SOURCE26} %{buildroot}/etc/systemd/system/display-manager.service.d/klassenarbeit.conf

%post
# add application defaults to mimeapps.list
ML=/etc/xdg/mimeapps.list
if [ ! -f $ML ]; then
  touch $ML
fi
if ! grep -q '[DefaultApplications]' $ML; then
  echo '[DefaultApplications]'>>$ML
fi
for L in application/ogg=vlc.desktop application/x-shockwave-flash=vlc.desktop audio/m3u=vlc.desktop\
 audio/mp4=vlc.desktop audio/mpeg=vlc.desktop audio/ogg=vlc.desktop audio/vnd.rn-realaudio=vlc.desktop\
 audio/vorbis=vlc.desktop audio/x-flac=vlc.desktop audio/x-flac+ogg=vlc.desktop audio/x-m4b=vlc.desktop\
 audio/x-matroska=vlc.desktop audio/x-mpegurl=vlc.desktop audio/x-ms-wma=vlc.desktop audio/x-oggflac=vlc.desktop\
 audio/x-scpls=vlc.desktop audio/x-speex+ogg=vlc.desktop audio/x-vorbis+ogg=vlc.desktop audio/x-wav=vlc.desktop\
 video/ogg=vlc.desktop video/x-matroska=vlc.desktop video/x-ms-asf=vlc.desktop video/x-ogm+ogg=vlc.desktop\
 video/x-theora=vlc.desktop; do
  if ! grep -q "$L" $ML; then
    echo "$L">>$ML
  fi
done

# mime type handling / system icon links and mime database
/usr/bin/update-mime-database /usr/share/mime
/usr/bin/update-desktop-database

%post gymhim
SCHULE=gymhim
BINDIR=/usr/bin
[ -e "$BINDIR/schulserver-notification" ] && rm -f "$BINDIR/schulserver-notification"
[ -e "$BINDIR/schulserver-notification-${SCHULE}" ] && ln -sf "$BINDIR/schulserver-notification-${SCHULE}" "$BINDIR/schulserver-notification"
ENVDIR=/etc/xdg/plasma-workspace/env
ENVCONFDIR=/etc/xdg/defaults
[ -e "$ENVDIR/startkde.schule.sh" ] && rm -f "$ENVDIR/startkde.schule.sh"
[ -e "$ENVCONFDIR/startkde.${SCHULE}.sh" ] && ln -sf "$ENVCONFDIR/startkde.${SCHULE}.sh" "$ENVDIR/startkde.schule.sh"
MENUDIR=/etc/xdg/menus/applications-merged
SCHULEDIR=/usr/share/schule-kde
[ -e "$MENUDIR/schule.menu" ] && rm -f "$MENUDIR/schule.menu"
[ -e "$SCHULEDIR/schule-kde-himmelsthuer.menu" ] && ln -s "$SCHULEDIR/schule-kde-himmelsthuer.menu" "$MENUDIR/schule.menu"
PLASMADIR=/usr/share/plasma/shells/org.kde.plasma.desktop/contents/updates
rm -f $SCHULEDIR/plasma-updates/schule
ln -sf $SCHULEDIR/plasma-updates/${SCHULE} $SCHULEDIR/plasma-updates/schule
for p in $(find -L $SCHULEDIR/plasma-updates/{all,schule}/*.js); do
    f=$(basename $p)
    rm -f $PLASMADIR/$f
    ln -sf $p $PLASMADIR/$f
done;
PIXMAPDIR=/usr/share/icons
[ -e "$PIXMAPDIR/schulserver.png" ] && rm -f "$PIXMAPDIR/schulesrver.png"
[ -e "$PIXMAPDIR/himmelsthuer.png" ] && ln -sf "$PIXMAPDIR/himmelsthuer.png" "$PIXMAPDIR/schulserver.png"

%post gymhim-netbook
SCHULE=gymhim
ENVDIR=/etc/xdg/plasma-workspace/env
ENVCONFDIR=/etc/xdg/defaults
[ -e "$ENVDIR/startkde.schule.sh" ] && rm -f "$ENVDIR/startkde.schule.sh"
[ -e "$ENVCONFDIR/startkde.${SCHULE}.sh" ] && ln -sf "$ENVCONFDIR/startkde.${SCHULE}.sh" "$ENVDIR/startkde.schule.sh"
MENUDIR=/etc/xdg/menus/applications-merged
SCHULEDIR=/usr/share/schule-kde
[ -e "$MENUDIR/schule.menu" ] && rm -f "$MENUDIR/schule.menu"
PLASMADIR=/usr/share/plasma/shells/org.kde.plasma.desktop/contents/updates
rm -f $SCHULEDIR/plasma-updates/schule
ln -sf $SCHULEDIR/plasma-updates/${SCHULE}-netbook $SCHULEDIR/plasma-updates/schule
for p in $(find -L $SCHULEDIR/plasma-updates/{all,schule}/*.js); do
    f=$(basename $p)
    rm -f $PLASMADIR/$f
    ln -sf $p $PLASMADIR/$f
done;
PIXMAPDIR=/usr/share/icons
[ -e "$PIXMAPDIR/schulserver.png" ] && rm -f "$PIXMAPDIR/schulserver.png"
[ -e "$PIXMAPDIR/himmelsthuer.png" ] && ln -sf "$PIXMAPDIR/himmelsthuer.png" "$PIXMAPDIR/schulserver.png"
[ -x /sbin/set_polkit_default_privs ] && /sbin/set_polkit_default_privs
systemctl enable klassenarbeit.service
systemctl enable resumeAus.service
systemctl daemon-reload

%post sas
SCHULE=sas
BINDIR=/usr/bin
[ -e "$BINDIR/schulserver-notification" ] && rm -f "$BINDIR/schulserver-notification"
[ -e "$BINDIR/schulserver-notification-${SCHULE}" ] && ln -sf "$BINDIR/schulserver-notification-${SCHULE}" "$BINDIR/schulserver-notification"
ENVDIR=/etc/xdg/plasma-workspace/env
ENVCONFDIR=/etc/xdg/defaults
[ -e "$ENVDIR/startkde.schule.sh" ] && rm -f "$ENVDIR/startkde.schule.sh"
[ -e "$ENVCONFDIR/startkde.${SCHULE}.sh" ] && ln -sf "$ENVCONFDIR/startkde.${SCHULE}.sh" "$ENVDIR/startkde.schule.sh"
MENUDIR=/etc/xdg/menus/applications-merged
SCHULEDIR=/usr/share/schule-kde
[ -e "$MENUDIR/schule.menu" ] && rm -f "$MENUDIR/schule.menu"
[ -e "$SCHULEDIR/schule-kde-himmelsthuer.menu" ] && ln -s "$SCHULEDIR/schule-kde-himmelsthuer.menu" "$MENUDIR/schule.menu"
PLASMADIR=/usr/share/plasma/shells/org.kde.plasma.desktop/contents/updates
rm -f $SCHULEDIR/plasma-updates/schule
ln -sf $SCHULEDIR/plasma-updates/${SCHULE} $SCHULEDIR/plasma-updates/schule
for p in $(find -L $SCHULEDIR/plasma-updates/{all,schule}/*.js); do
    f=$(basename $p)
    rm -f $PLASMADIR/$f
    ln -sf $p $PLASMADIR/$f
done;
PIXMAPDIR=/usr/share/icons
[ -e "$PIXMAPDIR/schulserver.png" ] && rm -f "$PIXMAPDIR/schulesrver.png"
[ -e "$PIXMAPDIR/himmelsthuer.png" ] && ln -sf "$PIXMAPDIR/himmelsthuer.png" "$PIXMAPDIR/schulserver.png"

%post sas-netbook
SCHULE=sas
ENVDIR=/etc/xdg/plasma-workspace/env
ENVCONFDIR=/etc/xdg/defaults
[ -e "$ENVDIR/startkde.schule.sh" ] && rm -f "$ENVDIR/startkde.schule.sh"
[ -e "$ENVCONFDIR/startkde.${SCHULE}.sh" ] && ln -sf "$ENVCONFDIR/startkde.${SCHULE}.sh" "$ENVDIR/startkde.schule.sh"
MENUDIR=/etc/xdg/menus/applications-merged
SCHULEDIR=/usr/share/schule-kde
[ -e "$MENUDIR/schule.menu" ] && rm -f "$MENUDIR/schule.menu"
PLASMADIR=/usr/share/plasma/shells/org.kde.plasma.desktop/contents/updates
rm -f $SCHULEDIR/plasma-updates/schule
ln -sf $SCHULEDIR/plasma-updates/${SCHULE}-netbook $SCHULEDIR/plasma-updates/schule
for p in $(find -L $SCHULEDIR/plasma-updates/{all,schule}/*.js); do
    f=$(basename $p)
    rm -f $PLASMADIR/$f
    ln -sf $p $PLASMADIR/$f
done;
PIXMAPDIR=/usr/share/icons
[ -e "$PIXMAPDIR/schulserver.png" ] && rm -f "$PIXMAPDIR/schulserver.png"
[ -e "$PIXMAPDIR/himmelsthuer.png" ] && ln -sf "$PIXMAPDIR/himmelsthuer.png" "$PIXMAPDIR/schulserver.png"
[ -x /sbin/set_polkit_default_privs ] && /sbin/set_polkit_default_privs
systemctl enable klassenarbeit.service
systemctl enable resumeAus.service
systemctl daemon-reload


%preun
if [ $1 -gt 0 ]; then
  exit 0;
fi
# mime type handling / remove system icon links

%preun gymhim
if [ $1 -gt 0 ]; then
  exit 0;
fi
BINDIR=/usr/bin
[ -e "$BINDIR/schulserver-notification" ] && rm -f "$BINDIR/schulserver-notification"
ENVDIR=/etc/xdg/plasma-workspace/env
FILE=startkde.schule.sh
[ -e "$ENVDIR/$FILE" ] && rm -f "$ENVDIR/$FILE"
SCHULEDIR=/usr/share/schule-kde
PLASMADIR=/usr/share/plasma/shells/org.kde.plasma.desktop/contents/updates
for p in $(find -L $SCHULEDIR/plasma-updates/{all,schule}/*.js); do
    f=$(basename $p)
    rm -f $PLASMADIR/$f
done;
rm -f $SCHULEDIR/plasma-updates/schule
MENUDIR=/etc/xdg/menus/applications-merged
[ -e "$MENUDIR/schule.menu" ] && rm -f "$MENUDIR/schule.menu"
PIXMAPDIR=/usr/share/icons
[ -e "$PIXMAPDIR/schulserver.png" ] && rm -f "$PIXMAPDIR/schulserver.png"

%preun gymhim-netbook
if [ $1 -gt 0 ]; then
  exit 0;
fi
ENVDIR=/etc/xdg/plasma-workspace/env
FILE=startkde.schule.sh
[ -e "$ENVDIR/$FILE" ] && rm -f "$ENVDIR/$FILE"
SCHULEDIR=/usr/share/schule-kde
PLASMADIR=/usr/share/plasma/shells/org.kde.plasma.desktop/contents/updates
for p in $(find -L $SCHULEDIR/plasma-updates/{all,schule}/*.js); do
    f=$(basename $p)
    rm -f $PLASMADIR/$f
done;
rm -f $SCHULEDIR/plasma-updates/schule
MENUDIR=/etc/xdg/menus/applications-merged
[ -e "$MENUDIR/schule.menu" ] && rm -f "$MENUDIR/schule.menu"
PIXMAPDIR=/usr/share/icons
[ -e "$PIXMAPDIR/schulserver.png" ] && rm -f "$PIXMAPDIR/schulserver.png"
systemctl disable klassenarbeit.service
systemctl disable resumeAus.service

%preun sas
if [ $1 -gt 0 ]; then
  exit 0;
fi
BINDIR=/usr/bin
[ -e "$BINDIR/schulserver-notification" ] && rm -f "$BINDIR/schulserver-notification"
ENVDIR=/etc/xdg/plasma-workspace/env
FILE=startkde.schule.sh
[ -e "$ENVDIR/$FILE" ] && rm -f "$ENVDIR/$FILE"
SCHULEDIR=/usr/share/schule-kde
PLASMADIR=/usr/share/plasma/shells/org.kde.plasma.desktop/contents/updates
for p in $(find -L $SCHULEDIR/plasma-updates/{all,schule}/*.js); do
    f=$(basename $p)
    rm -f $PLASMADIR/$f
done;
rm -f $SCHULEDIR/plasma-updates/schule
MENUDIR=/etc/xdg/menus/applications-merged
[ -e "$MENUDIR/schule.menu" ] && rm -f "$MENUDIR/schule.menu"
PIXMAPDIR=/usr/share/icons
[ -e "$PIXMAPDIR/schulserver.png" ] && rm -f "$PIXMAPDIR/schulserver.png"

%preun sas-netbook
if [ $1 -gt 0 ]; then
  exit 0;
fi
ENVDIR=/etc/xdg/plasma-workspace/env
FILE=startkde.schule.sh
[ -e "$ENVDIR/$FILE" ] && rm -f "$ENVDIR/$FILE"
SCHULEDIR=/usr/share/schule-kde
PLASMADIR=/usr/share/plasma/shells/org.kde.plasma.desktop/contents/updates
for p in $(find -L $SCHULEDIR/plasma-updates/{all,schule}/*.js); do
    f=$(basename $p)
    rm -f $PLASMADIR/$f
done;
rm -f $SCHULEDIR/plasma-updates/schule
MENUDIR=/etc/xdg/menus/applications-merged
[ -e "$MENUDIR/schule.menu" ] && rm -f "$MENUDIR/schule.menu"
PIXMAPDIR=/usr/share/icons
[ -e "$PIXMAPDIR/schulserver.png" ] && rm -f "$PIXMAPDIR/schulserver.png"
systemctl disable klassenarbeit.service
systemctl disable resumeAus.service

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
/etc/xdg/defaults/gymhim/CinqueMinuti.desktop
/etc/xdg/defaults/gymhim/geogebra.desktop
/etc/xdg/defaults/gymhim/gimp.desktop
/etc/xdg/defaults/gymhim/org.kde.dolphin.desktop
/etc/xdg/defaults/gymhim/org.kde.kcalc.desktop
/etc/xdg/defaults/gymhim/org.kde.konsole.desktop
/etc/xdg/defaults/gymhim/org.kde.spectacle.desktop
/etc/xdg/defaults/gymhim/org.kde.kwrite.desktop
/etc/xdg/defaults/gymhim/org.kde.parley.desktop
/etc/xdg/defaults/gymhim/sankore.desktop
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
/etc/xdg/defaults/gymhim/CinqueMinuti.desktop
/etc/xdg/defaults/gymhim/geogebra.desktop
/etc/xdg/defaults/gymhim/gimp.desktop
/etc/xdg/defaults/gymhim/org.kde.dolphin.desktop
/etc/xdg/defaults/gymhim/org.kde.kcalc.desktop
/etc/xdg/defaults/gymhim/org.kde.konsole.desktop
/etc/xdg/defaults/gymhim/org.kde.spectacle.desktop
/etc/xdg/defaults/gymhim/org.kde.kwrite.desktop
/etc/xdg/defaults/gymhim/org.kde.parley.desktop
/etc/xdg/defaults/gymhim/sankore.desktop
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
/etc/xdg/defaults/sas/OSS.desktop
/etc/xdg/defaults/sas/Dokuwiki.desktop
/etc/xdg/defaults/sas/Moodle.desktop
/etc/xdg/defaults/sas/firefox.desktop
/etc/xdg/defaults/sas/vlc.desktop
/etc/xdg/defaults/sas/Reset.desktop
/etc/xdg/defaults/sas/OSS-Admin.desktop
/etc/xdg/defaults/sas/Webmail.desktop
/etc/xdg/defaults/sas/k4dirstat.desktop
/etc/xdg/defaults/sas/CinqueMinuti.desktop
/etc/xdg/defaults/sas/geogebra.desktop
/etc/xdg/defaults/sas/gimp.desktop
/etc/xdg/defaults/sas/org.kde.dolphin.desktop
/etc/xdg/defaults/sas/org.kde.kcalc.desktop
/etc/xdg/defaults/sas/org.kde.konsole.desktop
/etc/xdg/defaults/sas/org.kde.spectacle.desktop
/etc/xdg/defaults/sas/org.kde.kwrite.desktop
/etc/xdg/defaults/sas/org.kde.parley.desktop
/etc/xdg/defaults/sas/sankore.desktop
/etc/xdg/defaults/sas/smarttech-notebook.desktop
/usr/share/schule-kde/schule-kde-sas.menu
/usr/share/%{name}/plasma-updates/sas

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
/etc/xdg/defaults/sas/OSS.desktop
/etc/xdg/defaults/sas/Dokuwiki.desktop
/etc/xdg/defaults/sas/Moodle.desktop
/etc/xdg/defaults/sas/firefox.desktop
/etc/xdg/defaults/sas/vlc.desktop
/etc/xdg/defaults/sas/Reset-Netbook.desktop
/etc/xdg/defaults/sas/OSS-Admin.desktop
/etc/xdg/defaults/sas/Webmail.desktop
/etc/xdg/defaults/sas/k4dirstat.desktop
/etc/xdg/defaults/sas/CinqueMinuti.desktop
/etc/xdg/defaults/sas/geogebra.desktop
/etc/xdg/defaults/sas/gimp.desktop
/etc/xdg/defaults/sas/org.kde.dolphin.desktop
/etc/xdg/defaults/sas/org.kde.kcalc.desktop
/etc/xdg/defaults/sas/org.kde.konsole.desktop
/etc/xdg/defaults/sas/org.kde.spectacle.desktop
/etc/xdg/defaults/sas/org.kde.kwrite.desktop
/etc/xdg/defaults/sas/org.kde.parley.desktop
/etc/xdg/defaults/sas/sankore.desktop
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
* Mon Dec 16 2019 fschuett@gymhim.de
- remove jbuilder_reset, add netbeans_reset
* Fri Nov 23 2018 fschuett@gymhim.de
- fix resumeAus: labels did not work
* Thu Nov 15 2018 fschuett@gymhim.de
- netbook background 2019.1
* Fri Nov 9 2018 fschuett@gymhim.de
- remove syslinux netbook install files as obsolete
- remove maxima
- fix resumeAus to use labels
* Thu Mar 8 2018 fschuett@gymhim.de
- fix: missing background (find -L to follow links)
* Wed Nov 1 2017 fschuett@gymhim.de
- update mimeapps.list in postin
* Wed Oct 25 2017 fschuett@gymhim.de
- add Dokuwiki, Moodle, OSS, OSS-Admin
- add some pixmaps
* Wed Aug 30 2017 fschuett@gymhim.de
- add syslinux netbook install files
* Wed Aug 23 2017 fschuett@gymhim.de
- remove multilogin
- remove epoptes
* Wed Jun 7 2017 fschuett@gymhim.de
- set XDG_CACHE_HOME=/var/tmp/xdgcache-$USER in schule.[c|]sh
* Wed May 24 2017 fschuett@gymhim.de
- added mimeapps.list with default vlc for video types
* Tue Apr 11 2017 fschuett@gymhim.de
- add home to defaults
- remove fix_launcher (not working anyway)
* Wed Feb 1 2017 fschuett@gymhim.de
- remove kmplot, kig
- fix UhrzugriffErlauben
- remove kde3 dir
- add systemd/logind.conf to ignore power button key
- fix klassenarbeitAnAus
* Thu Jan 5 2017 fschuett@gymhim.de
- change name to kde to reflect kde 5.8.3 using that name
- kde main dir is no longer /usr/share/kde4 but /usr/share
- syslinux is the boot manager used for efi systems
- remove plasma netbook shell
- remove ksimus, kde-q7z
- add ark
* Fri Apr 1 2016 fschuett@gymhim.de
- updated rosegarden deps
* Mon Dec 14 2015 fschuett@gymhim.de
- Fix race condition in klassenarbeit.service / display-manager.service
- Remove borland dependency.
* Fri Oct 30 2015 fschuett@gymhim.de
- open klassenarbeit panel for klassenarbeitwaechter
* Tue Jul 21 2015 fschuett@gymhim.de
- add kmarblerc
- remove rest of krandrtray, update netbook sas with klassenarbeit
* Tue Mar 17 2015 fschuett@gymhim.de
- remove lyx to get rid of texlive
- fix buildrequires geogebra -> geogebra5
* Mon Dec 15 2014 fschuett@gymnasium-himmelsthuer.de
- 01_gymhim Pfade korrigiert, Zugriff korrigiert
- LINBO local korrigiert
- Netbook: 2015.1
- *.pkla entfernt, stattdessen UhrzugriffErlauben
- Klassenarbeitsmodus leert /tmp,/var/tmp,/var/spool/mail
- Fix resumeAus.service verursacht zyklische Abhängigkeit.
* Thu Dec 11 2014 fschuett@gymnasium-himmelsthuer.de
- Die Netzwerkpfad werden jetzt in schule.* hinter den
  Standardpfaden eingefügt, damit Fehler bei der Installation
  der Smartboard-Programme verschwinden.
- Requires smart-notebook,epoptes entfernt.
* Wed Dec 3 2014 fschuett@gymnasium-himmelsthuer.de
- geogebra44 -> geogebra5
- kdirstat -> k4dirstat
* Tue Aug 5 2014 fschuett@gymnasium-himmelsthuer.de
- desktoptheme klassenarbeit
- lan driver wegraeumen
- Klassenarbeitsmodus: Mount-Rechte weg
* Wed Apr 2 2014 fschuett@gymnasium-himmelsthuer.de
- Klassenarbeitsmodus: resumeAus, resumeAus.service
- 01_gymhim hat jetzt das root-Passwort
* Tue Feb 25 2014 fschuett@gymnasium-himmelsthuer.de
- removed 10.16.1.1 from startkde.multilogin.sh
* Fri Dec 27 2013 fschuett@gymnasium-himmelsthuer.de
- removed Archimedes, acroread, mysql-workbench
- changed geogebra -> geogebra44
* Thu Nov 14 2013 fschuett@gymnasium-himmelsthuer.de
- Klassenarbeitsmodus: js-Datei, png/xcf-Datei
- klassenarbeit.service: startet klassenarbeitAnAus
- klassenarbeitAnAus: schaltet Klassenarbeitsmodus ein/aus
- 01_gymhim Bootmenue
* Thu Sep 12 2013 fschuett@gymnasium-himmelsthuer.de
- neu: kalzium
- korrigiert firefox_reset.sh
- neu: smartnotebook_reset.sh, smartnotebook_netbook_reset.sh
- digital-clock mit Datum
- geogebra5 existiert nicht mehr
* Tue Jun 4 2013 fschuett@gymnasium-himmelsthuer.de
- restart-plasma netbook-fähig
- reset-netbook.sh
- Netbook-Seite1 Programme
- kde_netbook_reset.sh
- schule.[c]sh, schulserver-autostart, setInitialActivity verschoben
- added schule-kde4-gymhim-plasma-netbook.js
- added krandrtray-autostart.desktop.live
- jetzt standardmäßig netbook shell
- startkde.gymhim.sh verweist auf die richtige Arbeitsfläche mit xdg-user-dir
- startkde.gymhim.sh legt Link auf Medien an
* Mon Jun 3 2013 fschuett@gymnasium-himmelsthuer.de
- added solfege
- added netbook wallpaper
- added gymhim wallpaper source xcf
- removed selfphp, selflinux, selfhtml
- added Martins symbols
- geogebra5
* Thu Dec 27 2012 fschuett@gymnasium-himmelsthuer.de
- added geogebra5, removed geogebra-beta
- added cinqueminuti-help
* Tue Sep 11 2012 fschuett@gymnasium-himmelsthuer.de
- added network locations for XDG_DATA_DIRS, XDG_CONFIG_DIRS
- added imagej, imagej-plugins-astronomy
* Wed Jul 11 2012 fschuett@gymnasium-himmelsthuer.de
- corrected kde_reset .kde -> .kde.xxx
* Sun Jul 8 2012 fschuett@gymnasium-himmelsthuer.de
- added sas-netbook
- added school specific programs
- added reset programs
- removed Diskette finally
- added wine_reset.sh
* Sat May 12 2012 fschuett@gymnasium-himmelsthuer.de
- added Rosegarden4
- added qsynth
- added musescore
* Mon Mar 12 2012 fschuett@gymnasium-himmelsthuer.de
- change initial activity to desktop icons
- change wallpaper in activities
* Wed Feb 29 2012 fschuett@gymnasium-himmelsthuer.de
- changed netbeans -> netbeans_de (7.1)
* Tue Feb 28 2012 fschuett@gymnasium-himmelsthuer.de
- added akonadiserverrc for switch to smaller sql lib sqlite3
* Thu Feb 2 2012 fschuett@gymnasium-himmelsthuer.de
- added kcmclock save right (polkit)
- renamed MozillaFirefox.desktop -> firefox.desktop
* Mon Jan 30 2012 fschuett@gymnasium-himmelsthuer.de
- kdirstat/KDE3
- schulserver-notifications
- knotify.py
- apps/schulserver
- schulserver.png als link von himmelsthuer/sas.png in post,preun von gymhim,gymhim-netbook,sas
* Sat Dec 10 2011 fschuett@gymnasium-himmelsthuer.de
- netbook.menu
- removed VirtualLab
- changed mysql* -> mysql-workbench
- added subject icons
* Thu Nov 24 2011 fschuett@gymnasium-himmelsthuer.de
- Added okteta, Archimedes.
- Added generation of categories in desktop files from schule-programme
* Thu Nov 3 2011 fschuett@gymnasium-himmelsthuer.de
- removed freemind.desktop
- added VirtualLab.desktop, ksimus.desktop, ktechlab.desktop
* Wed Oct 12 2011 fschuett@gymnasium-himmelsthuer.de
- added Deutsch, Religion
* Thu Jul 7 2011 fschuett@gymnasium-himmelsthuer.de
- added subpackages
- added reset
* Fri Apr 15 2011 fschuett@gymnasium-himmelsthuer.de
- added kmplot, vym (replacing freemind)
* Mon Nov 8 2010 fschuett@gymnasium-himmelsthuer.de
- added X-...
- added desktop_database macros
* Sat Nov 6 2010 fschuett@gymnasium-himmelsthuer.de
- added musikus
* Sat Sep 25 2010 fschuett@gymnasium-himmelsthuer.de
- updated geogebra.desktop
- removed dependency tipp10
* Wed Sep 8 2010 fschuett@gymnasium-himmelsthuer.de
- added x-wxMaxima file type
- added links to icon theme dirs
* Wed Sep 1 2010 fschuett@gymnasium-himmelsthuer.de
- fixed Categories trailing semikolon
* Sat Jul 24 2010 fschuett@gymnasium-himmelsthuer.de
- changed home.desktop to start dolphin
- added tuxtype, Menu Tastatur, changed vnd.scribus
- fixed Diskette.desktop
* Thu Mar 11 2010 fschuett@gymnasium-himmelsthuer.de
- smartboard-Eintrag aus startkde.gymhim.sh entfernt
- Menü: Videobearbeitung kdenlive, avidemux hinzugefügt
* Sat Dec 12 2009 fschuett@gymnasium-himmelsthuer.de
- Release 2
- wine.desktop korrigiert, himmelsthuer.menu korrigiert
- Version 1.1
- wine.desktop hinzugefügt
- Verknüpfung zu EXE-Dateien hinzugefügt
- wine.png, winestartfile hinzugefügt
- wine.xml hinzugefügt
