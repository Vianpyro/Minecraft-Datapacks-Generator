# [Minecraft](https://www.minecraft.net/download)-[Datapacks](https://minecraft.gamepedia.com/Data_Pack)-Generator ([M](https://www.minecraft.net/download)[D](https://minecraft.gamepedia.com/Data_Pack)G)

## How to use?

* First of all make sure you have [Python](https://www.python.org/downloads/) **3** or more recent installed on your computer.
* Create a new empty [Python](https://www.python.org/downloads/) file.
* Import the MDG library in your new [Python](https://www.python.org/downloads/) file.
* Create and compile your own datapack.
* Type `/reload` to load the datapack.
* Have fun playing with your brand new handmade datapack!

## Example

```py
from MDG import *

datapack = Datapack('t', 't', '6')
workspace = Workspace('mysuperworkspace')
file = File('mysuperfile')
file.set_content(['say this is a super say !'])
workspace.add_file(file)
datapack.add_workspace(workspace)
datapack.build('D:\.minecraft\saves\datapack mc\datapacks', True)
```

* In this example, I start by importing the MDG library, this line is **required** for the datapack to be generated!!
* I created an datapack object with : his name, his description and his [Minecraft](https://www.minecraft.net/download) version
* after, I added an workspace object, this is where the files will be generated :

    ![IMG](img/workspace.png)

* after, to write commands and to launch them I created a file object, in file explorer it's this :

    ![IMG](img/file.png)

* to write some commands in this file, I added in the file object the set_content function, like his name you can set the content of your file with, to give our commands to add give to the method an list of str and their str are the commands added in the file
* and finally I build the datapack with the path to were to export the datapack and if I delete the dir with the same name
* The author is : [Vianpyro](https://github.com/Vianpyro) and [Theskyblockman](https://github.com/theskyblockman).
* If you need some help to learn mcfunction and you are french go see the Silvathor's youtube channel
