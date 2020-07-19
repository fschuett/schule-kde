if ( ! ${?XDG_DATA_DIRS} ) then
    set XDG_DATA_DIRS="/usr/share"
else
    set XDG_DATA_DIRS=(${XDG_DATA_DIRS:as/:/ /})
endif
set nonomatch
foreach xdgdir (/home/software/progs/share)
    if ( -d "$xdgdir" ) then
        set -l XDG_DATA_DIRS=($XDG_DATA_DIRS $xdgdir)
    endif
end
unset nonomatch

set    xdgdir="${XDG_DATA_DIRS:q}"
unset  XDG_DATA_DIRS
setenv XDG_DATA_DIRS "${xdgdir:as/ /:/}"
unset  xdgdir

if ( ! ${?XDG_CONFIG_DIRS} ) then
    set XDG_CONFIG_DIRS="/etc/xdg"
else
    set XDG_CONFIG_DIRS=(${XDG_CONFIG_DIRS:as/:/ /})
endif
set nonomatch
foreach xdgdir (/home/software/progs/xdg)
    if ( -d "$xdgdir" ) then
        set -l XDG_CONFIG_DIRS=($XDG_CONFIG_DIRS $xdgdir)
    endif
end
unset nonomatch

set    xdgdir="${XDG_CONFIG_DIRS:q}"
unset  XDG_CONFIG_DIRS
setenv XDG_CONFIG_DIRS "${xdgdir:as/ /:/}"
unset  xdgdir

# could be more paranoid, and not accept any previously defined XDG_CACHE_HOME
if ( -z "${XDG_CACHE_HOME}" ) then
  setenv XDG_CACHE_HOME "/var/tmp/xdgcache-${USER}"
endif

if ( -d "${XDG_CACHE_HOME}" ) then
  # verify existing dir is suitable
  if ( ! `test -G "${XDG_CACHE_HOME}" -a -w "${XDG_CACHE_HOME}"` ) then
    # else, make a new/secure one with mktemp
    setenv XDG_CACHE_HOME "$(mktemp -d ${XDG_CACHE_HOME}-XXXXXX)"
  endif
else
  mkdir -p "${XDG_CACHE_HOME}"
endif
