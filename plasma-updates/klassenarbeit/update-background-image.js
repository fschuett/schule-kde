var desktop = desktops();
desktop.forEach(function(d,i,dar)
{
    d.currentConfigGroup = new Array("Wallpaper","ord.kde.image","General");
    d.writeConfig("Image","file:///usr/share/wallpapers/logo_klassenarbeit.png");
    d.reloadConfig();
});
