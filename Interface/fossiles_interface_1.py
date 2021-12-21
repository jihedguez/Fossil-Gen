import maya.cmds as cmds

window = cmds.window(title="Générateur de fossiles", backgroundColor=(1.0, 0.956, 0.901), widthHeight=(200, 140))
cmds.rowColumnLayout(width=470, nc=4, cal=[(1,"center"), (2,"center"), (3,"center"), (4,"center")], cw=[(1,150), (2,100), (3,100), (4,100)])
cmds.text(label='Environnement')
cmds.iconTextRadioCollection()
cmds.iconTextRadioButton( st='iconAndTextVertical', i1='D:\Python\Projet_final\iceberg.png', l='polaire', highlightColor=(0.294, 0.219, 0.196),h=100, onCommand=('cmds.deleteUI(\"'+window+'\", window=True)'))

cmds.iconTextRadioButton( st='iconAndTextVertical', i1='D:\Python\Projet_final\midland.png', l='continental', highlightColor=(0.521, 0.266, 0.258),h=10,w=50, onCommand=('cmds.deleteUI(\"'+window+'\", window=True)'))

cmds.iconTextRadioButton( st='iconAndTextVertical', i1='D:\Python\Projet_final\ghaba.png', l='tropical', highlightColor=(0.745, 0.607, 0.482),h=10,w=50, onCommand=('cmds.deleteUI(\"'+window+'\", window=True)'))



cmds.rowColumnLayout(width=450, nc=2, cal=[(1,"center"), (2,"center")], cw=[(1,150), (2,300)])

cmds.text(label='Epoque')
cmds.intSlider(max=4,min=2, value=3, step=1,bgc=(0.222,0.856,0.150))


cmds.rowColumnLayout(width=470, nc=4, cal=[(1,"center"), (2,"center"), (3,"center"), (4,"center")], cw=[(1,150), (2,100), (3,100), (4,100)])
cmds.text(label='Espèce')
cmds.iconTextRadioCollection()
cmds.iconTextRadioButton( st='iconAndTextVertical', i1='D:\Python\Projet_final\petit.png', l='petit', highlightColor=(0.788, 0.509, 0.462), h=100,w=50, onCommand=('cmds.deleteUI(\"'+window+'\", window=True)'))
cmds.iconTextRadioButton( st='iconAndTextVertical', i1='D:\Python\Projet_final\moyen.png', l='moyen', highlightColor=(0.235, 0.184, 0.184), h=100,w=50, onCommand=('cmds.deleteUI(\"'+window+'\", window=True)'))
cmds.iconTextRadioButton( st='iconAndTextVertical', i1='D:\Python\Projet_final\grand.png', l='grand', highlightColor=(0.925, 0.467, 0.047),h=100,w=50, onCommand=('cmds.deleteUI(\"'+window+'\", window=True)'))





cmds.showWindow(window)