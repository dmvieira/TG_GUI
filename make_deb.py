from py2deb import Py2deb

from glob import glob

version="0.4"

p=Py2deb("tggui")
p.author="Diogo"
p.mail="diogo.mvieira@gmail.com"
p.description=u"Program to create backgrounds wallpapers that change with time."
p.depends="gconf2, python"
p.license="gpl"
p.section="utils"
p.arch="all"

p["/usr/share/applications"]=["tggui.desktop|tggui.desktop"]
p["/usr/bin"]=["source.py|tggui"]
p["/usr/share/icons/hicolor/48x48/apps"]=["tggui.png|tggui.png"]
p.generate(version,rpm=True,src=True)
