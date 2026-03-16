compile-c:
	gcc -shared -fPIC -o lib/libcore.so core/src/*.c