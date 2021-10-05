# Virtual Painter using OpenCV
Using openCV and following this ![This tutorial](https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=97s) i built a virtual painter

I made a few changes and this implementation only detects green and black. Other colors can be easily added.

**Ideas Incoporated**
a. The openCV trackbar class was used to detect the HSV range of the of each pen color.
b. Then we used the findContour() function to locate the pen edges after they've been converted to HSV (FONT_BGR2HSV) and masked using the inRange() function.
c. openCV's circle function and some basic python logics did the rest.



https://user-images.githubusercontent.com/63596779/136053207-3c9cb03c-db51-4c97-997d-b195b84ad40c.mp4

