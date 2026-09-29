/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * ML-DSA-44 verify benchmark: cycles per verify (DWT) and peak stack use.
 * Test vector (bench_vectors.h) is generated on the host by gen_vectors.py.
 */

#include <stdio.h>
#include <string.h>
#include <zephyr/kernel.h>
#include <cmsis_core.h>
#include <mldsa_native.h>

#include BENCH_VECTORS

#define RUNS 10

/* Only the signing/keygen paths use randomness; never called here */
int randombytes(uint8_t *out, size_t outlen)
{
	(void)out;
	(void)outlen;
	return -1;
}

static uint32_t timed_verify(const uint8_t *sig, int *rc)
{
	uint32_t start = DWT->CYCCNT;

	*rc = crypto_sign_verify(sig, sizeof(bench_sig), bench_msg, sizeof(bench_msg),
				 NULL, 0, bench_pk);
	return DWT->CYCCNT - start;
}

int main(void)
{
	static uint8_t bad_sig[sizeof(bench_sig)];
	uint32_t hz = sys_clock_hw_cycles_per_sec();
	uint32_t cyc;
	size_t unused;
	int rc;

	CoreDebug->DEMCR |= CoreDebug_DEMCR_TRCENA_Msk;
	DWT->CYCCNT = 0;
	DWT->CTRL |= DWT_CTRL_CYCCNTENA_Msk;

	printf("BENCH mldsa%d clock_hz=%u pk=%u sig=%u msg=%u\n", MLD_CONFIG_PARAMETER_SET, hz,
	       (unsigned int)sizeof(bench_pk), (unsigned int)sizeof(bench_sig),
	       (unsigned int)sizeof(bench_msg));

	for (int i = 1; i <= RUNS; i++) {
		cyc = timed_verify(bench_sig, &rc);
		printf("BENCH run=%d case=valid rc=%d cyc=%u us=%u\n", i, rc, cyc,
		       cyc / (hz / 1000000U));
	}

	/* Last byte of the signature flipped: must fail */
	memcpy(bad_sig, bench_sig, sizeof(bad_sig));
	bad_sig[sizeof(bad_sig) - 1] ^= 0x01;
	cyc = timed_verify(bad_sig, &rc);
	printf("BENCH run=1 case=bad_sig rc=%d cyc=%u us=%u\n", rc, cyc, cyc / (hz / 1000000U));

	if (k_thread_stack_space_get(k_current_get(), &unused) == 0) {
		size_t size = k_current_get()->stack_info.size;

		printf("BENCH stack size=%u used=%u\n", (unsigned int)size,
		       (unsigned int)(size - unused));
	}
	printf("BENCH done\n");
	return 0;
}
