import sys, traceback
from operator import itemgetter

def main(): 
	lines = [str.split() for str in sys.stdin.readlines()]
	try: 
		num_songs = int(lines[0][0])
		num_to_choose = int(lines[0][1])
		if len(lines) < num_songs+1: 
			print "Error: There must be ", num_songs, " lines of song input."
			return
		zipf(num_songs, num_to_choose, lines[1:num_songs+1])
	except:
		print "Invalid input - first line should be in format: "
		print "<n> <m>"
		print "where n and m are both integers"
		traceback.print_exc()

def zipf(num_songs, num_to_choose, lines): 
	try: 
		num_first_song_listens = int(lines[0][0])
		qualities = []

		for i in range(0, len(lines)): 
			qualities.append((lines[i][1], get_quality(lines[i], num_first_song_listens, i)))
		
		sorted_qualities = [x for x in reversed(sorted(qualities, key=itemgetter(1,0)))]

		for i in range(0, num_to_choose): 
			print sorted_qualities[i][0]

	except:
		print "Each line after the first should have the format: "
		print "<integer> <string>"
		print "integer - represents the number of times a song is listened to"
		print "string - the name of the song"
		traceback.print_exc()


def get_quality(line, num_first_song_listens, index): 
	num_expected_listens = num_first_song_listens / (index+1)
	num_real_listens = line[0]
	if num_expected_listens == 0: 
		return 0
	return float(num_real_listens) / float(num_expected_listens)

if __name__ == "__main__": 
	main()