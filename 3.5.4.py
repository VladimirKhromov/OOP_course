class Track:

	def __init__(self, start_x, start_y):
		self.start_x = start_x
		self.start_y = start_y
		self.all_track = [TrackLine(start_x,start_y,0)]


	def add_track(self, tr):
		if isinstance(tr,TrackLine):
			self.all_track.append(tr)

	def get_tracks(self):
		return tuple(self.all_track)



	def get_tracks_coord(self):
		result = [object.get_coords() for object in self.all_track]
		return result

	def __len__(self):
		result = 0
		tracks = self.get_tracks_coord()
		for i in range(len(self.all_track)-1):
			x1 = tracks[i][0]
			x2 = tracks[i+1][0]
			y1 = tracks[i][1]
			y2 = tracks[i+1][1]
			result += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
			
		return int(result)


	def __eq__(self, other):
		return len(self) == len(other)

	def __lt__(self, other):
		return len(self) < len(other)


class TrackLine:
	def __init__(self, to_x, to_y, max_speed):
		self.to_x = to_x
		self.to_y = to_y
		self.max_speed = max_speed

	def get_coords(self):
		return self.to_x, self.to_y


track1 = Track(0,0)
trackLine11 = TrackLine(2,4,100)
trackLine12 = TrackLine(5,-4,100)
track1.add_track(trackLine11)
track1.add_track(trackLine12)

track2 = Track(0,1)
trackLine21 = TrackLine(3,2,90)
trackLine22 = TrackLine(10,8,90)
track2.add_track(trackLine21)
track2.add_track(trackLine22)


res_eq = track1 == track2

