def main():
	fp="input.txt"
	with open(fp) as f:
		m_names=f.readline().split()
		w_names=f.readline().split()
		n=len(m_names)
		m_free=list(range(n))
		wife=[-1 for i in range(n)]
		husband=[-1 for i in range(n)]
		m_pref=[[] for i in range(n)]
		w_pref=[[-1 for i in range(n)] for j in range(n)]
		
		for i in range(n):
			l=f.readline().split()
			m_index=m_names.index(l[0])
			for j in l[1:]:
				#print(w_names.index(j))
				m_pref[m_index].append(w_names.index(j))

		for i in range(n):
			l=f.readline().split()
			w_index=w_names.index(l[0])
			priority=1
			for j in l[1:]:
				w_pref[w_index][m_names.index(j)]=priority
				priority+=1
		
		pcount=[0 for i in range(n)]
		
		while m_free != []:
			m=m_free[0]
			if pcount[m]!=n:
				w=m_pref[m][pcount[m]]
				if husband[w] is -1:
					husband[w]=m
					wife[m]=w
					m_free.pop(0)
				elif w_pref[w][husband[w]]>w_pref[w][m]:
					m_free.append(husband[w])
					print("Woman",w,"changed from",husband[w],"to",m)
					wife[husband[w]]=-1
					husband[w]=m
					wife[m]=w
					m_free.pop(0)
				pcount[m]+=1
		print("----------------OUTPUT-----------------")
		for i in range(n):
			print('\t'+w_names[wife[i]],' Weds ',m_names[husband[wife[i]]])
		print("---------------------------------------")		

if __name__=='__main__':
	main()