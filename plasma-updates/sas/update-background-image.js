var desktop = desktops();
desktop.forEach(function(d,i,dar)
{
    d.currentConfigGroup = new Array("Wallpaper","ord.kde.image","General");
    d.writeConfig("Image","file:///usr/share/wallpapers/SAS_Chalk/contents/images/1280x1024.jpg");
    d.reloadConfig();
});
