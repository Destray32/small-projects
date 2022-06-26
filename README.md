# Repository with collection of my small projects in various PLs.


## discord-bot
> Small bot with few functions. Uncommented code is used for downloading and sending .mp4 file for discord chats so you doesn't need to open
> youtube to watch it.
> The other, commented section was designed for tracking down planes that were flying in specified area. Area can be changed with custom points on line 78.
```python
states = api_c.get_states(bbox=(49.596470, 49.875168, 20.405045, 20.849991))
```
> as well as country origin of planes that you want to track in area on line 87
```python
if (str(s.origin_country) == "United States"):
```

## transparent-crosshair
> Small C# program designed to show square in the middle of screen.
> Square is transparent so you can't click it by mistake and unfocus from game window.
> Color of crosshair is customizable on program tray icon.
> Compile source code with and you should be good to go.
