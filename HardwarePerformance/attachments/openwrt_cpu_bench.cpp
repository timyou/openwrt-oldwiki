
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>
#include <unistd.h>




#define VERSION_STR "v0.1"


long long get_micros()
{
	struct timeval tv;
	int ret = gettimeofday(&tv, NULL);
	//printf("Secs: %d / Usecs: %d\n", tv.tv_sec, tv.tv_usec);
	long long total = (tv.tv_sec*1000000);
       	total += tv.tv_usec;
	return total;
}

float do_run_memory_bench()
{
	long long begin = get_micros();

	int len = (1<<24)/sizeof(int); // 16Mb
	int* buf = new int[len];
	len--;len--;

	// Write to memory - sequential
	for (int i=0;i<len;i++)
	{
		buf[i] = i;
	}

	// Read memory - sequential
	for (int i=0;i<len;i++)
	{
		int a = buf[i];
	}

	// Read memory - random
	for (int i=0;i<len;i++)
	{
		int index = (i*23)%(len/2);
		int a = buf[index];
	}

	// Write memory - random
	for (int i=0;i<len;i++)
	{
		int index = (i*23)%(len/2);
		buf[index] = i;
	}
	
	long long end = get_micros();

	float secs = ((end-begin)/1000000.0);
	printf("Time to run memory bench: %.2f[secs]\n", secs);

	return secs;
}

float run_memory_bench()
{
	float f = do_run_memory_bench();
	f += do_run_memory_bench();
	f += do_run_memory_bench();

	return f;
}

#define NBD 9009
float run_compute_e()
{
	long long begin = get_micros();

	int N=NBD, n=N, a[NBD],x;
	while(--n)
	{
		a[n]=1+1/n;
	}

	for(;N>9;)
	{
		for(n=N--;--n; a[n]=x%n, x=10*a[n-1]+x/n)
		{
		}
	}

	long long end = get_micros();

	float secs = ((end-begin)/1000000.0);
	printf("Time to run computation of e (%d digits): %.2f[secs]\n", NBD, secs);

	return secs;
}

float run_compute_pi()
{
	long long begin = get_micros();

	for (int i=0;i<10;i++)
	{
		int a=10000,b,c=8400,d,e,f[8401],g;
		for(;b-c;)
		{
			f[b++]=a/5;
		}

		for(;d=0,g=c*2;c-=14,e=d%a)
		{
			for(b=c;d+=f[b]*a,f[b]=d%--g,d/=g--,--b;d*=b)
			{
			}
		}
	}
	
	long long end = get_micros();

	float secs = ((end-begin)/1000000.0);
	printf("Time to run computation of pi (2400 digits, 10 times): %.2f[secs]\n", secs);

	return secs;
}


int main()
{
	printf("This is a CPU and memory benchmark. This will then take some time... (typically 30-60 seconds on a 200MHz computer)\n");
	
	float sec_mem = run_memory_bench();

	float sec_pi = run_compute_pi();

	float sec_e = run_compute_e();

	printf("Total time: %.1fs\n", (sec_mem+sec_e+sec_pi));

	time_t t = time(0);
	struct tm* ti = localtime(&t);
	printf("You can copy/paste the following line in the wiki table\n");
	printf("|| %02d-%02d-%04d || 'Author' || %.1fs || %.1fs || %.1fs || " VERSION_STR " || 'DeviceModel' || BCM3302 V0.7 || 200MHz || HwPage ||\n", ti->tm_mday, (ti->tm_mon+1), ti->tm_year, sec_mem, sec_pi, sec_e);

	return 0;
}

