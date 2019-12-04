#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

void condicion(double *c,double x,double t);
void ej(double *ej, double *c, double delta_t, double delta_x);
void nombre(string filename);	
int main(){
  double delta_t=0.01;
  double delta_x=0.01;
  nombre("eje17.dat");
  return 0;
}

void condicion(double *c,double x,double t){
    c[0]=exp(-0.5*((x-1)*(x-1)))/(0.25*0.25);
}
void ej(double *ej, double *c, double delta_t, double delta_x){
	ej[0]=(((delta_t+c[0])-(delta_t-c[0]))/(2.0*c[0]))+(((delta_x+c[0])-(delta_x-c[0]))/(2.0*c[0]));
}
void nombre(string filename){

  ofstream outfile;
  outfile.open(filename);
    

}