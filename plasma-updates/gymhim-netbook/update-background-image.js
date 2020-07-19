var desktop = desktops();
desktop.forEach(function(d,i,dar)
{
    d.currentConfigGroup = new Array("Wallpaper","ord.kde.image","General");
    d.writeConfig("Image","file:///usr/share/wallpapers/logo_gymhim_wallpaper_netbook.png");
    d.reloadConfig();
});
