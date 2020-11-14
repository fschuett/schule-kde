#!/bin/bash
# KDE auf Standardwerte zurücksetzen
# Für den Benutzer, der das Skript aufruft, werden
# die Standardwerte wiederhergestellt.
# Nach dem Durchlaufen des Skripts muss sich der
# Benutzer ab- und wieder anmelden.
#

if [ "$USER" = "root" -o 0`id -u` = 0 ]; then
    echo "root darf das nicht."
    exit;
fi

DIRS_TO_CLEAN=$(xdg-user-dir DESKTOP)
DIRS_TO_CLEAN="${DIRS_TO_CLEAN##*/} .config .local .skel .kde .kde4"

CURRENT=`pwd`

if [ "$HOME" = "" ]; then
  echo "Die Variable HOME enthält keinen Wert. Ich breche ab.";
  exit 1;
fi

# find kde cache
KDECACHE=
if [ -L "$KDEHOME/cache-$HOSTNAME" ]; then
    KDECACHE=`readlink "$KDEHOME/cache-$HOSTNAME"`
    echo "Der Link $KDEHOME/cache-$HOSTNAME -> $KDECACHE wurde gefunden."
elif [ -d "${KDEVARTMP}/kdecache-${USER}" ]; then
    KDECACHE="${KDEVARTMP}/kdecache-${USER}"
    echo "Das Verzeichnis mit KDEVARTMP: ${KDEVARTMP}/kdecache-${USER} wurde gefunden."
elif [ -d "/var/tmp/kdecache-$USER" ]; then
    KDECACHE="/var/tmp/kdecache-$USER"
    echo "Das Standardverzeichnis $KDECACHE wurde gefunden."
fi
# clean other dirs
cd $HOME

for d in $DIRS_TO_CLEAN; do
  if [ -e "$d" -a -d "$d" ]; then
    (
      if [ ! -e "backup" ]; then
        mkdir -p backup
      fi
      tar xcf "backup/${d#.}.tar.gz" $d
      cd $d;
      if [ "`pwd`" = "$HOME/$d" ]; then
	echo "Ich leere das Verzeichnis $HOME/$d";
	rm -rf * .[^.]* ..?*
	cd ..
	rmdir $d
      else
	echo "Das Verzeichnis sollte $HOME/$d sein, ist aber `pwd`. Ich breche ab.";
      fi
    )
  elif [ -e "$d" ]; then
    echo "Ich entferne die Datei $HOME/$d";
    rm -f $d
  else
    echo "Nichts zu tun($HOME/$d)";
  fi
done;

# clean kde cache
if [ ! -z "${KDECACHE}" ]; then
    if [ -d "${KDECACHE}" ]; then
        echo "Ich wechsle in ${KDECACHE}"
	(
        cd "${KDECACHE}"
        if [ "`pwd`" == "${KDECACHE}" ]; then
	    echo "Ich leere den KDECACHE unter ${KDECACHE}"
	    rm -rf * .[^.]* ..?*
	fi
        )
    fi
fi

echo "Bitte melden Sie sich neu an. Ich melde Sie jetzt ab.";
sleep 5

qdbus org.kde.ksmserver /KSMServer logout 0 0 0

cd "$CURRENT"

exit 0;
