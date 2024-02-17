CXXFLAGS = -O3 -static -std=c++20

r3c: r3clib.cpp r3c.cpp
	g++ $(CXXFLAGS) -o $@ $^

clean:
	rm -f r3c
	rm -rf __pycache__
