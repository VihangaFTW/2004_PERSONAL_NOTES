The reason why this approach gives the correct result every time is due to the **stability** of the counting sort algorithm, which is used as a subroutine in radix sort.

A sorting algorithm is said to be **stable** if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted. 

When we sort the words starting from the end, we ensure that for each character position, the words are sorted in a stable manner. This means that when two words have the same character at the current position being considered, their original order is preserved. 

Let's consider an example with the words "cat", "car", and "cap". If we sort these words starting from the end:

1. After the first pass (sorting by the last character), we get: "cap", "car", "cat".
2. After the second pass (sorting by the second character), the order remains the same: "cap", "car", "cat".
3. After the third pass (sorting by the first character), the order still remains the same: "cap", "car", "cat".

As you can see, at each step, the order of the words with the same character at the current position being considered is preserved, which is why we get the correct lexicographical order at the end.

This property of preserving the relative order of records with equal keys is crucial to getting the correct result when sorting words lexicographically with radix sort.

When we’re sorting numbers, we start from the least significant digit (the rightmost digit) because it has the least impact on the overall value of the number. Similarly, when we’re sorting words, we start from the end of the word because the characters at the end of the word have the least impact on the overall lexicographical order of the word.