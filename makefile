resultado.png : eje17.dat eje17.py eje15.py eje16.py
	python eje17.py eje15.py eje16.py
eje17.dat : eje17.x
	./eje17.x
eje17.x: eje17.cpp
	c++ eje17.cpp -o eje17.x