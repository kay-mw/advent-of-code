#include "string.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// 112112112
// 1 -> 1.1.2.1.1.2.1.1.2
// 2 -> 11.21.12.11.2
// 3 -> 112.112.112

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

  // char example[] = "1001001";
  //
  // int actual_length = sizeof(example) - 1;
  // int equal = 0;
  // for (int step = 1; step < sizeof(example) / 2; step++) {
  //   char storage[sizeof(example)][50];
  //   equal = 0;
  //   for (int pos = 0; pos < sizeof(example); pos++) {
  //     char ss[20];
  //     if ((pos * step) >= actual_length - step) {
  //       strncpy(ss, example + (pos * step), actual_length);
  //       strcpy(storage[pos], ss);
  //       // printf("Str: %s, Pos: %d, Step: %d, Assignment: %d | Special
  //       // clause!\n",
  //       //        ss, (pos * step), step, pos);
  //       int strings_equal = memcmp(storage[pos - 1], storage[pos], step);
  //       printf(
  //           "Comparison Prev: %s, Comparison Pres: %s, Result: %d, Size:
  //           %d\n", storage[pos - 1], storage[pos], strings_equal, step);
  //       if (strings_equal != 0) {
  //         equal += 1;
  //       }
  //       break;
  //     }
  //     strncpy(ss, example + (pos * step), step);
  //     // printf("Str: %s, Pos: %d, Step: %d, Assignment: %d\n", ss, (pos *
  //     // step),
  //     //        step, pos);
  //     strcpy(storage[pos], ss);
  //     if (pos > 0) {
  //       int strings_equal = memcmp(storage[pos - 1], storage[pos], step);
  //       printf("Comparison Prev: %s, Comparison Pres: %s, Result: %d\n",
  //              storage[pos - 1], storage[pos], strings_equal);
  //       if (strings_equal != 0) {
  //         equal += 1;
  //       }
  //     }
  //   }
  //
  //   if (equal == 0) {
  //     printf("Step: %d\n", step);
  //     break;
  //   }
  // }

  unsigned long invalid_ids[1000];
  int o = 0;
  unsigned long start;
  unsigned long end;
  for (int k = 0; k < i; k++) {
    start = array[k].range_start;
    end = array[k].range_end;

    for (unsigned long num = start; num <= end; num++) {
      int digits = log10(num) + 1;

      char num_str[digits + 1];
      sprintf(num_str, "%lu", num);

      int equal = 0;
      for (int step = 1; step < (sizeof(num_str) + 1) / 2; step++) {
        int inner_size = 500;
        char storage[sizeof(num_str)][inner_size];
        equal = 0;
        for (int pos = 0; pos < sizeof(num_str); pos++) {
          char ss[inner_size];
          if ((pos * step) >= digits - step) {
            strncpy(ss, num_str + (pos * step), digits);
            strcpy(storage[pos], ss);
            // printf("Str: %s, Pos: %d, Step: %d, Assignment: %d | Special
            // clause!\n",
            //        ss, (pos * step), step, pos);
            int strings_equal = memcmp(storage[pos - 1], storage[pos], step);
            // printf("Comparison Prev: %s, Comparison Pres: %s, Result:
            // % d\n ",
            //        storage[pos - 1], storage[pos], strings_equal);
            if (strings_equal != 0) {
              equal += 1;
            }
            break;
          }
          strncpy(ss, num_str + (pos * step), step);
          // printf("Str: %s, Pos: %d, Step: %d, Assignment: %d\n", ss, (pos
          // *
          // step),
          //        step, pos);
          strcpy(storage[pos], ss);
          if (pos > 0) {
            int strings_equal = memcmp(storage[pos - 1], storage[pos], step);
            // printf("Comparison Prev: %s, Comparison Pres: %s, Result:
            // % d\n ",
            //        storage[pos - 1], storage[pos], strings_equal);
            if (strings_equal != 0) {
              equal += 1;
            }
          }
        }
        if (equal == 0) {
          printf("%ld, %d\n", num, step);
          invalid_ids[o] = num;
          o++;
          break;
        }
      }

      // printf("Equal: %d\n", equal);
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
