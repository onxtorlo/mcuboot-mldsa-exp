/*
 * SPDX-License-Identifier: Apache-2.0
 */

#include <stdio.h>

int main(void)
{
	printf("[%s] Hello World! %s\n", APP_TAG, CONFIG_BOARD_TARGET);

	return 0;
}
