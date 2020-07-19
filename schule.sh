# schule.sh
# Konfigurationsdateien der Linux-Netzwerkprogramme
#
# uniquefy_search_path (search_path):
#
# Remove duplicate entries from a search path string, preserving order.
uniquefy_search_path ()
{
  OIFS="$IFS"
  IFS='
'
  set -- $(echo ${1+"$@"} | sed -r 's@/*:|([^\\]):@\1\n@g;H;x;s@/\n@\n@')
  IFS="$OIFS"

  _y=""
  for _x ; do
    case ":${_y}:" in
      *:"${_x}":*) continue
    esac
    _y=${_y:+"$_y:"}${_x}
  done

  echo "${_y}"
  unset _y _x
}

xdgdir=/home/software/progs/share
if [ -e "$xdgdir" ] ; then
   if test -d "$xdgdir" && test -d "$xdgdir/applications"; then
      if test -z "$XDG_DATA_DIRS"; then
         XDG_DATA_DIRS="/usr/share:$xdgdir"
      else
         XDG_DATA_DIRS="$XDG_DATA_DIRS:$xdgdir"
      fi
   fi
fi

XDG_DATA_DIRS=$(uniquefy_search_path "$XDG_DATA_DIRS")
export XDG_DATA_DIRS

xdgdir=/home/software/progs/xdg
if [ -e "$xdgdir" ] ; then
   if test -d "$xdgdir"; then
      if test -z "$XDG_CONFIG_DIRS"; then
         XDG_CONFIG_DIRS="/etc/xdg:$xdgdir"
      else
         XDG_CONFIG_DIRS="$XDG_CONFIG_DIRS:$xdgdir"
      fi
   fi
fi

XDG_CONFIG_DIRS=$(uniquefy_search_path "$XDG_CONFIG_DIRS")
export XDG_CONFIG_DIRS

unset xdgdir

# could be more paranoid, and not accept any previously defined XDG_CACHE_HOME
if [ -z "${XDG_CACHE_HOME}" ] ; then
  XDG_CACHE_HOME="/var/tmp/xdgcache-${USER}"
  export XDG_CACHE_HOME
fi

if [ -d "${XDG_CACHE_HOME}" ]; then
  # verify existing dir is suitable
  if ! `test -G "${XDG_CACHE_HOME}" -a -w "${XDG_CACHE_HOME}"` ; then
    # else, make a new/secure one with mktemp
    XDG_CACHE_HOME="$(mktemp -d ${XDG_CACHE_HOME}-XXXXXX)"
    export XDG_CACHE_HOME
  fi
else
  mkdir -p "${XDG_CACHE_HOME}" 
fi
