#!/bin/bash
# SMART Notebook Software auf Standardwerte zurücksetzen
# Für den Benutzer, der das Skript aufruft, werden
# die Standardwerte wiederhergestellt.
#
if [ "$USER" = "root" -o 0`id -u` = 0 ]; then
    echo "root darf das nicht."
    exit;
fi

CURRENT=`pwd`

if [ "$HOME" = "" ]; then
  echo "Die Variable HOME enthält keinen Wert. Ich breche ab.";
  exit 1;
fi

cd $HOME

d=".SMART Technologies Inc"
# Rechte setzen
if [ -e "$d/SMART Board Software/Gallery" ]; then
  chmod 755 "$d/SMART Board Software/Gallery";
fi
# entfernen
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
# neu erzeugen
mkdir -p "$d/SMART Board Software/Gallery"
chmod 555 "$d/SMART Board Software/Gallery"

# entfernen
d=".config/SMART Technologies"
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

echo "Die SMART Notebook-Standardwerte wurden wieder hergestellt.";

cd "$CURRENT"

exit 0;
