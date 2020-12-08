# audio_button

This is code intended to run on a raspberry pi, originally written on a raspberry pi 4 but it would run on any model with some minor tweaking. 

My work is exhibition design and fabrication and audio is something that plagues exhibit designers the world over (I assume).
  Do you use headphones?
  What about audio tours?
  Can the sound just play?
  What if it is annoying?
  What if the installation isn't in a museum or place where people will tolerate an audio loop playing forever?
  Why are some commercial solutions so expensive?

The specific problem I was trying to solve was three-fold:
  1) Avoid using headphones for exhibit installations that use sound (gross) 
  2) Do not play sound continuously while the installation is up
  3) Share sound in exhibits as easily as possible

So, I thought why not a button that you press which then unmutes the sound on whatever is playing for certain amount of time?

I did some searching and thanks to firum user named paddyg I found the solution I was looking for. 

https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=222763&p=1644293&hilit=alsamixer+volume+control+via+gpio#p1644293

Code is commented for ease of customization.

Final note, this solution is for unmuting and muting the sound on a video that is playing over and over.

If you want visitors to simply press a button and hear a sound far simpler solutions exist, and can run on AA batteries. 

https://www.adafruit.com/product/2133
