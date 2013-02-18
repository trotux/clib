#include "clib_internal.h"
#include "testsuite.h"

#include <stdio.h>

int
main(void)
{
	struct sockaddr_storage *sa = NULL;
	int ntest = 0, exitval = 0, special;
	void *ptr;
	uint32_t ip;

	test_expect_int(int, (special = c_str2sockaddr("127.0.0.1:53", &sa)), 0);
	if (special)
		fprintf(stderr, "Error was: %s\n", gai_strerror(special));

	test_expect_int(int, sa->ss_family, AF_INET);
	test_expect_int(short, ((struct sockaddr_in *)sa)->sin_port, htons(53));
	test_expect_str("reserialized IP address", (ptr = c_sockaddr2str(sa)), "127.0.0.1");
	if (ptr)
		free(ptr);
	ptr = NULL;
	free(sa);
	sa = NULL;

	test_expect_int(int, (special = c_str2sockaddr("[::1]:53", &sa)), 0);
	if (special)
		fprintf(stderr, "Error was: %s\n", gai_strerror(special));
	if ( sa )
	{
		test_expect_int(int, sa->ss_family, AF_INET6);
		test_expect_str("reserialized IP address", (ptr = c_sockaddr2str(sa)), "::1");
		if (ptr)
			free(ptr);
		ptr = NULL;
		free(sa);
		sa = NULL;
	}

	exit(exitval ? EXIT_FAILURE : EXIT_SUCCESS);
}

