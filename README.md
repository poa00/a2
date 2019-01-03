# a2 [![Codacy Badge](https://api.codacy.com/project/badge/Grade/0bc56698a44144e68ff191105f97215d)](https://app.codacy.com/app/ewerybody/a2?utm_source=github.com&utm_medium=referral&utm_content=ewerybody/a2&utm_campaign=badger) [![Join the chat at https://gitter.im/ewerybody/a2](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/ewerybody/a2?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Script managing and developing framework for [Autohotkey](http://ahkscript.org/) with [PySide](https://wiki.qt.io/PySide) (Python/Qt) frontend.<br>
See [wiki](https://github.com/ewerybody/a2/wiki) for more information especially the page about [setting you up](https://github.com/ewerybody/a2/wiki/setting-you-up).

## news:
* **PySide2 ✔**!! And **Python 3.6.5 ✔**!! Whow! The [first release project](https://github.com/ewerybody/a2/projects/1) is coming closer! We also reached > **1000 commits** already and on [4. of July](https://github.com/ewerybody/a2/commit/71031e49299a2e1189a30405380581b02c28c5c9) **a2 will turn 5** on github! 
* **Hotkey widgets** now show the scope right away and users can edit if they desire. Some shots in the [gallery](http://imgur.com/a/fkD8u)
* Package **download** and **update** checker threads are implemented!! 🎊 yay 🥂 This is quite a big deal for this project.
* Quite some stuff: **New Element Dialog** can now add to local module or globally and enlist in the display list.
 **Unicode HotStrings** start to work a bit. Keep crossing fingers! **New Label element**. I added some stuff to the [gallery](http://imgur.com/a/fkD8u)
* **animated gifs ftw!** I created a [gallery on imgur](http://imgur.com/a/fkD8u) to make latest changes a little more visual. Something between a video and just writing a proper commit msg. I know I need to make videos! Please be patient! :]
* **package building** :package: works now! Using [PyInstaller](https://github.com/pyinstaller/pyinstaller) and some batch and py scripting we can now build self-containing a2 packages with no further dependencies. To do that of course there is now one more dependency: `pip install PyInstaller`. [The milestone](https://github.com/ewerybody/a2/milestones/alpha%20preview) is coming closer!!
* since there is no option for a default issue view [**backlog**](https://github.com/ewerybody/a2/issues?q=label%3Abacklog) and [**wontfix**](https://github.com/ewerybody/a2/issues?q=label%3Awontfix) issues have been "closed" for better overview (and looking like there is less todo). They are still there! That's why I put the links. When such an issue is tackled it will be opened again. When closed the wontfix or backlog label will be removed.
* **a2/a2.modules separation complete!** There are still a lot of features to add but the main functionality is implemented: One can have multiple module sources and enable/disable them individually. You see there is a lot less [Autohotkey code here](https://github.com/ewerybody/a2/search?l=autohotkey) now. See [the **a2.modules** project](https://github.com/ewerybody/a2.modules) for the standard ones. 

## a2 main loop layout:
![](https://i.imgur.com/zyv1mUb.gif)

## blog posts:
* [a2 – the first humble steps](http://goodsoul.de/?p=780)

## <a name="dev-team"></a>Authors/Contributors  
* [Eric Werner (ewerybody)](https://github.com/ewerybody)
* [Oliver Lipkau](https://github.com/lipkau)
