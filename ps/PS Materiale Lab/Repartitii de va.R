#Repartitii de v.a.
#1.d+nume_repartitie=functie de masa(caz discret)/functia de densitate(caz continuu)
#dgeom(x,p)
#dbinom(x,n,p)
dbinom(3,5,0.4)
#P(X=3)
#dexp(x,lambda)
dexp(3,1)
#NU mai e o probabilitate
#2. p+nume_repartitie=functia de repartitie
 #  pbinom(x,n,p)
   #P(X<=x)
   pbinom(3,5,0.4)
#3. r+nume_repartitie=genereaza valori din acel tip de repartitie
 #  rbinom(nr,n,p)
   rbinom(3,5,0.4)
   #Reprezentari grafice de functii
   #Functia densitate de probabilitate a repartitiei normale
   t <- seq(-6,6,0.001)
   plot(t,dnorm(t,0,1))
   plot(t,dexp(t,2),ylim=c(0,0.))
   #ATENTIE: IN R parametrii normalei sunt media si abaterea medie standard
   y <- rnorm(100,0,1)
   
   poz <- y[y>0]
   prob_nr_poz <- length(poz)/10^2
   neg <- y[y<0]
   prob_nr_neg <- length(neg)/10^2
   
   y <- rnorm(1000000,0,1)
   
   length(y[(y>-3)&(y<3)])
  
   lines(t,dnorm(t,0,1))
   plot(t,dnorm(t,0,1),col="magenta",xlim=c(-8,8),ylim=c(0,1))
   lines(t,dnorm(t,0,4), col=2)
   lines(t,dnorm(t,0,0.5), col=3)
   lines(t,dnorm(t,0,2), col=5)
   lines(t,dnorm(t,0,0.5),col=1)
   
   z <- rnorm(1000,2,1)
   length(z[z< -2])
   
   plot(t,dnorm(t,0,1),col="magenta",ylim=c(0,1.8))
   for (i in c(0.25,0.5,0.3,0.9,1.3,2)) lines(t,dnorm(t,0,i), col=i*20)
   