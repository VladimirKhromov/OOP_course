class SoftList(list):

	def __getitem__(self, indx):
		try:
			res = super().__getitem__(indx)
		except:
			res = False

		return res

sl = SoftList("python")
a1 = sl[0] # 'p'
a2 = sl[-1] # 'n'
a3 = sl[6] # False
a4 = sl[-7] # False

print(a1, a2, a3, a4)