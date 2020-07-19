var panel = panels();
panel.forEach(function(p,i,par)
{
    var widget = p.widgets();
    widget.forEach(function(w,ii,war)
    {
        if( w.type == "org.kde.plasma.digitalclock" )
        {
            w.currentConfigGroup = new Array("Configuration","Appearance");
            w.writeConfig("showDate","true");
            w.reloadConfig();
        }
    });
});
