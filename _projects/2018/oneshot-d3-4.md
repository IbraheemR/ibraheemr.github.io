---
title: OneShot - Devlog Day 3 & 4

date: 2018-07-28 -
image: /assets/p/2018/oneshot/oneshot-ui.png
---

I've spent these days implementing the features/fixes I described in my [last post](/blog/oneshot-d1-2/), and I'm probably ready to submit the game at this point.

The first fix I tackled was the issue with the comms UI element, where the previous message would redo it's typing animation before the next one was animated. Turns out this was caused by a single line of code I had forgotten to delete. Originally, there was only one vaiable to store the message to be displayed, meaning a new message would override the new one even if it's entry 'typing' animation had not finished. I replaced the single vaiabe with an array; the first element would be typed, and after it had finished, if there were other messages waiting, it would be `shift()`ed from the front and the next one would take it's place and be typed. I had forgotten to remove the call to restart the animation for the new message from my old approach, so now upon recieving a message the animation would be played (causing the old message to reshow), then the new message would be loaded and moved to ther front, and then played for the seconds (and correct time). Despite all this this took me over an hour (or even two) to find, since my socket events and event handlers are in different parts of the file. That's debugging for you kids!

Aside from a tackling a few other bugs, I also had an issue with physics, the ship would fly in an unweildly manner. My approach to the physics was this (I'll probably have a more in depth explanation of my approach to simple physics soon):

1. Update `x`, `y` and heading (`a` for angle) based on velocity (`dx` & `dy`) and angular velocity (`da`)
2. Apply drag to `dx`, `dy`, & `da`
3. If the user is pressing keys, calculate the increment to `dx`, `dy` & `da`

Due to the mental gymnastics I'm having to do to comprehend this, I'm not quite sure what the exact issue was, but somehow I realised I could fix this storing dx as forward movement, as apposed to movement along the x axis and the same for `y`, and then apply that to `x` based on `cos(dx) + sin(dy)` and y based on `sin(dx) + cos(dy)`. Perhaps one day I'll manage to wrap my head around this and have a better explanation.

I also added a few conditional clauses to only render entities if off screen, reducing load on the render engine, and added a circular radar to point you in the direction of other ships within 'the sector' (i.e the game area).

![](/assets/p/2018/oneshot/oneshot-radar.png)  
_Arrows incicate players and circles indicate recharge powerups_

I also added recharge powerups, so you could replenish your one shot if you use it. I hope this will create a draw for other players, perhaps creating a zone of conflict or somewhere to wait for other players to kill. Also on the theme of making gamplay better I added a suicide button -`[X]`- if you so wish as to terminate your time in the sector quickly - useful if you cannot find a recharge for your shot.

I also created some sounds, and using the sound library for [p5.js](https://p5js.org), implemented some effects for the comms system, shooting, death and opening/closing the flight guide. This nicely ties the game to a point where I can call it finished, although there may be some more tweaks to add.

So, without further ado, play it [here](https://oneshot--ibraheemrodrigues.repl.co/)