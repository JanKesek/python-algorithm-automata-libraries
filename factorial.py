from multiprocessing import Process, Queue

def silnia(n):
	if (n.get()==1): return 1
	else:
		return n.get()*silnia(n.get()-1)
			

if __name__ == '__main__':
    q = Queue()
	q.put(5)
	p = Process(target=silnia, args=(q,))
    p.start()
    print q.get()    # prints "[42, None, 'hello']"
    p.join()