import os
from guitarReptile import Reptile
from getpictureurl import Reptile1
# rep = Reptile("http://www.qupu123.com/hechang","合唱",296)
# rep.builddriver()
# rep.getPageItems()
# rep.destroy()

rep1 = Reptile1("http://www.qupu123.com/minge/1.html")
rep1.builddriver()
rep1.getPageItems()
rep1.destroy()
