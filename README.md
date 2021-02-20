# [Minecraft](https://www.minecraft.net/download)-[Datapacks](https://minecraft.gamepedia.com/Data_Pack)-Generator

## How to use?

* First of all make sure you have [Python](https://www.python.org/downloads/) **3.9.0** or above installed on your computer.
* Download this repository in the folder where the datapack should be generated.
* Create a new empty [Python](https://www.python.org/downloads/) file.
* Import the library in your new [Python](https://www.python.org/downloads/) file.
* Create and compile your own datapack.
* Once the datapack is generated, paste it in the *datapacks* folder of your [Minecraft](https://www.minecraft.net/download) world.
* Type `/reload` to load the datapack.
* Have fun playing with your brand new handmade datapack!

### Example

```py
from datapackmc import *

datapack = Datapack('my super datapack', 'hey this is the description of my super datapack!', '6')
workspace = Workspace('mysuperworkspace')
function = Function('mysuperfunction', workspace)
function.set_content(['# warning it is a super code so don\'t copy it!'
                      'execute run execute run say hey!'])
datapack.build('.minecraft/saves/mysuperworld', [function])
```

* In this example, I start by importing the wmcpy "library", this line is ***required*** for the datapack to be generated!!
* I also create a variable containing the name of my datapack because I want to be able to change it in every file I mention it.
* Then I create another variable containing an instance of the class "Datapack" to start the creation of my datapack.
* The title is the name of the datapack I'll paste in the *datapacks* folder of my [Minecraft](https://www.minecraft.net/download) world.
* The author is me, [Vianpyro](https://github.com/Vianpyro).
* The pack_meta is the informations I'll set in the *pack.mcmeta* file, this file is very important; it allows [Minecraft](https://www.minecraft.net/download) to read your datapack.
* As you can see I use 2 *reserved* names: ***main*** - containing the functions I want to repeat every [Minecraft](https://www.minecraft.net/download) tick - and ***load*** - once when the datapack is reloaded.
* Then I write whatever I want to be in my datapack ; one advancement, 4 functions and a predicate.
* I know that the new version of my datapack is better than the older so I want to replace it without being asked when I run the program.
* I also add another function - **main** - after the initialisation of my datapack because I want to be able to change it whenever I want without having to search for it in the big block of code above.
* Once I'm sure I don't have anything to add to my datapack I compile it.
* At last, when the datapack is successfuly generated I just paste it into my [Minecraft](https://www.minecraft.net/download) world to enjoy the features I added.
