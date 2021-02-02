int GCD(int a, int b){
    if (b == 0) { 
        return a;
    }
    else {
        return GCD(b, a%b);
    }
}
int LCM(int a, int b){
    int g = GCD(a,b);
    return g * (a/g) * (b/g);
}


