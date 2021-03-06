#!/bin/bash
# Office auf Standardwerte zurücksetzen
# Für den Benutzer, der das Skript aufruft, werden
# die Standardwerte wiederhergestellt.
#
if [ "$USER" = "root" -o 0`id -u` = 0 ]; then
    echo "root darf das nicht."
    exit;
fi

DIRS_TO_REMOVE=".config/libreoffice"

CURRENT=`pwd`

if [ "$HOME" = "" ]; then
  echo "Die Variable HOME enthält keinen Wert. Ich breche ab.";
  exit 1;
fi

cd $HOME

for d in $DIRS_TO_REMOVE; do
  if [ "$d" = "" ]; then
    echo "Es wurde kein Verzeichnis übergeben. Ich breche ab.";
  elif [ -e "$d" -a -d "$d" ]; then
    echo "Ich entferne das Verzeichnis $HOME/$d";
    rm -rf "$d"
  elif [ -e "$d" ]; then
    echo "Ich entferne die Datei $HOME/$d";
    rm -f $d
  else
    echo "Nichts zu tun ($HOME/$d)";
  fi
done;

echo "Die Office-Standardwerte wurden wieder hergestellt.";

cd "$CURRENT"

exit 0;
