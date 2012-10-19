from music21 import *
import os

def generateMatrix(bound):
	return [ [ 0.0 for i in range(bound) ] for j in range(bound)]

def getBounds(lst):
	return len(list(set(lst)) #not order preserving, but we don't care here.. 

def getNoteMap(lst):
	noteMap = {}
	y=0
	for x in sorted(list(set(lst))):
		noteMap[x] = y
		y+=1
	return noteMap


def getTransitions(notelist,transitionMatrix,NoteMapping):
	itr = iter(notelist)
	try:
		while True:
			a = itr.next()
			aid = NoteMapping[a.nameWithOctave]

			b = itr.next()
			bid = NoteMapping[b.nameWithOctave]

			print a.nameWithOctave, aid
			print b.nameWithOctave, bid

			transitionMatrix[aid][bid] += 1

	except:
		pass
#foo
	return transitionMatrix

def getTransitionSum(transitionMatrix):
	total = 0
	for x in range(len(transitionMatrix)):
		for y in range(len(transitionMatrix[x])):
			total += transitionMatrix[x][y]
	return total

def getTransitionFrequency(transitionMatrix,transitionMatrixSum):
	bounds = len(transitionMatrix)
	freqTable = generateMatrix(bounds)
	for x in range(len(transitionMatrix)):
		for y in range(len(transitionMatrix[x])):
			freqTable[x][y] = transitionMatrix[x][y]/transitionMatrixSum * 1.0
	return freqTable

def pm(matrix):
	for row in matrix:
		print row

def pmi(matrix,NoteMapping):
	print NoteMapping
	for row in matrix:
		print row



if __name__ == "__main__":
	fp = os.path.join('in','derezzed.midi')
	mf = midi.MidiFile()
	mf.open(fp)
	mf.read()
	mf.close()
	print len(mf.tracks)
	s = midi.translate.midiFileToStream(mf)
	p1 = s.parts[0]
	p1n = p1.flat.elements
	notes_in_order = []
	for n in p1n:
		try:
			if n.isNote:
				notes_in_order.append(n)
		except:
			pass

	TransitionCountMatrix = generateMatrix(getBounds(notes_in_order))
	pm(TransitionCountMatrix)

	NoteMapping = getNoteMap(notes_in_order)
	print NoteMapping


	tmpTransitionsMatrix = getTransitions(notes_in_order,TransitionCountMatrix,NoteMapping)
	pm(tmpTransitionsMatrix)

	TransitionFrequencies = getTransitionFrequency(tmpTransitionsMatrix,getTransitionSum(tmpTransitionsMatrix))

	pmi(TransitionFrequencies)

