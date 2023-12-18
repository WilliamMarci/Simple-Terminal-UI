# SimpleTUI
Use python to draw your Terminal UI!

## Class Introduction
- Const
  - `BOX` ordinary box characters
  - `BOLDBOX` bold box characters
  - `CORNER1` corner characters for left-top(light) and right-bottom(bold) 
  - `TICKS` tick characters for chart with bold edge
  - `DASH1` dash characters for chart 
  - `DOUBLE` double line characters for chart
  - `BARHOR` horizontal bar characters
  - `BARVER` vertical bar characters
  - `BLOCK` block characters for graph
  - `SHADOW` shadow effect (sort by light to dark)
  - `POINT` points for scatter
  - `ARROW` arrows
  - `RUNINGCHAR` running characters
  - `DOTS` dots for hex graph 
  - `TPC` transparent character
- subfunctions
  - `emptyContent` return empty list 1D or 2D
  - `zeroContent` return zero list 1D or 2D
  - `linearSpace` return linear space list
  - `floarToPercentStr` retern percent string
- Canvas
  - `convertPositionCanvas` convert position to canvas position
  - `summonRectangular` summon rectangular
  - `rectOnCanvas` draw rectangular on canvas

## Basic class:
-   [x] `UIElement`
-   [x] `TerminalEnv`
-   [ ] `AnimeElement`

## Achieved class:
-   [x] `TypeRender` (need more functions)
-   [x] `CanvasRender`
-   [x] `TextElement`
-   [x] `ProgressBar` (H)
-   [x] `Scatter`
-   [x] `Image`

## Planning class:
-   [ ] `BarChart`
-   [ ] `Circle`
-   [ ] `Clock`
-   [ ] `RunningChar`
-   [ ] `Card`
-   [ ] `Table`
-   [ ] `Tree`

## Const
```python
#the basic element of terminal UI
BOX=['─','│','┌','┐','└','┘','├','┤','┬','┴','┼']   #Ordinary Box
BOLDBOX=['━','┃','┏','┓','┗','┛','┣','┫','┳','┻','╋'] #Bold Box
CORNER1=['┒','┕']   #Corner fot left-up to right-down shadow
TICKS=['┠','┨','┯','┷']      
DASH1=['┄','┅','┆','┇','┈','┉','┊','┋']
DOUBLE=['═','║','╔','╗','╚','╝','╠','╣','╦','╩','╬']
BARHOR=['█','▉','▊','▋','▌','▍','▎','▏']
BARVER=['█','▇','▆','▅','▄','▃','▂','▁']
BLOCK=[' ','▘','▝','▀','▖','▌','▞','▛','▗','▚','▐','▜','▄','▙','▟','█']
#sort by 1-LT 2-RT 3-LD 4-RD and they combine 4 pixel
DOUBLEPIXEL=[' ','▀','▄','█']
SHADOW=[' ','░','▒','▓','█']
POINT=['.','o','O','@','*','+','x','X','#']
ARROW=['←','↑','→','↓','↖','↗','↘','↙']
RUNINGCHAR=['◜','◠','◝','◞','◡','◟','○']
DOTS=['⠀','⠁','⠂','⠃','⠄','⠅','⠆','⠇','⠈','⠉','⠊','⠋','⠌','⠍','⠎','⠏','⠐','⠑','⠒','⠓','⠔','⠕','⠖','⠗','⠘','⠙','⠚','⠛','⠜','⠝','⠞','⠟','⠠','⠡','⠢','⠣','⠤','⠥','⠦','⠧','⠨','⠩','⠪','⠫','⠬','⠭','⠮','⠯','⠰','⠱','⠲','⠳','⠴','⠵','⠶','⠷','⠸','⠹','⠺','⠻','⠼','⠽','⠾','⠿']
TPC=' ' #Transparent Character
``` 
