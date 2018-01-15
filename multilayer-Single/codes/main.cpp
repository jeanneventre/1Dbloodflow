#include <network.h>
#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sstream>
#include <time.h>
#include <sys/time.h>

using namespace std;

void print_usage (FILE* stream, int exit_code) {
	fprintf (stream, "Usage: bloodflow -i inputFolder -o dataFolder [-s string] [-q] [-v] \n");
	fprintf (stream,
			"-h --help	Display this usage information.\n"
			"-i --input	folderName Parameter files to initalize the computing.\n"
			"-o --output	folderName Write output to this folder.\n"
			"-s --suffix	string Suffix to the names of output files.\n"
			"-q --sequential sequential computing, otherwise using openMP.\n"
			"-v --verbose	Print verbose messages.\n");
	exit (exit_code);
}

double get_wall_time(){
    struct timeval time;
    if (gettimeofday(&time,NULL)){
        //  Handle error
        return 0;
    }
    return (double)time.tv_sec + (double)time.tv_usec * .000001;
}
double get_cpu_time(){
    return (double)clock() / CLOCKS_PER_SEC;
}

int main(int argc, char* argv[]){

		//  Start Timers
		double wall0 = get_wall_time();
		double cpu0  = get_cpu_time();

    int next_option;
	/* A string listing valid short options letters. */
	const char* const short_options = "hi:o:c:s:vq";
	/* An array describing valid long options. */
	const struct option long_options[] = {
	{ "help", 0, NULL, 'h' },
	{ "output", 1, NULL, 'o' },
	{ "suffix", 1, NULL, 's' },
	{ "verbose", 0, NULL, 'v' },
	{ "sequential", 0, NULL, 'p' },
	{ NULL, 0, NULL, 0 }
	};  	/* Required at end of array. */

	/* The name of the file to receive program output */
    const char* input_folderName = NULL;
	const char* output_folderName = NULL;
    const char* suff_string = NULL;
    /* Whether to display verbose messages. */
    bool verbose = false;
    bool sequential = false;


	do {
	next_option = getopt_long (argc, argv, short_options, long_options, NULL);
	switch (next_option) {
		case 'h':   /* -h or --help */
		             /* User has requested usage information. Print it to standard
                    output, and exit with exit code zero (normal termination). */
		print_usage (stdout, 0);
        case 'i':
		input_folderName = optarg;
        break;

		case 'o':
		output_folderName = optarg;
		break;

        case 's':
		suff_string = optarg;
		break;

		case 'v':	 /* -v or --verbose */
		verbose = true;
		break;

    case 'q':
		sequential = true;
    break;

		case '?':
		/* The user specified an invalid option. */
		/* Print usage information to standard error, and exit with exit
		code one (indicating abnormal termination). */
		print_usage (stderr, 1);

		case -1:
		break;
		/* Done with options.
		*/
		default:
		/* Something else: unexpected.*/
		abort ();
		}
	} while (next_option != -1);

    if (input_folderName == NULL || output_folderName == NULL)
        print_usage(stderr,1);
    printf("Suffix string : %s \n", suff_string);
    printf("Verbose : %s; ",verbose? "Yes": "No");
    printf("Sequential Computing : %s \n", sequential? "Yes":"No");

    struct stat sb;
    if(stat(input_folderName, &sb) != 0 ) {
        printf("Error: no \"%s\" \n",input_folderName);
        exit(1);
    }
    else{
        if (!S_ISDIR(sb.st_mode)){
            printf("Error: \"%s\" exists, but not a foldoer\n",input_folderName);
            exit(1);
        }
    }

    if(stat(output_folderName, &sb) != 0 ) {
        printf("Error: no \"%s\"\n",output_folderName);
        exit(1);
        }
    else{
        if (!S_ISDIR(sb.st_mode)){
            printf("Error: \"%s\" exists, but not a foldoer\n",output_folderName);
            exit(1);
        }
    }

    // Constructor function for the networkxc

   {
        network net(input_folderName);
        net.set_dataFolder(output_folderName);
        if (suff_string != NULL) {
						net.set_suffix(string(suff_string)+"_");
        }
        else {
						net.set_suffix("");
        }
        if (verbose) {
            cout<<"press enter to continue or 0 to quit "<<endl;
            int flag = getchar();
            if(flag == '0')
            exit(0);
        }
        if(sequential) {
					printf("#########################################\n") ;
					printf("%s\n", "Run: SEQUENTIAL");
            net.run();
					}
        else {
					printf("#########################################\n") ;
					printf("%s\n", "Run: OPENMP");
            // net.run_openMP();
        }
    }

		//  Stop timers
		double wall1 = get_wall_time();
		double cpu1  = get_cpu_time();
		printf("#########################################\n") ;
		cout << "Elapsed Time = " << wall1 - wall0 << endl;
		cout << "CPU Time  = " << cpu1  - cpu0  << endl;
		printf("#########################################\n\n") ;

		// Write time to file
	  string Timedatafile = string(output_folderName) + "/Time.csv";
	  FILE* file_time = fopen(Timedatafile.c_str(), "w");
	  fprintf(file_time,
	         "%s,\t %s \n ",
	         "#t_real [s]","t_CPU [s]"
	          );
		fprintf(file_time,
		       "%20.20f ,\t %20.20f \n",
		       wall1 - wall0, cpu1  - cpu0
		        );
	  fflush(file_time);
		fclose(file_time);

		return 0;
}
