

int distanceBetweenBusStops(int* distance, int distanceSize, int start, int destination){
    if (start>destination){
        int temp=start;
        start=destination;
        destination=temp;
    }
    int total=0;
    for (int i=0;i<distanceSize;i++){
        total+=distance[i];
    }
    int a=0;
    for (int i=start;i<destination;i++){
        a+=distance[i];
    }
    int b=total-a;
    if (a>b){
        return b;
    }
    else{
        return a;
    }
}