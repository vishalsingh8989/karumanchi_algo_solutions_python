#include<stdio.h>
#include <stdlib.h> 

void hanoi(long numofdisk, int startpeg, int auxpeg, int endpeg){



	if(numofdisk){

	            hanoi(numofdisk-1, startpeg, endpeg, auxpeg);
		  //#printf("Move %d  disk from %d to %d\n" numofdisk, startpeg, endpeg))
	            hanoi(numofdisk-1, auxpeg, startpeg, endpeg);


	}
}





int main(int argc, char **argv){

	if(argc != 2){
		printf("Args error\n");
		return 0;
	}
	long x = strtol(argv[1],NULL, 10);
	hanoi(x,1,2,3);
	printf("**********Done*********");

	return 0;
}

