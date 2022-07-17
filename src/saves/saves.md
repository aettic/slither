# Saves

### Using Saves

In order for the save / load function to work, the slither/src/saves/ folder must exist (otherwise there is nowhere for the game to write to). This file exists to ensure that the saves folder will exist. If you have no game saves (for instance, if it's your first time playing), you can save from the Player Menu in game. If you try to load without one, it will start a new game anyway.

At this stage in the game, saves are really just json files. Yes, there are better ways to do this, especially if this game were to have some kind of commercial release; however, since it's more of a proof of concept, and a labor of love, I've decided to use what I already have learned, and keep it simple. Using json has also allowed me to conceptualize what the player character is at any moment using key value pairs and variables.

If for some reason your save file is corrupted, you can try to fix it manually (by adjusting the json) or you can simply delete it and start a new game. There are certainly ways one could "cheat" using this save system, but personally I feel like the fun of the game is in playing it and exploring the story, and it's the responsibility of the player to gracefully handle their own enjoyment of the game (and that goes for any game, many of which can be exploited, it doesn't mean they should, or that it enhances the experience.
