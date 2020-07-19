#!/bin/sh
#
# create defaults for kde 5
#
SCHULE=gymhim
ENVDIR=/etc/xdg/defaults/${SCHULE}
if [ ! -e "$HOME/.skel/${SCHULE}" ]; then
    desktop="`xdg-user-dir DESKTOP 2>/dev/null`"
    if test -z "$desktop"; then
        desktop=$HOME/Desktop
    fi


    mkdir -p $desktop

    if test -e $HOME/Medien ; then
        rm -f $HOME/Medien
    fi
    ln -sf /run/media $HOME/Medien

    cp -a $ENVDIR/*.desktop $desktop/
    chmod u+x $desktop/*.desktop

    mkdir -p $HOME/.skel/
    touch $HOME/.skel/${SCHULE}
fi
