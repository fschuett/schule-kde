#!/bin/bash
# Dieses Skript ermöglicht das Zurücksetzen ausgewählter
# Programmeinstellungen.
#
# Was soll zurückgesetzt werden?
if [ "$USER" = "root" -o 0`id -u` = 0 ]; then
    echo "root darf das nicht."
    exit;
fi

DIR=`dirname $0`
PROGNR=$(kdialog --radiolist "Zurücksetzen von" 1 "KDE" on 2 "KDE-Arbeitsfläche" off 3 "Firefox" off 4 "JBuilder" off 5 "OpenOffice" off 6 "Wine" off 7 "SMART Software" off 8 "Alle" off)

if [ $? != 0 ]; then
    echo "Abbrechen"
    exit 1;
fi

echo "DIR=$DIR PROGNR=$PROGNR"


case "$PROGNR" in

    1)
	ERGEBNIS=`$DIR/kde_netbook_reset.sh`;
	kdialog --title "KDE zurücksetzen" --passivepopup "$ERGEBNIS"
	;;
	
    2)
	ERGEBNIS=`$DIR/restart-plasma`;
	kdialog --title "KDE-Arbeitsfläche zurücksetzen" --passivepopup "$ERGEBNIS"
	;;
	
    3)
	ERGEBNIS=`$DIR/firefox_reset.sh`;
	kdialog --title "Firefox zurücksetzen" --passivepopup "$ERGEBNIS"
	;;
	
    4)
	ERGEBNIS=`$DIR/netbeans_reset.sh`;
	kdialog --title "Netbeans zurücksetzen" --passivepopup "$ERGEBNIS"
	;;
	
    5)
	ERGEBNIS=`$DIR/office_reset.sh`;
	kdialog --title "Office zurücksetzen" --passivepopup "$ERGEBNIS"
	;;
	
    6)
	ERGEBNIS=`$DIR/wine_reset.sh`;
	kdialog --title "Wine zurücksetzen" --passivepopup "$ERGEBNIS"
	;;
	
    7)
	ERGEBNIS=`$DIR/smartnotebook_netbook_reset.sh`;
	kdialog --title "SMART Software zurücksetzen" --passivepopup "$ERGEBNIS"
	;;
	
    8)
	$DIR/firefox_reset.sh
	$DIR/jbuilder_reset.sh
	$DIR/office_reset.sh
	$DIR/wine_reset.sh
	$DIR/smartnotebook_netbook_reset.sh
	$DIR/kde_netbook_reset.sh
	ERGEBNIS="KDE, Arbeitsfläche, Firefox, JBuilder, SMART Software und Office zurückgesetzt";
	kdialog --title "Alles zurücksetzen" --passivepopup "$ERGEBNIS"
	;;
esac

exit 0;
