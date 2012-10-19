class Colour(object):
	def __init__(self,_r=0,_g=0,_b=0):
		self.R = _r
		self.G = _g
		self.B = _b
	def toHexString(self,val):
		if val > 0:
			return hex(val)[2:4]
		else:
			return "00"
	def toHex(self):
		redComponent = self.toHexString(self.R) #hex(self.R)[2:4]
		greenComponent = self.toHexString(self.G)  #hex(self.G)[2:4]
		blueComponent = self.toHexString(self.B) #hex(self.B)[2:4]
		return "#%s%s%s" % (redComponent,greenComponent,blueComponent)

	def Lerp(self,start,end,amount):
		difference = end - start
		adjusted = difference * amount
		return start+adjusted;

	def colourLerp(self,toColour,amount):
		if amount > 254:
			return self
		sr = self.R
		sg = self.G
		sb = self.B
		
		er = toColour.R
		eg = toColour.G
		eb = toColour.B
		
		nr = self.Lerp(sr,er,amount)
		ng = self.Lerp(sg,eg,amount)
		nb = self.Lerp(sb,eb,amount)
		
		return Colour(nr,ng,nb)

	def __repr__(self):
		return self.toHex()		


if __name__ == "__main__":
	x = Colour(255,0,0) # red
	print x.toHex() # should print #ff0000
	white = Colour(255,255,255)
	pink = x.colourLerp(white,40)
	for i in range(0,255,10):
		shade = x.colourLerp(white,i)
		print shade.toHex()
