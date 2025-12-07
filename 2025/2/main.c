#include "string.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

struct id_range {
  unsigned long range_start;
  unsigned long range_end;
};

int main() {
  FILE *fptr;
  fptr = fopen("2/input.txt", "r");
  int size = 1000;
  char contents[size];
  char *res = fgets(contents, size, fptr);

  struct id_range array[1000] = {};
  char *token, *sub_token;
  int i = 0;
  char *end_token = NULL;
  while ((token = strsep(&res, ","))) {
    struct id_range range;
    int j = 0;
    while ((sub_token = strsep(&token, "-"))) {
      if (j == 0) {
        range.range_start = strtoul(sub_token, &end_token, 10);
      } else {
        range.range_end = strtoul(sub_token, &end_token, 10);
      }
      j++;
    }
    array[i] = range;
    i++;
  }

  unsigned long invalid_ids[1000];
  int o = 0;
  unsigned long start;
  unsigned long end;
  for (int k = 0; k < i; k++) {
    start = array[k].range_start;
    end = array[k].range_end;

    for (unsigned long num = start; num <= end; num++) {
      int digits = log10(num) + 1;
      if (digits % 2 != 0) {
        continue;
      }
      char num_str[digits + 1];
      sprintf(num_str, "%lu", num);
      char first_half[digits / 2];
      char second_half[digits / 2];

      for (int l = 0; l < (digits / 2); l++) {
        first_half[l] = num_str[l];
      }
      int n = 0;
      for (int m = digits / 2; m < digits; m++) {
        second_half[n] = num_str[m];
        n++;
      }
      int equal = memcmp(first_half, second_half, sizeof(first_half));
      if (equal == 0) {
        invalid_ids[o] = num;
        o++;
      }
    }
  }

  unsigned long sum = 0;
  for (int p = 0; p < o; p++) {
    sum += invalid_ids[p];
  }
  printf("%lu\n", sum);

  fclose(fptr);

  return 0;
}
