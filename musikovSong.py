from music21 import *
import os
import sys
import traceback
import pygraphviz as pgv


class MusikovSong(object):

	def __init__(self,SongPath):
		self.SongName = os.path.basename(SongPath).split('.')[0]
		#self.TransitionMatrix [x][a]
		#					   [a][1]
		#self.NoteMapping {A:0, B:1, C:2} etc
		self.filext = "png"
		pass

	def generateMatrix(self):
		return [ [ 0.0 for i in range(self.Bounds) ] for j in range(self.Bounds)]

	def getBounds(self):
		self.Bounds = len(list(set(self.NotesInOrder))) #not order preserving, but we don't care here.. 

	def getNoteMap(self):
		noteMap = {}
		y=0
		for x in sorted(list(set(self.NotesInOrder))):
			noteMap[x] = y
			y+=1
		self.NoteMapping = noteMap
		self.InverseNoteMapping = dict((v,k) for k, v in self.NoteMapping.iteritems())

		#return noteMap


	def generateTransitionCount(self):
		self.getBounds()
		self.TransitionMatrix  = self.generateMatrix()

		itr = iter(self.NotesInOrder)
		try:
			while True:
				a = itr.next()
				aid = self.NoteMapping[a]

				b = itr.next()
				bid = self.NoteMapping[b]

				#print a, aid
				#print b, bid

				self.TransitionMatrix[aid][bid] += 1

		except:
			pass
	#foo
		#self.TransitionMatrix = transitionMatrix
		#return transitionMatrix


	def getTransitionSum(self):
		total = 0
		for x in range(len(self.TransitionMatrix)):
			for y in range(len(self.TransitionMatrix[x])):
				total += self.TransitionMatrix[x][y]
		#return total
		self.TransitionSum = total
		

	def getTransitionFrequency(self):
		freqTable = self.generateMatrix()
		for x in range(len(self.TransitionMatrix)):
			for y in range(len(self.TransitionMatrix[x])):
				try:
					freqTable[x][y] = self.TransitionMatrix[x][y]/self.TransitionSum * 1.0
				except:
					freqTable[x][y] = 0.0
		
		self.TransitionFrequencies = freqTable
		#return freqTable

	@staticmethod
	def pm(matrix):
		for row in matrix:
			print row

	@staticmethod
	def pmi(matrix,NoteMapping):
		print NoteMapping
		for row in matrix:
			print row

	def loadSong(self,filePath):
		self.MidiFile = midi.MidiFile()
		self.MidiFile.open(filePath)
		self.MidiFile.read()
		self.MidiFile.close()
		self.Stream = midi.translate.midiFileToStream(self.MidiFile)
		self.Part0 = self.Stream.parts[0]
		


	def getNotesFromSong(self):
		self.Notes = self.Part0.flat.elements
		notes_in_order = []

		for note in self.Notes:
			try:
				if note.isNote:
					notes_in_order.append(note.nameWithOctave)
			except:
				pass
		self.NotesInOrder = notes_in_order


	def getTracks(self):
		return len(self.MidiFile.tracks)

	def generateGraph(self):
		G = pgv.AGraph()
		G.edge_attr['dir'] = 'forward'
		G.edge_attr['arrowtype'] = 'normal'
		for x in range(len(self.TransitionFrequencies)):
				for y in range(len(self.TransitionFrequencies[x])):
					try:
						if self.TransitionFrequencies[x][y] != 0.0:
							noteA = self.InverseNoteMapping[x] #reverse the mapping, to get the notes
							noteB = self.InverseNoteMapping[y]
							print "%s -> %s (%s)" %(noteA,noteB,self.TransitionFrequencies[x][y])
							G.add_node(noteA)
							G.add_node(noteB)
							G.add_edge(noteA,noteB,label="%0.4f"%self.TransitionFrequencies[x][y])
					except:
						ex, val, tb = sys.exc_info()
						traceback.print_exception(ex, val, tb)
		G.layout(prog='dot')
		G.write("./graphs/%s.dot"%self.SongName)
		G.draw("./graphs/%s.%s"%(self.SongName,self.filext))
		return 0




if __name__ == "__main__":
	derezzed = "in/derezzed.midi"
	fp = sys.argv[1]

	ms = MusikovSong(fp)
	ms.loadSong(fp)
	ms.getNotesFromSong()
	ms.getNoteMap()

	print "Note Mapping"
	print ms.NoteMapping
	

	ms.generateTransitionCount()

	print "Transition Counts"
	ms.pm(ms.TransitionMatrix)
	ms.getTransitionSum()
	ms.getTransitionFrequency()
	print "Transition Sum", ms.TransitionSum

	print "Transition Frequencies"
	ms.pm(ms.TransitionFrequencies)
	ms.generateGraph()

