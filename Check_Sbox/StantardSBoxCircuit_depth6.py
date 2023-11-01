def StantardSBox(u):
	t = list()
	m = list()
	l = list()
	s = list()
	for i in range(100):
		t.append(0)
		m.append(0)
		l.append(0)
	for i in range(8):
		s.append(0)
	t[0] = u[7] ^ u[4]
	t[1] = u[7] ^ u[2]
	t[2] = u[7] ^ u[1]
	t[3] = u[4] ^ u[2]
	t[4] = u[3] ^ u[1]
	t[5] = t[0] ^ t[4]
	t[6] = u[6] ^ u[5]
	t[7] = u[0] ^ t[5]
	t[8] = u[0] ^ t[6]
	t[9] = t[5] ^ t[6]
	t[10] = u[6] ^ u[2]
	t[11] = u[5] ^ u[2]
	t[12] = t[2] ^ t[3]
	t[13] = t[5] ^ t[10]
	t[14] = t[4] ^ t[10]
	t[15] = t[4] ^ t[11]
	t[16] = t[8] ^ t[15]
	t[17] = u[4] ^ u[0]
	t[18] = t[6] ^ t[17]
	t[19] = t[0] ^ t[18]
	t[20] = u[1] ^ u[0]
	t[21] = t[6] ^ t[20]
	t[22] = t[1] ^ t[21]
	t[23] = t[1] ^ t[9]
	t[24] = t[19] ^ t[16]
	t[25] = t[2] ^ t[15]
	t[26] = t[0] ^ t[11]
	m[0] = (t[12] & t[5]) ^ m[0]
	m[1] = (t[22] & t[7]) ^ m[1]
	m[2] = t[13] ^ m[0]
	m[3] = (t[18] & u[0]) ^ m[3]
	m[4] = m[3] ^ m[0]
	m[5] = (t[2] & t[15]) ^ m[5]
	m[6] = (t[21] & t[8]) ^ m[6]
	m[7] = t[25] ^ m[5]
	m[8] = (t[19] & t[16]) ^ m[8]
	m[9] = m[8] ^ m[5]
	m[10] = (t[0] & t[14]) ^ m[10]
	m[11] = (t[3] & t[26]) ^ m[11]
	m[12] = m[11] ^ m[10]
	m[13] = (t[1] & t[9]) ^ m[13]
	m[14] = m[13] ^ m[10]
	m[15] = m[2] ^ m[1]
	m[16] = m[4] ^ t[23]
	m[17] = m[7] ^ m[6]
	m[18] = m[9] ^ m[14]
	m[19] = m[15] ^ m[12]
	m[20] = m[16] ^ m[14]
	m[21] = m[17] ^ m[12]
	m[22] = m[18] ^ t[24]
	m[23] = m[21] ^ m[22]
	m[24] = (m[21] & m[19]) ^ m[24]
	m[25] = m[20] ^ m[24]
	m[26] = m[19] ^ m[20]
	m[27] = m[22] ^ m[24]
	m[28] = (m[27] & m[26]) ^ m[28]
	m[29] = (m[25] & m[23]) ^ m[29]
	m[30] = (m[19] & m[22]) ^ m[30]
	m[31] = (m[26] & m[30]) ^ m[31]
	m[32] = m[26] ^ m[24]
	m[33] = (m[20] & m[21]) ^ m[33]
	m[34] = (m[23] & m[33]) ^ m[34]
	m[35] = m[23] ^ m[24]
	m[36] = m[20] ^ m[28]
	m[37] = m[31] ^ m[32]
	m[38] = m[22] ^ m[29]
	m[39] = m[34] ^ m[35]
	m[40] = m[37] ^ m[39]
	m[41] = m[36] ^ m[38]
	m[42] = m[36] ^ m[37]
	m[43] = m[38] ^ m[39]
	m[44] = m[41] ^ m[40]
	m[45] = (m[43] & t[5]) ^ m[45]
	m[46] = (m[39] & t[7]) ^ m[46]
	m[47] = (m[38] & u[0]) ^ m[47]
	m[48] = (m[42] & t[15]) ^ m[48]
	m[49] = (m[37] & t[8]) ^ m[49]
	m[50] = (m[36] & t[16]) ^ m[50]
	m[51] = (m[41] & t[14]) ^ m[51]
	m[52] = (m[44] & t[26]) ^ m[52]
	m[53] = (m[40] & t[9]) ^ m[53]
	m[54] = (m[43] & t[12]) ^ m[54]
	m[55] = (m[39] & t[22]) ^ m[55]
	m[56] = (m[38] & t[18]) ^ m[56]
	m[57] = (m[42] & t[2]) ^ m[57]
	m[58] = (m[37] & t[21]) ^ m[58]
	m[59] = (m[36] & t[19]) ^ m[59]
	m[60] = (m[41] & t[0]) ^ m[60]
	m[61] = (m[44] & t[3]) ^ m[61]
	m[62] = (m[40] & t[1]) ^ m[62]
	l[0] = m[60] ^ m[61]
	l[1] = m[49] ^ m[55]
	l[2] = m[45] ^ m[47]
	l[3] = m[46] ^ m[54]
	l[4] = m[53] ^ m[57]
	l[5] = m[48] ^ m[60]
	l[6] = m[61] ^ l[5]
	l[7] = m[45] ^ l[3]
	l[8] = m[50] ^ m[58]
	l[9] = m[51] ^ m[52]
	l[10] = m[52] ^ l[4]
	l[11] = m[59] ^ l[2]
	l[12] = m[47] ^ m[50]
	l[13] = m[49] ^ l[0]
	l[14] = m[51] ^ m[60]
	l[15] = m[54] ^ l[1]
	l[16] = m[55] ^ l[0]
	l[17] = m[56] ^ l[1]
	l[18] = m[57] ^ l[8]
	l[19] = m[62] ^ l[4]
	l[20] = l[0] ^ l[1]
	l[21] = l[1] ^ l[7]
	l[22] = l[3] ^ l[12]
	l[23] = l[18] ^ l[2]
	l[24] = l[15] ^ l[9]
	l[25] = l[6] ^ l[10]
	l[26] = l[7] ^ l[9]
	l[27] = l[8] ^ l[10]
	l[28] = l[11] ^ l[14]
	l[29] = l[11] ^ l[17]
	s[7] = l[6] ^ l[24]
	s[6] = l[16] ^ l[26]
	s[5] = l[19] ^ l[28]
	s[6] = 1 ^ s[6]
	s[5] = 1 ^ s[5]
	s[4] = l[6] ^ l[21]
	s[3] = l[20] ^ l[22]
	s[2] = l[25] ^ l[29]
	s[1] = l[13] ^ l[27]
	s[0] = l[6] ^ l[23]
	s[1] = 1 ^ s[1]
	s[0] = 1 ^ s[0]

	return s
